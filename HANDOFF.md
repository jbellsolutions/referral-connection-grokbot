# The Referral Connection team: the handoff

What Justin does, then what each agent does on its own. Follows the factory PLAYBOOK and the client-build GrokBot standard. Unverified platform facts are flagged *(unverified)*.

## The team: one agent per role

Four GrokBot agents on one Grok account, each with its own chat, memory, skills and routines. Agents on one account share one computer, its files and its logins (factory PLAYBOOK), so all four work in `/workspace/referral-connection/` and hand work to each other through `requests/<role>/`. That memory, skills and routines are each agent's own is *(unverified)*.

| Agent (the bot's name) | Role | Does | Routines |
|---|---|---|---|
| Referral Connection Lead | lead | Plans the day, watchdog, scoreboard, Justin's queue | 3 |
| Referral Connection SEO | seo | Site check, guides, measure | 3 |
| Referral Connection Leads | leads | Finds prospects, drafts outreach, replies | 3 |
| Referral Connection Sales | sales | Intake, listings, matches, introductions | 3 |

## Part 1: Justin

1. **Account.** Sign in at x.ai/bot with the Grok account for **The Referral Connection** only (one account per business). Check the plan covers four bots and their routines. No agent ever buys a plan.
2. **Desktop app.** Open the Grok desktop app. Setup runs in each agent's one-to-one chat there (approval, secret and sign-in requests only show there).
3. **The four agents.** Create four bots named as in the table above, pin them, and set Settings → General → Bot → Timezone to **UTC** on each.
4. **The pack: one link, the lead first.** Paste the line below into **Referral Connection Lead** (`bin/publish` made the link). If it can't download, attach the zip from the same release instead *(zip route unverified)*.

   > You are the lead agent of The Referral Connection team. Download https://github.com/jbellsolutions/referral-connection-grokbot/releases/latest/download/referral-connection.zip, unpack it into /workspace/referral-connection/repo/ and follow HANDOFF.md: Part 2A, then Part 2B as lead. Read MASTER-PROMPT.md and CHARTER.md first. Ask me one thing at a time. Nothing sends, posts, spends or writes to a CRM until I say yes in this chat.

5. **The other three agents.** When the lead says Part 2A is done, paste this into each of the other three, with its own role (seo, leads, sales) in place of ROLE:

   > You are the ROLE agent of The Referral Connection team. The pack is in /workspace/referral-connection/repo/ (if it is not there, download https://github.com/jbellsolutions/referral-connection-grokbot/releases/latest/download/referral-connection.zip and unpack it there). Follow HANDOFF.md Part 2B as ROLE. Read MASTER-PROMPT.md and CHARTER.md first. Ask me one thing at a time. Nothing sends, posts, spends or writes to a CRM until I say yes in this chat.

6. **Auto-review rules.** At Part 2A step 3, paste the Ask-first lines the lead shows into Auto-review → Custom Rules.
7. **Sign-ins and keys.** When an agent asks, sign in through Connect apps, one at a time. Keys go only through a secure secret card or the hidden terminal prompt with **Take over**. Rotate first any key ever pasted in a chat.

## Part 2A: the lead agent sets up the shared ground (once)

1. **Workspace.** Create `/workspace/referral-connection/` with `context/`, `daily/`, `requests/` (one folder per role, plus `justin`), `approved/`, `data/` (mode 600), `log/`, `vault/` (Obsidian: `Daily/`, `People/`, `Decisions.md`), `state/` and `state/test/`, `.secrets/` (mode 700). Write `context/routines-on.md` with every routine `off` and `crm-writes: off`, `context/standing-approvals.md` (empty), `context/spend-approvals.md` (empty) and `context/team-registry.md` (one section per agent). Don't create `context/STOP`. Start `log/setup.md`. Run `python3 repo/tools/check.py` and paste its RESULT line into `log/setup.md`.
2. **Intake.** Ask Justin, one at a time: the Slack channel for this team; the Notion page for the scoreboard and Drafts; the launch area (the first city or metro, and trades if any); the address and tool that member emails go out from; whether a suppression list already exists; whether the sales agent may apply removal requests itself (`rc.py remove`) or queues each one for him; which message types, if any, are already approved. Write `context/launch-area.md` from his answer. Write `context/owner.md`; save the suppression list as `context/suppression.csv`; mark approved templates in `standing-approvals.md`.
3. **Approval rules.** Show Justin the Ask-first lines from GATES.md to paste.
4. **Keys.** Put each key name in `.env.example` into `.secrets/<system>.env` by hidden prompt, one at a time. The other agents read them from there.
5. **Old agents.** None known; Justin confirms. The site has one admin key: of the four agents only sales writes its records, and only seo writes its guide pages.
6. **Tell Justin** that Part 2A is done and the other three agents can start, then do Part 2B as lead.

## Part 2B: each agent sets itself up (all four, as its own role)

1. **Memory.** Save MASTER-PROMPT.md to memory word for word with your role in place of `<role>`, then the "System prompt section" from `roles/<your role>.md` under it. Save no other role's section.
2. **Skills.** Save `guards/SKILL.md` and every `skills/<your role>/<skill>/SKILL.md` as a private skill (skills.json lists each role's).
3. **Connect, read-only, one at a time.** Do the rows of this table that name your role. Each gets a Check that reads one real record into `log/setup.md`. A sign-in another agent already made is there for you too; run the Check anyway.

   | App | Agents | Check |
   |---|---|---|
   | Slack `(the channel Justin names at intake)` | lead | Read the last message |
   | Notion | lead | Read today's scoreboard row |
   | Referral Connection site | seo, leads, sales | `python3 repo/tools/rc.py stats` returns `"ok": true` and the counts |
   | Email (the sender Justin names) | leads, sales | Read the last message in the inbox |
   | Google Search Console | seo | List the properties; findreferralpartners.com is there |

4. **Routines, switched off.** Create your role's routines from TRIGGER-MAP.md (the section with your role's name), paused, in your own bot. Each prompt starts `Role: <your role>.` Record each in your section of `context/team-registry.md` with cron, time zone and next run. A next run an hour or more off means the time zone isn't set.
5. **Report.** Read back your routines and connections into `context/team-registry.md` and tell Justin what is set up and what isn't and why. The lead, once all four sections are filled, sends Justin the whole list.

## Usage kit (usage-mastery v1.0.0)

From `grokbot-usage-mastery`. The lead does steps 1, 3, 4 and 6 once, after Part 2A. Every agent does steps 2 and 5 after its own memory step.

1. Run `bash repo/usage/scripts/install.sh` (free, pinned, no keys) and paste its last line into `log/setup.md`.
2. Save `repo/usage/SKILL.md` as a private skill named usage-saver.
3. Copy `repo/usage/LEDGER.md` to `log/usage-ledger.md`. Ask Justin for the baseline reading (Settings → Usage: % used and reset date) before the first test day, and again after it.
4. The weekly audit (`repo/usage/AUDIT.md`) runs inside the Monday evening report; it adds no routine and changes nothing.
5. Check: `bash repo/usage/scripts/grep_lines.sh 'usage-mastery v' repo/usage/.. 3` prints at least one line (the rules are in place and the scripts run).
6. Show Justin the two owner-only steps, once per Grok account, and record the answers in `log/setup.md`:
   - A spending cap: grok.com/dashboard/billing → a monthly additional-usage limit, or Auto top-up off. No agent changes billing.
   - Three lines for Auto-review → Custom Rules (chat only; routines never wait on approvals):

     ```
     Ask first before opening more than 5 web pages for one task.
     Ask first before starting a sub-agent or a second bot on a job.
     Ask first before re-running a step that has already failed twice.
     ```
## Bring-up order

| # | Agent | Why this order | Turned on first |
|---|---|---|---|
| 1 | lead | Plans, watchdog, scoreboard | Morning plan, watchdog, scoreboard |
| 2 | sales (intake only) | Reads sign-ups, lists real ones, queues removals. Nothing reaches a person | Intake |
| 3 | seo | Read-only site check, then guide drafts | Site check, Guides (drafts) |
| 4 | leads (find only) | Builds the prospect file from public pages | Find prospects |
| 5 | sales (match) | Introductions are messages to members | Match and introduce, Follow matched pairs |
| 6 | leads (outreach) | Cold messages and group posts, last because they touch deliverability and public channels | Draft outreach, Replies and follow-ups | |

## The first-day test run

Every routine is `test` in `context/routines-on.md`, so nothing reaches a person. **Test on a routine does real work**: the `test` line goes in before every Test press.

| Step | Agent | Do | Pass when |
|---|---|---|---|
| 1 | lead | Morning plan | A plan for every agent in `daily/<date>/lead.md` and in Slack |
| 2 | sales | Intake, after Justin submits one sign-up on the site with a name starting TEST | The TEST sign-up is read back; `daily/<date>/sales.md` has the counts; no real listing was changed |
| 3 | seo | Site check | `daily/<date>/seo.md` has the sitemap count and zero failing URLs |
| 4 | seo | Guides | One guide saved as a draft; its public URL returns 404; the brief is in `daily/<date>/seo.md` |
| 5 | leads | Find prospects | Rows in `data/prospects.csv` for the launch area, each with a public source |
| 6 | leads | Draft outreach | Drafts in `requests/justin/`; nothing sent |
| 7 | sales | Match and introduce | A match recorded between two TEST sign-ups; the introduction is a draft in `requests/justin/`; then the TEST records are removed on Justin's yes |
| n-2 | All | Suppression test | A known suppressed name is held by every drafting agent |
| n-1 | All | STOP test | Create `context/STOP`; the next run of every agent says stopped and does nothing; remove it |
| n | lead | Evening scoreboard | Every agent has a line; today's vault note exists; `beat.py status` shows no SILENT; nothing was sent |

The day passes when every row passes and `state/` shows 0 sends. Then Justin approves each message type once, and agents go `on` one at a time.

## Reporting back

| Where | What | Written by |
|---|---|---|
| Slack `(the channel Justin names at intake)` | Morning plan, alarms (silent agents, unapproved sends), evening scoreboard, Justin's queue | lead |
| Notion | Scoreboard row a day; Drafts waiting on Justin | lead |
| The workspace vault | `vault/Daily/<date>.md`, `People/`, `Decisions.md` | lead writes the daily note; each agent adds its section |
| The single brain | A scrubbed status line and the daily summary, no raw transcripts or contact data | lead's nightly routine (deploy key) or Justin's Mac pulls: decision on NEEDS-JUSTIN |
