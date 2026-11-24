# The Referral Connection (findreferralpartners.com)

Justin, 2026-11-20: "building out that site to attract clients who want to do collaborations, partnerships, sponsorships, and deals with others." And 2026-11-24: "the Referral Connection site (which is a disruptor product in and of itself)."

The message: [MESSAGING.md](MESSAGING.md), a draft until Justin confirms it. The plan: [LAUNCH.md](LAUNCH.md).

## Who it is for

Business owners who want a partner: someone to collaborate with, sponsor or be sponsored by, do a deal with, or swap commission referral campaigns with.

## The site, and what the agent does not do

A directory on its own server. People sign up, real sign-ups get a listing, and a visitor can ask to be connected to a listed business. The agent reaches it only through its admin API (`tools/rc.py`). The site's code is Justin's private repo: the agent never builds or deploys it. A fault, or a page the site needs, is a brief in `requests/justin/`. Its pages today say commission referral campaigns only; the brief for all four is NEEDS-JUSTIN 9.

## The numbers, and where each comes from

| Number | Source |
|---|---|
| Sign-ups, by source and by area | `python3 repo/tools/rc.py stats` |
| Listings, and areas with a listing | `rc.py listings` |
| Matches by stage: proposed, introduced, agreed, sent, paid | `rc.py matches` |
| Guides published and reachable | `rc.py pages`, the site check |
| Whether search and AI answers name the site | The Tuesday read (a panel of 10 questions) |
| Jobs carried by Claude Code, Codex and the bot | `python3 repo/tools/job.py audit` |

Message types: `rc_outreach_first`, `rc_outreach_followup`, `rc_reply`, `rc_group_post`, `rc_introduction`, `rc_match_followup`, `rc_guide`.

## One writer

Only one agent writes the site's records. The site's earlier pack ran several referral agents; if it is installed anywhere, it is switched off before this one writes.
