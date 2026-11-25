#!/usr/bin/env python3
"""Classroom MCP server: the checks and builders behind the teaching skills.

A Model Context Protocol server over stdio, written against the standard
library only, so it runs anywhere Python 3.10+ does with nothing to install.

    python3 classroom_server.py            # serve over stdio (what Claude runs)
    python3 classroom_server.py --list     # print the tools and exit
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "vendor"))

from classroom.tools import TOOLS, ToolError, call  # noqa: E402

NAME, VERSION = "classroom", "1.0.0"
PROTOCOLS = ["2025-06-18", "2025-03-26", "2024-11-05"]
INSTRUCTIONS = (
    "Tools for teachers. Use check_answer_key (or fix_answer_key) on every multiple-choice set and sort task "
    "before it reaches students. Use recall_starter, log_attempts and progress_review when the teacher keeps a "
    "question bank and an attempts log. Use validate_lesson then build_lesson_page to turn a lesson into the "
    "interactive student page. Use check_reports on any batch of reports and text_stats for word limits and "
    "reading level. Refer to students by initials or ids, never full names."
)


def _result(id_, result):
    return {"jsonrpc": "2.0", "id": id_, "result": result}


def _error(id_, code, message):
    return {"jsonrpc": "2.0", "id": id_, "error": {"code": code, "message": message}}


def handle(msg: dict) -> dict | None:
    """Handle one JSON-RPC message. Returns the reply, or None for notifications."""
    method, id_ = msg.get("method"), msg.get("id")
    if method is None:
        return None  # a response to something we never asked; ignore
    if id_ is None:
        return None  # notification (e.g. notifications/initialized)
    params = msg.get("params") or {}
    if method == "initialize":
        asked = params.get("protocolVersion")
        return _result(id_, {
            "protocolVersion": asked if asked in PROTOCOLS else PROTOCOLS[0],
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": {"name": NAME, "version": VERSION},
            "instructions": INSTRUCTIONS,
        })
    if method == "ping":
        return _result(id_, {})
    if method == "tools/list":
        return _result(id_, {"tools": [
            {"name": n, "description": t["description"], "inputSchema": t["schema"]} for n, t in TOOLS.items()
        ]})
    if method == "tools/call":
        name = params.get("name")
        if name not in TOOLS:
            return _error(id_, -32602, f"Unknown tool: {name}")
        try:
            out = call(name, params.get("arguments"))
            text, is_error = json.dumps(out, ensure_ascii=False, indent=2), False
        except ToolError as e:
            text, is_error = str(e), True
        except Exception as e:  # never take the server down for one bad call
            text, is_error = f"{type(e).__name__}: {e}", True
        return _result(id_, {"content": [{"type": "text", "text": text}], "isError": is_error})
    if method in {"resources/list", "prompts/list"}:
        return _result(id_, {method.split("/")[0]: []})
    return _error(id_, -32601, f"Method not found: {method}")


def serve(stdin=sys.stdin, stdout=sys.stdout) -> None:
    for line in stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            reply = _error(None, -32700, "Parse error")
        else:
            if isinstance(msg, list):
                replies = [r for r in (handle(m) for m in msg) if r is not None]
                reply = replies or None
            else:
                reply = handle(msg)
        if reply is not None:
            stdout.write(json.dumps(reply, ensure_ascii=False) + "\n")
            stdout.flush()


if __name__ == "__main__":
    if "--list" in sys.argv:
        for n, t in TOOLS.items():
            print(f"{n}: {t['description'][:90]}")
    else:
        serve()
