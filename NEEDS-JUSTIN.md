# NEEDS-JUSTIN: The Referral Connection team

Only what Justin can do. Each line: what, the exact click or command, what it unblocks. Ticked off in order when he works the list.

| # | What | The exact step | What it unblocks |
|---|---|---|---|
| 1 | [ ] Grok account for The Referral Connection | Sign in at x.ai/bot with the account for this business ; check the plan includes four bots and their routines | Everything |
| 2 | [ ] Create the four agents | Grok desktop app: four new bots, "Referral Connection Lead", "Referral Connection SEO", "Referral Connection Leads", "Referral Connection Sales", each on time zone UTC. Paste the message in HANDOFF.md Part 1 step 4 into the Lead; when it says Part 2A is done, paste the step 5 message into the other three | Setup |
| 3 | [ ] Auto-review rules | Paste the Ask-first lines from GATES.md into Auto-review → Custom Rules | Safe routines |
| 4 | [ ] Sign-ins | Slack, Notion, Email (the sender for member emails), Google Search Console, through Connect apps when an agent asks | Read-only checks |
| 5 | [ ] Keys, by hidden prompt (names only) | `SLACK_BOT_TOKEN`, `NOTION_TOKEN`, `RC_ADMIN_KEY` (the site's admin key: it is the `ADMIN_KEY` variable on the site's Railway service) | The tools each role uses. `RC_SITE` is `https://findreferralpartners.com` |
| 6 | [ ] Launch area | Tell the lead agent the first city or metro, and trades if any | Leads and the first matches |
| 7 | [ ] Removals | Say whether the sales agent may apply a removal request itself (`rc.py remove <email>` deletes that member's records) or queues each one for you. The factory gate says an agent never deletes data; the site's privacy page promises removal | Removal requests being honoured |
| 8 | [ ] Suppression list | Give the lead agent the file when it asks (never in the repo), or say there is none yet | Any draft to a person |
| 9 | [ ] Single brain path | "Deploy key" (the lead agent pushes the daily note) or "Mac pulls" | Reports reach the single brain |
| 10 | [ ] Approve each message type once | Reply yes to each draft type in Notion Drafts (`outreach-first`, `outreach-followup`, `reply`, `group-post`, `introduction`, `match-followup`, `guide`); say "auto" for a type once its replies look right | Sends and published guides |
