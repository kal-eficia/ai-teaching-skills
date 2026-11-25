---
description: Write a batch of student reports and check them for repeated wording, jargon and length
argument-hint: <my notes on each student, word limit>
---

Write reports from these notes: $ARGUMENTS

1. Follow the `student-report-writer` skill: a real strength, one doable next step, a positive close, different wording for every student. Use placeholders such as [S1] unless my teaching context allows names.
2. Call `check_reports` on the whole batch with my word limits (default 60 to 90). Rewrite anything it flags and check again until every report passes.
3. Give me the table (student, report, word count) and flag any student where my notes were too thin to say something specific.
