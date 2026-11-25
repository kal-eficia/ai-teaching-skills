import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path

SERVER = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SERVER))
sys.path.insert(0, str(SERVER / "vendor"))

from classroom import tools  # noqa: E402
from classroom.tools import ToolError  # noqa: E402


def mcq(i, answer, n=4, last=None):
    opts = [f"Q{i} option {k}" for k in range(n)]
    if last:
        opts[-1] = last
    return {"q": f"Question {i}?", "options": opts, "answer": answer}


BANK = [
    {"id": "H1", "topic": "CPU", "question": "What does the ALU do?", "answer": "Arithmetic and logic"},
    {"id": "H2", "topic": "CPU", "question": "What does the PC hold?", "answer": "Address of next instruction"},
    {"id": "M1", "topic": "Memory", "question": "Why is RAM volatile?", "answer": "Loses data without power"},
    {"id": "M2", "topic": "Memory", "question": "One use of ROM?", "answer": "Boot instructions"},
    {"id": "S1", "topic": "Storage", "question": "How does an SSD store data?", "answer": "Flash memory"},
    {"id": "S2", "topic": "Storage", "question": "One drawback of cloud storage?", "answer": "Needs internet"},
]
LOG = [
    {"student": "S01", "question_id": "H1", "date": "2026-10-05", "result": "wrong"},
    {"student": "S01", "question_id": "M1", "date": "2026-10-05", "result": "wrong"},
    {"student": "S01", "question_id": "H2", "date": "2026-10-06", "result": "right"},
    {"student": "S01", "question_id": "H1", "date": "2026-11-10", "result": "right"},
    {"student": "S01", "question_id": "M1", "date": "2026-11-11", "result": "right"},
    {"student": "S01", "question_id": "H2", "date": "2026-11-12", "result": "right"},
    {"student": "S01", "question_id": "S1", "date": "2026-11-12", "result": "wrong"},
]
QUESTION = {
    "q": "Why is RAM described as volatile?", "marks": 2,
    "points": [
        {"id": "lose", "label": "it loses its contents", "accept": [[["lose", "lost", "wiped", "cleared"], ["data", "content", "memory"]]]},
        {"id": "power", "label": "when the power is turned off", "accept": ["power", "switched off", "turned off", "electricity"]},
    ],
}
LESSON = {
    "title": "Inside the CPU", "subject": "Computer Science",
    "pages": [
        {"title": "Starter", "blocks": [
            {"type": "mcq", "id": "s1", "q": "Which part does calculations?", "options": ["ALU", "CU", "Cache", "PC"], "answer": 0, "why": "The ALU."},
            {"type": "mcq", "id": "s2", "q": "Which register holds the next address?", "options": ["PC", "MDR", "ACC", "CIR"], "answer": 0, "why": "The PC."},
            {"type": "mcq", "id": "s3", "q": "Which bus is one way?", "options": ["Address", "Data", "Control", "Serial"], "answer": 0, "why": "Address."},
        ]},
        {"title": "Learn", "blocks": [
            {"type": "text", "heading": "The cycle", "body": "The CPU **fetches**, decodes and executes."},
            {"type": "sort", "id": "t1", "prompt": "Sort these.", "buckets": ["Register", "Bus"],
             "items": [{"text": "MAR", "bucket": "Register"}, {"text": "Address", "bucket": "Bus"},
                       {"text": "MDR", "bucket": "Register"}, {"text": "Data", "bucket": "Bus"}]},
            {"type": "write", "id": "w1", "prompt": "Explain the fetch stage in your own words.", "minWords": 20},
        ]},
    ],
}


