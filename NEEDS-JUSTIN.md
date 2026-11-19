# NEEDS-JUSTIN: Referral Connection Bot

Only what Justin can do. Each line: what, the exact click or command, what it unblocks. Ticked off in order when he works the list.

| # | What | The exact step | What it unblocks |
|---|---|---|---|
| 1 | [ ] Grok account for The Referral Connection | Sign in at x.ai/bot with the account for this business (or an existing bot, if this is to be a role set on it); check the plan includes bots and routines | Everything |
| 2 | [ ] Create the bot | Grok desktop app: new bot "Referral Connection Bot", time zone UTC, paste the message in HANDOFF.md Part 1 step 4 | Setup |
| 3 | [ ] Auto-review rules | Paste the Ask-first lines from GATES.md into Auto-review → Custom Rules | Safe routines |
| 4 | [ ] Sign-ins | Slack, Notion, Email (the sender for member emails), Google Search Console, through Connect apps when the bot asks | Read-only checks |
| 5 | [ ] Keys, by hidden prompt (names only) | `SLACK_BOT_TOKEN`, `NOTION_TOKEN`, `RC_ADMIN_KEY` (the site's admin key: it is the `ADMIN_KEY` variable on the site's Railway service) | The tools each role uses. `RC_SITE` is `https://findreferralpartners.com`; until that domain's DNS is set, give the bot the site's Railway address instead |
| 6 | [ ] Launch area | Tell the bot the first city or metro, and trades if any | Leads and the first matches |
| 7 | [ ] Removals | Say whether the bot may apply a removal request itself (`rc.py remove <email>` deletes that member's records) or queues each one for you. The factory gate says the bot never deletes data; the site's privacy page promises removal | Removal requests being honoured |
| 8 | [ ] Suppression list | Give the bot the file when it asks (never in the repo), or say there is none yet | Any draft to a person |
| 9 | [ ] Single brain path | "Deploy key" (the bot pushes its daily note) or "Mac pulls" | Reports reach the single brain |
| 10 | [ ] Approve each message type once | Reply yes to each draft type in Notion Drafts (`outreach-first`, `outreach-followup`, `reply`, `group-post`, `introduction`, `match-followup`, `guide`); say "auto" for a type once its replies look right | Sends and published guides |
