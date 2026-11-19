# Project charter: Referral Connection Bot

The bot loads this page first. Where a role's charter and this page differ, this page wins.

## Purpose

The Referral Connection is a directory site (findreferralpartners.com) where local businesses sign up to be connected for commission referral campaigns: "You send to my list. I send to yours." Each partner emails their own list about the other, once, and they pay each other commission on the sales. This bot does the three jobs that make the site a business: it gets the site found (SEO), it gets local businesses to sign up (leads), and it turns sign-ups into listings, matches and introduced pairs that run a campaign (sales). Done well looks like one area at a time filling with real listed businesses, each matched with a partner, and Justin seeing every number with its proof.

Justin's words, 2026-11-18: "They sign up to get connected to others in the area that want to do referral relationships that pay on commission. You send to my list, I send to your list... this is referral campaigns." And: "give it to GrokBot, and let GrokBot go promote the crap out of it."

## The loop

1. **Intake** (sales). Read new sign-ups, connection requests and removal requests from the site. Mark spam. Apply removals.
2. **List** (sales). Each real sign-up that ticked the directory box gets a listing with a one-line blurb written from what they typed. Their state, city and category pages appear on the site by themselves.
3. **Match** (sales). Pair sign-ups in the same area that share a kind of customer and don't compete. Record the match. Draft the introduction to both.
4. **Introduce and follow** (sales). On approval the introduction goes out. Follow each pair from introduced to agreed, sent and paid.
5. **Find** (leads). Build the list of local businesses in the launch area that have customers they can email. No paid enrichment.
6. **Reach** (leads). Draft the outreach that gets them to sign up, each link tagged so the sign-up's source shows what worked.
7. **Publish** (seo). Write guides that answer what an owner looking for referral partners asks, save them as drafts on the site, and publish on approval.
8. **Measure** (seo, lead). Sign-ups by source and area, listings, matches by stage, pages indexed. Double down on what the records show.

Each step's trigger and judgment call is in [TRIGGER-MAP.md](TRIGGER-MAP.md).

## KPIs

| Measure | Target | Source |
|---|---|---|
| Silent roles | None for more than 26 hours | Factory standard |
| Messages sent without an approved template | 0 | Factory standard |
| Sign-ups, listings, matches introduced, by area | Counted daily from `rc.py stats`, no target set | Justin sets the launch area and targets at intake |

## Gates

Every gate in [GATES.md](GATES.md). They never move.

## Handoffs between roles

Through files only: `daily/<date>/<role>.md` for what each role did, `requests/<role>/<id>.md` for work handed over, `requests/justin/` for Justin's queue.

| From | What | To |
|---|---|---|
| Any role | Price, terms, an upset person, an account warning | `requests/justin/` |
| leads | A reply that says yes or asks how it works | `requests/sales/` |
| sales | An area with listings but no partner categories; a category nobody has signed up for | `requests/leads/` |
| sales | A question members keep asking | `requests/seo/` (a guide) |
| seo | A new guide or area page that is live | `requests/leads/` (a link worth sharing) |
| lead | The launch area and the day's plan | every role, in `daily/<date>/lead.md` |

## Roles

| Role | Job | Routines |
|---|---|---|
| [lead](roles/lead.md) | Plans the day, watchdog, scoreboard, the vault daily note, Justin's queue | 3 |
| [seo](roles/seo.md) | Guides, the site check, search and AI-answer visibility | 3 |
| [leads](roles/leads.md) | Finds local businesses in the launch area and drafts the outreach that gets them to sign up | 3 |
| [sales](roles/sales.md) | Intake, listings, removals, matches, introductions, follow-up to a paid campaign | 3 |

## Workspace

`/workspace/referral-connection/`: `repo/` (this pack), `context/` (owner, routines-on, standing-approvals, team-registry, suppression, launch-area), `daily/<date>/`, `requests/<role>/` and `requests/justin/`, `approved/`, `data/` (mode 600: prospects, exports), `log/runs-<YYYY-MM>.md`, `vault/` (Obsidian: `Daily/`, `People/`, `Decisions.md`), `state/` and `state/test/`, `.secrets/` (mode 700).

## Milestones

| # | Milestone | Done when |
|---|---|---|
| K0 | Account and bot | Justin signed in, the bot has the pack and wrote `log/setup.md` |
| K1 | Read-only | The site, Slack and Notion connected, each with one real record read back (`rc.py stats` for the site) |
| K2 | Routines | Every routine created and paused, read back into `team-registry.md` |
| K3 | Test day | The first-day run in HANDOFF.md passes with zero sends and zero publishes |
| K4 | Drafts approved | Justin approved each message type once |
| K5 | Low-risk lanes on | sales intake and listing, the seo site check, leads finding (nothing reaches a person) |
| K6 | Outreach and introductions on | Outreach, introductions and guides marked `auto` one type at a time |

## Done means

K6 reached: the site fills one area at a time without Justin doing the work, and he sees the scoreboard in Slack and Notion and the daily note in the vault, with every number traceable to a record on the site.