class AnswerKeys(unittest.TestCase):
    def test_bare_key(self):
        self.assertFalse(tools.check_answer_key(key="ABCDABCD")["ok"])
        self.assertTrue(tools.check_answer_key(key="CADBDACB")["ok"])

    def test_bad_key_is_a_readable_error(self):
        with self.assertRaises(ToolError):
            tools.check_answer_key(key="12345")
        with self.assertRaises(ToolError):
            tools.check_answer_key()

    def test_questions_and_fix(self):
        quiz = [mcq(i, i % 4) for i in range(8)]
        self.assertFalse(tools.check_answer_key(questions=quiz)["ok"])
        fixed = tools.fix_answer_key(questions=quiz, seed=3)
        self.assertTrue(fixed["ok"])
        for old, new in zip(quiz, fixed["questions"]):
            self.assertEqual(old["options"][old["answer"]], new["options"][new["answer"]])
            self.assertEqual(sorted(old["options"]), sorted(new["options"]))
        self.assertEqual(quiz[0]["answer"], 0, "the caller's questions must not be changed in place")

    def test_fix_keeps_all_of_the_above_last(self):
        quiz = [mcq(i, i % 3, last="All of the above") for i in range(8)]
        for seed in range(10):
            fixed = tools.fix_answer_key(questions=quiz, seed=seed)
            self.assertTrue(all(q["options"][-1] == "All of the above" for q in fixed["questions"]))

    def test_fix_writes_file(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "quiz.json"
            p.write_text(json.dumps({"title": "T", "questions": [mcq(i, 0) for i in range(6)]}))
            out = tools.fix_answer_key(quiz_path=str(p), write=True, seed=1)
            self.assertTrue(out["ok"])
            saved = json.loads(p.read_text())
            self.assertEqual(saved["title"], "T")
            self.assertTrue(tools.check_answer_key(quiz_path=str(p))["ok"])

    def test_sort_task_checked(self):
        task = {"type": "sort", "id": "x", "items": [{"text": str(i), "bucket": "A" if i < 4 else "B"} for i in range(8)]}
        rep = tools.check_answer_key(questions=[task])
        self.assertFalse(rep["ok"])
        self.assertTrue(tools.fix_answer_key(questions=[task], seed=2)["ok"])

    def test_plan(self):
        for n in (5, 12, 30):
            out = tools.plan_answer_key(length=n, options=4, seed=n)
            self.assertEqual(len(out["key"]), n)
            self.assertTrue(tools.check_answer_key(key=out["key"], options=4)["ok"])
        with self.assertRaises(ToolError):
            tools.plan_answer_key(length=0)


class Retrieval(unittest.TestCase):
    def test_starter_prioritises_wrong_and_interleaves(self):
        out = tools.recall_starter(bank=BANK, log=LOG, student="S01", size=4, today="2026-11-20", seed=1)
        ids = [q["id"] for q in out["questions"]]
        self.assertIn("S1", ids)  # wrong last time
        self.assertEqual(len(ids), len(set(ids)))
        topics = [q["topic"] for q in out["questions"]]
        self.assertTrue(all(a != b for a, b in zip(topics, topics[1:])) or len(set(topics)) < 3)
        self.assertTrue(all(q["why_chosen"] for q in out["questions"]))

    def test_starter_without_a_log_uses_all_topics(self):
        out = tools.recall_starter(bank=BANK, size=5, seed=1)
        self.assertEqual(len(out["questions"]), 5)

    def test_starter_hides_answers(self):
        out = tools.recall_starter(bank=BANK, log=LOG, student="S01", show_answers=False, today="2026-11-20")
        self.assertTrue(all("answer" not in q for q in out["questions"]))

    def test_review(self):
        out = tools.progress_review(bank=BANK, log=LOG, student="S01", today="2026-11-14")
        cpu = next(t for t in out["topics"] if t["topic"] == "CPU")
        self.assertEqual((cpu["baseline_pct"], cpu["recent_pct"], cpu["change_points"]), (50, 100, 50))
        self.assertIn("Storage", out["needs_attention"])
        self.assertIn("Storage", out["not_comparable"])

    def test_review_unknown_student(self):
        with self.assertRaises(ToolError):
            tools.progress_review(bank=BANK, log=LOG, student="nobody")

    def test_log_attempts_then_use_it(self):
        with tempfile.TemporaryDirectory() as d:
            log = str(Path(d) / "sub" / "attempts.csv")
            tools.log_attempts(log_path=log, attempts=[{"student": "S02", "question_id": "H1", "result": "wrong"}], today="2026-11-01")
            tools.log_attempts(log_path=log, attempts=[{"student": "S02", "question_id": "M1", "result": True, "date": "2026-11-02"}])
            with open(log, newline="", encoding="utf-8") as f:
                rows = list(csv.DictReader(f))
            self.assertEqual([r["result"] for r in rows], ["wrong", "right"])
            out = tools.recall_starter(bank=BANK, log=log, student="S02", today="2026-11-10", size=3)
            reasons = {q["id"]: q["why_chosen"] for q in out["questions"]}
            self.assertEqual(reasons.get("H1"), "got it wrong last time")


class Marking(unittest.TestCase):
    def test_marks_and_feedback(self):
        out = tools.mark_answers(question=QUESTION, answers=[
            {"student": "S01", "answer": "It loses its data when the power is turned off."},
            {"student": "S02", "answer": "It is fast."},
            "The data is lost.",
        ])
        scores = [r["score"] for r in out["results"]]
        self.assertEqual(scores, [2, 0, 1])
        self.assertEqual(out["results"][2]["student"], "#3")
        self.assertEqual(out["class_summary"]["most_missed_points"][0]["point"], "when the power is turned off")

    def test_needs_points(self):
        with self.assertRaises(ToolError):
            tools.mark_answers(question={"q": "x"}, answers=["y"])


class Lessons(unittest.TestCase):
    def test_valid_lesson(self):
        out = tools.validate_lesson(lesson=LESSON)
        self.assertTrue(out["ok"], out)
        self.assertEqual(out["stats"]["mcq"], 3)

    def test_catches_problems(self):
        bad = json.loads(json.dumps(LESSON))
        bad["pages"][0]["blocks"][1]["id"] = "s1"                       # duplicate id
        bad["pages"][0]["blocks"][2]["answer"] = 9                      # out of range
        bad["pages"][1]["blocks"][1]["items"][0]["bucket"] = "Nope"     # unknown bucket
        bad["pages"][1]["blocks"][0]["body"] = "Students should copy this down."
        out = tools.validate_lesson(lesson=bad)
        self.assertFalse(out["ok"])
        joined = " ".join(out["errors"])
        self.assertIn("used twice", joined)
        self.assertIn("index of the correct option", joined)
        self.assertIn("isn't listed", joined)
        self.assertTrue(any("teacher note" in w for w in out["warnings"]))

    def test_build_page(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "lesson.html"
            out = tools.build_lesson_page(out_path=str(p), lesson=LESSON)
            self.assertTrue(out["built"])
            page = p.read_text()
            self.assertIn('data-lesson="lesson"', page)
            self.assertIn("Inside the CPU", page)
            self.assertNotIn('src="lesson-kit.js"', page)  # self-contained
            start = page.index('id="lesson">') + len('id="lesson">')
            embedded = json.loads(page[start:page.index("</script>", start)])
            self.assertEqual(embedded["pages"][0]["blocks"][0]["id"], "s1")

    def test_build_refuses_broken_lesson(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "lesson.html"
            out = tools.build_lesson_page(out_path=str(p), lesson={"title": "x", "pages": [{"title": "a", "blocks": []}]})
            self.assertFalse(out["built"])
            self.assertFalse(p.exists())

    def test_script_in_lesson_text_cannot_break_out(self):
        with tempfile.TemporaryDirectory() as d:
            evil = json.loads(json.dumps(LESSON))
            evil["pages"][1]["blocks"][0]["body"] = "</script><script>alert(1)</script>"
            p = Path(d) / "l.html"
            tools.build_lesson_page(out_path=str(p), lesson=evil)
            self.assertNotIn("</script><script>alert(1)", p.read_text())

    def test_endpoint_must_be_https(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ToolError):
                tools.build_lesson_page(out_path=str(Path(d) / "l.html"), lesson=LESSON, endpoint="javascript:alert(1)")


GOOD = ("[S1] explains how a CPU works more clearly than most of the group, and his quiz scores show it. "
        "The next step is getting that depth onto paper, so he will plan each long answer with six quick points "
        "before writing. With that habit in place he is ready for the top grades, and he should be proud of "
        "how far his explanations have come since September.")


class Writing(unittest.TestCase):
    def test_reports_pass(self):
        other = ("This term [S2] has gone from 41% to 68%, one of the biggest improvements in the class, and it came "
                 "from steady work on every homework. Binary conversions are where marks still slip, so ten minutes "
                 "of practice twice a week will fix that. Her consistency is her real strength, and it is clearly "
                 "paying off in lessons and in her written answers too.")
        out = tools.check_reports(reports=[{"student": "[S1]", "text": GOOD}, {"student": "[S2]", "text": other}])
        self.assertTrue(out["ok"], out)

    def test_reports_catch_repeats_jargon_and_length(self):
        out = tools.check_reports(reports=[
            {"student": "Amir Khan", "text": "Amir is a pleasure to teach and he always works hard in every lesson. He is working towards AO2."},
            {"student": "Sara Ali", "text": "Sara is a pleasure to teach and she always works hard in every lesson. She has done well."},
        ])
        self.assertFalse(out["ok"])
        issues = " | ".join(i for r in out["reports"] for i in r["issues"])
        self.assertIn("under the minimum", issues)
        self.assertIn("repeated from Amir Khan", issues)
        self.assertIn("pleasure to teach", issues)
        self.assertIn("AO2", issues)
        self.assertIn("no clear next step", issues)

    def test_text_stats(self):
        easy = tools.text_stats(text="The cat sat on the mat. It was a big cat. The dog ran to the park.", target_age=9)
        hard = tools.text_stats(text="Notwithstanding the aforementioned considerations, the organisational "
                                     "restructuring necessitates comprehensive reconsideration of interdepartmental "
                                     "responsibilities and accountability mechanisms throughout the institution.", target_age=9)
        self.assertTrue(easy["on_target"])
        self.assertFalse(hard["on_target"])
        self.assertGreater(hard["reading_age_estimate"], easy["reading_age_estimate"] + 5)
        self.assertEqual(tools.text_stats(text="one two three", max_words=2)["within_limit"], False)


class Registry(unittest.TestCase):
    def test_every_tool_has_schema_and_runs_through_call(self):
        for name, t in tools.TOOLS.items():
            self.assertEqual(t["schema"]["type"], "object", name)
            self.assertGreater(len(t["description"]), 40, name)
        self.assertTrue(tools.call("check_answer_key", {"key": "CADB"})["ok"])
        with self.assertRaises(ToolError):
            tools.call("check_answer_key", {"nonsense": 1})
        with self.assertRaises(ToolError):
            tools.call("no_such_tool", {})


if __name__ == "__main__":
    unittest.main()
