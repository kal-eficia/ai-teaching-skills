---
name: agent-build-spec
description: Turn an app idea into a phase-gated build spec and copy-paste phase prompts for an AI coding agent (Replit Agent, Claude Code, Cursor, Lovable), with a visual stop gate after every phase so the agent can't drift. Use when someone wants to build an app, tool or website with an AI agent, says "spec this out", "how should I structure this build" or "write me the Replit prompts".
---

# Agent Build Spec

AI coding agents are fast and literal. Give them a vague brief and they will build something fast and wrong. Give them one phase at a time, each ending in something you can *see*, and they build what you meant.

## Principles

- **Show before plumbing.** Phase 1 is always the full UI with fake data. You judge it with your eyes before any database, auth or API exists. Changing a screen is cheap; changing a schema under live data is not.
- **One phase, one visible result.** Every phase ends with a stop gate: something to click or look at, and a short checklist.
- **The agent doesn't decide scope.** Every prompt says what is in this phase and what is explicitly *not*.
- **Builds are fast.** Phases take minutes to an hour, not days. Plan in phases, not weeks.

## Step 1: Interview (keep it short)

Ask only what you need: who uses it, the one job it does, the three screens that matter most, what data it holds, whether people sign in, and the look (a reference site or three adjectives). Note anything sensitive (children's data, payments, health) because that changes the security phase.

## Step 2: Write `SPEC.md`

```
# <App name>
One sentence: who it's for and the job it does.

## Users and the core loop
## Screens (each: purpose, key elements, empty state, mobile notes)
## Data (entities, fields, who can see what)
## Look and feel (fonts, colours, references, tone of copy)
## Out of scope for v1
## Phases (table: phase, goal, stop gate)
```

## Step 3: Phase plan (default; adapt it)

| Phase | Goal | Stop gate |
|---|---|---|
| 1. Cinema | Every screen, real copy, fake data, fully clickable | Click through on phone and laptop; does it *feel* right? |
| 2. Data | Real database and models, seeded with realistic sample data | Create, edit, delete one of everything |
| 3. Accounts | Sign-in, roles, permissions | Log in as each role; try to see what you shouldn't |
| 4. Integrations | Email, payments, AI calls, file uploads | One real end-to-end run of each |
| 5. Polish and safety | Empty/error/loading states, accessibility, security review, rate limits | Checklist below passes |
| 6. Ship | Deploy, domain, analytics, backups | Live URL works on a fresh phone |

## Step 4: Write each phase prompt

Each prompt is self-contained and copy-pasteable:

```
PHASE <n> of <total>: <name>
Context: <one paragraph on the app, link to SPEC.md>
Build now: <bullet list>
Do NOT build yet: <bullet list>
Constraints: <stack, design rules, "no new dependencies without asking">
When done: stop. Show me <the stop gate>. List anything you assumed.
```

## Security checklist (phase 5, never skip)

- [ ] Secrets only in environment variables, never in code or the client
- [ ] Every API route checks who is asking and what they may see
- [ ] Inputs validated server-side; output escaped
- [ ] Rate limits on anything that costs money (AI calls, email)
- [ ] If children use it: minimum data, no public profiles, nothing indexed
