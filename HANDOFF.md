# Referral Connection Bot: the handoff

What Justin does, then what the bot does on its own. Follows the factory PLAYBOOK and the client-build GrokBot standard. Unverified platform facts are flagged *(unverified)*.

## Part 1: Justin

1. **Account.** Sign in at x.ai/bot with the Grok account for **The Referral Connection** only (one account per business). Check the plan covers bots and routines. The bot never buys a plan.
2. **Desktop app.** Open the Grok desktop app. Setup runs in the one-to-one chat there (approval, secret and sign-in requests only show there).
3. **The bot.** Create one bot named **Referral Connection Bot**, pin it, and set Settings → General → Bot → Timezone to **UTC**.
4. **The pack: one link.** Paste the line below into the new bot (`bin/publish` made the link). If the bot can't download, attach the zip from the same release instead *(zip route unverified)* and paste:

   > You are Referral Connection Bot. Download https://github.com/jbellsolutions/referral-connection-grokbot/releases/latest/download/referral-connection.zip, unpack it into /workspace/referral-connection/repo/ and follow HANDOFF.md, Part 2, from step 1. Read MASTER-PROMPT.md and CHARTER.md first. Ask me one thing at a time. Nothing sends, posts, spends or writes to a CRM until I say yes in this chat.

5. **Auto-review rules.** At Part 2 step 4, paste the Ask-first lines it shows into Auto-review → Custom Rules.
6. **Sign-ins and keys.** When it asks, sign in through Connect apps, one at a time. Keys go only through a secure secret card or the hidden terminal prompt with **Take over**. Rotate first any key ever pasted in a chat.

## Part 2: the bot

1. **Workspace.** Create `/workspace/referral-connection/` with `context/`, `daily/`, `requests/` (one folder per role, plus `justin`), `approved/`, `data/` (mode 600), `log/`, `vault/` (Obsidian: `Daily/`, `People/`, `Decisions.md`), `state/` and `state/test/`, `.secrets/` (mode 700). Write `context/routines-on.md` with every routine `off` and `crm-writes: off`, `context/standing-approvals.md` (empty), `context/spend-approvals.md` (empty) and `context/team-registry.md`. Don't create `context/STOP`. Start `log/setup.md`. Run `python3 repo/tools/check.py` and paste its RESULT line into `log/setup.md`.
2. **Memory and skills.** Save MASTER-PROMPT.md to memory word for word, then each role's "System prompt section" from `roles/`. Save `guards/SKILL.md` and every `skills/<role>/<skill>/SKILL.md` as a private skill. Put each key name in `.env.example` into `.secrets/<system>.env` by hidden prompt, one at a time.
3. **Intake.** Ask Justin, one at a time: the Slack channel for this bot; the Notion page for the scoreboard and Drafts; the launch area (the first city or metro, and trades if any); the address and tool that member emails go out from; whether a suppression list already exists; whether this bot may apply removal requests itself (`rc.py remove`) or queues each one for him; which message types, if any, are already approved. Write `context/launch-area.md` from his answer. Write `context/owner.md`; save the suppression list as `context/suppression.csv`; mark approved templates in `standing-approvals.md`.
4. **Approval rules.** Show Justin the Ask-first lines from GATES.md to paste.
5. **Connect, read-only, one at a time.** Each gets a Check that reads one real record into `log/setup.md`.

   | App | Roles | Check |
   |---|---|---|
   | Slack `(the channel Justin names at intake)` | lead | Read the last message |
   | Notion | lead | Read today's scoreboard row |
   | Referral Connection site | seo, leads, sales | `python3 repo/tools/rc.py stats` returns `"ok": true` and the counts |
| Email (the sender Justin names) | leads, sales | Read the last message in the inbox |
| Google Search Console | seo | List the properties; findreferralpartners.com is there |

6. **Old agents.** None known; Justin confirms. The site has one admin key, so a second bot with that key would write the same records.
7. **Routines, switched off.** Create every routine in TRIGGER-MAP.md, paused. Each prompt starts `Role: <role>.` Record each in `team-registry.md` with role, cron, time zone and next run. A next run an hour or more off means the time zone isn't set.
8. **Report.** Read back every routine and connection into `team-registry.md`, and send Justin the list plus what isn't done and why.

