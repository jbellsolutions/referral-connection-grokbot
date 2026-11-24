# The Referral Connection site agent

One agent for one site, [findreferralpartners.com](https://findreferralpartners.com): a free directory where businesses get customers from each other. Justin, 2026-11-24: "Can you give me a separate referral site, the agent for the referral site only? Give me that separately. I'm going to put it in the other Grok Bot."

**Install:** one line, in [INSTALL.md](INSTALL.md), pasted into a bot Justin already runs. It is an add-on: it keeps to its own folder and adds one memory section, one skill and four routines. **What only Justin can do:** [NEEDS-JUSTIN.md](NEEDS-JUSTIN.md).

## How it works

The bot only orchestrates. Each routine hands one job to the **Claude Code CLI** (`tools/job.py`), with the **Codex CLI** as the second engine.

| Job | What it does | When (UTC) |
|---|---|---|
| [referral-desk](jobs/referral-desk.md) | Sign-ups, listings, connection and removal requests; pairs matched, introduced and followed | 13:20 and 20:20 daily |
| [referral-growth](jobs/referral-growth.md) | Fills the launch area: prospects, outreach drafts, public asks (social, Skool, Whop), one post a day | 15:20 weekdays |
| [referral-guides](jobs/referral-guides.md) | A guide per pillar, the site check, the Tuesday read of search and AI answers | 14:20 Tuesday and Friday |
| [referral-report](jobs/referral-report.md) | The nightly numbers, tomorrow's focus, jobs counted by engine | 23:50 daily |

## What is in the pack

| | |
|---|---|
| `MASTER-PROMPT.md`, `roles/` | The memory section the bot adds |
| `jobs/` | One brief per job, which the CLI works from |
| `skills/` | The CLI rule, and the six site skills: directory-desk, matchmaker, prospect-finder, outreach-drafts, guide-publisher, site-check |
| `tools/job.py` | Hands a job to Claude Code, then Codex; logs which engine carried it |
| `tools/rc.py` | The site's admin API: reads freely, writes only when the switches allow, otherwise saves the proposal |
| `campaigns/referral-connection/` | The message (a draft), the plan |
| `guards/`, `convlog/` | The switches' checks; the log of every draft, send and reply |
| `tools/install.py`, `team.py`, `check.py` | The installer and the checks |

## Not in this pack

The site's code (Justin's private repo: the agent never builds or deploys it), and the host bot's own pack, which this add-on does not change.
