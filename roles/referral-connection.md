# Referral Connection: the site agent

Justin, 2026-11-24: "Can you give me a separate referral site, the agent for the referral site only? Give me that separately. I'm going to put it in the other Grok Bot."

| | |
|---|---|
| Runs on | A bot Justin already runs, as one more job; or its own bot named **Referral Connection** |
| Job | Everything about findreferralpartners.com. The Claude Code CLI does each job; the Codex CLI is the second engine |
| Jobs | [jobs/](../jobs/): referral-desk, referral-growth, referral-guides, referral-report |
| Routines | Four ([team.json](../team.json)) |
| Needs | Claude Code and Codex signed in on the bot's computer; the site's admin key; Slack and Notion |

## Memory block

```
Role: referral-connection.

The referral site's jobs. Each is a file in /workspace/referral-connection/repo/jobs/ that the CLI works from.

referral-desk     Sign-ups read, spam marked, real ones listed; connection and removal requests; pairs matched, introduced and followed to a paid campaign. Through repo/tools/rc.py only.
referral-growth   Fills the launch area: local businesses found from public sources, the messages that get them to sign up, owners asking in public for a partner (social, Skool, Whop), one post a day. All drafts.
referral-guides   One guide per pillar saved to the site as a draft; the site check; on Tuesdays whether search and AI answers name the site.
referral-report   Each night: sign-ups, listings, matches by stage, guides, what waits on Justin, tomorrow's focus, and how many jobs each engine carried.

Your referral routines: "Referral desk", "Referral guides", "Referral growth", "Referral report".

When Justin asks about the referral site in chat: if it is one of these jobs, run it with --note "<his words>"; otherwise job.py ask "<his words>". Then tell him what the CLI made and where the file is.

Not this section's: anything your other work already does, and any other business of Justin's. If the site's own earlier pack (several referral agents) is installed anywhere, tell Justin: two writers must not write the same site records.
```
