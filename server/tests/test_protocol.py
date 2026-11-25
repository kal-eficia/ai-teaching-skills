"""Protocol tests: talk to the server over stdio the way an MCP client does."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

SERVER = Path(__file__).resolve().parent.parent / "classroom_server.py"


class Client:
    def __init__(self):
        self.p = subprocess.Popen([sys.executable, str(SERVER)], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, text=True, encoding="utf-8")
        self.n = 0

    def send(self, method, params=None, notify=False):
        msg = {"jsonrpc": "2.0", "method": method}
        if params is not None:
            msg["params"] = params
        if not notify:
            self.n += 1
            msg["id"] = self.n
        self.p.stdin.write(json.dumps(msg) + "\n")
        self.p.stdin.flush()
        return None if notify else json.loads(self.p.stdout.readline())

    def raw(self, line):
        self.p.stdin.write(line + "\n")
        self.p.stdin.flush()
        return json.loads(self.p.stdout.readline())

    def close(self):
        self.p.stdin.close()
        self.p.wait(timeout=5)
        self.p.stdout.close()
        self.p.stderr.close()


class Protocol(unittest.TestCase):
    def setUp(self):
        self.c = Client()
        self.init = self.c.send("initialize", {"protocolVersion": "2025-06-18", "capabilities": {},
                                               "clientInfo": {"name": "test", "version": "0"}})
        self.c.send("notifications/initialized", notify=True)

    def tearDown(self):
        self.c.close()

    def test_initialize(self):
        r = self.init["result"]
        self.assertEqual(r["protocolVersion"], "2025-06-18")
        self.assertEqual(r["serverInfo"]["name"], "classroom")
        self.assertIn("tools", r["capabilities"])

    def test_unknown_protocol_version_falls_back(self):
        c = Client()
        r = c.send("initialize", {"protocolVersion": "1999-01-01", "capabilities": {}, "clientInfo": {"name": "t", "version": "0"}})
        self.assertEqual(r["result"]["protocolVersion"], "2025-06-18")
        c.close()

    def test_tools_list(self):
        tools = self.c.send("tools/list")["result"]["tools"]
        names = {t["name"] for t in tools}
        self.assertTrue({"check_answer_key", "fix_answer_key", "recall_starter", "mark_answers",
                         "build_lesson_page", "check_reports"} <= names)
        for t in tools:
            self.assertEqual(t["inputSchema"]["type"], "object")

    def test_tool_call(self):
        r = self.c.send("tools/call", {"name": "check_answer_key", "arguments": {"key": "ABCDABCD"}})["result"]
        self.assertFalse(r["isError"])
        self.assertFalse(json.loads(r["content"][0]["text"])["ok"])

    def test_tool_error_is_reported_not_fatal(self):
        r = self.c.send("tools/call", {"name": "check_answer_key", "arguments": {"key": "999"}})["result"]
        self.assertTrue(r["isError"])
        self.assertIn("letters", r["content"][0]["text"])
        self.assertIn("result", self.c.send("ping"))  # still alive

    def test_unknown_tool_and_method(self):
        self.assertEqual(self.c.send("tools/call", {"name": "nope", "arguments": {}})["error"]["code"], -32602)
        self.assertEqual(self.c.send("does/not/exist")["error"]["code"], -32601)

    def test_bad_json_does_not_kill_the_server(self):
        self.assertEqual(self.c.raw("{not json")["error"]["code"], -32700)
        self.assertIn("result", self.c.send("ping"))

    def test_nothing_but_json_on_stdout(self):
        self.c.send("tools/call", {"name": "plan_answer_key", "arguments": {"length": 10}})
        self.c.p.stdin.close()
        rest = self.c.p.stdout.read()
        self.assertEqual(rest.strip(), "")


@unittest.skipUnless(__import__("importlib").util.find_spec("mcp"), "official mcp client not installed")
class OfficialClient(unittest.TestCase):
    def test_official_sdk_can_use_the_server(self):
        import asyncio

        from mcp import ClientSession, StdioServerParameters
        from mcp.client.stdio import stdio_client

        async def run():
            params = StdioServerParameters(command=sys.executable, args=[str(SERVER)])
            async with stdio_client(params) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    tools = await session.list_tools()
                    out = await session.call_tool("plan_answer_key", {"length": 8, "options": 4, "seed": 1})
                    return [t.name for t in tools.tools], out

        names, out = asyncio.run(run())
        self.assertIn("build_lesson_page", names)
        self.assertFalse(getattr(out, 'isError', getattr(out, 'is_error', False)))
        self.assertEqual(len(json.loads(out.content[0].text)["key"]), 8)


if __name__ == "__main__":
    unittest.main()