## Usage kit (usage-mastery v1.0.0)

From `grokbot-usage-mastery`. Do these right after the workspace and memory steps.

1. Run `bash repo/usage/scripts/install.sh` (free, pinned, no keys) and paste its last line into `log/setup.md`.
2. Save `repo/usage/SKILL.md` as a private skill named usage-saver.
3. Copy `repo/usage/LEDGER.md` to `log/usage-ledger.md`. Ask Justin for the baseline reading (Settings → Usage: % used and reset date) before the first test day, and again after it.
4. The weekly audit (`repo/usage/AUDIT.md`) runs inside the Monday evening report; it adds no routine and changes nothing.
5. Check: `bash repo/usage/scripts/grep_lines.sh 'usage-mastery v' repo/usage/.. 3` prints at least one line (the rules are in place and the scripts run).
6. Show Justin the two owner-only steps, once per Grok account, and record the answers in `log/setup.md`:
   - A spending cap: grok.com/dashboard/billing → a monthly additional-usage limit, or Auto top-up off. The bot never changes billing.
   - Three lines for Auto-review → Custom Rules (chat only; routines never wait on approvals):

     ```
     Ask first before opening more than 5 web pages for one task.
     Ask first before starting a sub-agent or a second bot on a job.
     Ask first before re-running a step that has already failed twice.
     ```
## Bring-up order

| # | Role | Why this order | Turned on first |
|---|---|---|---|
| 1 | lead | Plans, watchdog, scoreboard | Morning plan, watchdog, scoreboard |
| 2 | sales (intake only) | Reads sign-ups, lists real ones, queues removals. Nothing reaches a person | Intake |
| 3 | seo | Read-only site check, then guide drafts | Site check, Guides (drafts) |
| 4 | leads (find only) | Builds the prospect file from public pages | Find prospects |
| 5 | sales (match) | Introductions are messages to members | Match and introduce, Follow matched pairs |
| 6 | leads (outreach) | Cold messages and group posts, last because they touch deliverability and public channels | Draft outreach, Replies and follow-ups | |

## The first-day test run

Every routine is `test` in `context/routines-on.md`, so nothing reaches a person. **Test on a routine does real work**: the `test` line goes in before every Test press.

| Step | Role | Do | Pass when |
|---|---|---|---|
| 1 | lead | Morning plan | A plan for every role in `daily/<date>/lead.md` and in Slack |
| 2 | sales | Intake, after Justin submits one sign-up on the site with a name starting TEST | The TEST sign-up is read back; `daily/<date>/sales.md` has the counts; no real listing was changed |
| 3 | seo | Site check | `daily/<date>/seo.md` has the sitemap count and zero failing URLs |
| 4 | seo | Guides | One guide saved as a draft; its public URL returns 404; the brief is in `daily/<date>/seo.md` |
| 5 | leads | Find prospects | Rows in `data/prospects.csv` for the launch area, each with a public source |
| 6 | leads | Draft outreach | Drafts in `requests/justin/`; nothing sent |
| 7 | sales | Match and introduce | A match recorded between two TEST sign-ups; the introduction is a draft in `requests/justin/`; then the TEST records are removed on Justin's yes |
| n-2 | All | Suppression test | A known suppressed name is held by every drafting role |
| n-1 | All | STOP test | Create `context/STOP`; the next run of every role says stopped and does nothing; remove it |
| n | lead | Evening scoreboard | Every role has a line; today's vault note exists; `beat.py status` shows no SILENT; nothing was sent |

The day passes when every row passes and `state/` shows 0 sends. Then Justin approves each message type once, and roles go `on` one at a time.

## Reporting back

| Where | What | Written by |
|---|---|---|
| Slack `(the channel Justin names at intake)` | Morning plan, alarms (silent roles, unapproved sends), evening scoreboard, Justin's queue | lead |
| Notion | Scoreboard row a day; Drafts waiting on Justin | lead |
| The workspace vault | `vault/Daily/<date>.md`, `People/`, `Decisions.md` | lead writes the daily note; each role adds its section |
| The single brain | A scrubbed status line and the daily summary, no raw transcripts or contact data | lead's nightly routine (deploy key) or Justin's Mac pulls: decision on NEEDS-JUSTIN |
