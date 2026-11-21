# Trigger map

The loop is deterministic: schedules start every step, and the agent makes only the judgment call inside it. Gates stay on until replies prove good. Every cron is UTC. Each role is its own agent (its own GrokBot), and each agent creates only its own role's routines. **50 routines max per bot**; `tools/check.py` counts the cron rows below. The team uses 12, 3 per agent.

## The loop, step by step

| # | Step | Started by | Role | Judgment call | Human gate |
|---|---|---|---|---|---|
| 1 | Plan the day | Schedule `30 13 * * *` | lead | Which area and which lane matters today | None |
| 2 | Intake: sign-ups, connection requests, removals | Schedule `0 14,18,22 * * *` | sales | Real business or spam; what the blurb should say | Listing writes wait for `crm-writes: on` |
| 3 | Find prospects in the launch area | Schedule `30 14 * * *` | leads | Does this business have customers it can email; which partner category it fills | None (nothing reaches a person) |
| 4 | Site check | Schedule `0 15 * * *` | seo | Is anything broken, thin or missing | None (read-only) |
| 5 | Draft outreach | Schedule `0 16 * * *` | leads | The one reason this business would want a partner | Every send, until the type is `auto` |
| 6 | Match and draft introductions | Schedule `0 17 * * *` | sales | Same customer, different trade, lists of similar size, commission that fits | Every introduction, until `auto` |
| 7 | Replies and follow-ups | Schedule `0 19 * * *` | leads | Yes, no, question, or hand to Justin | Every send, until `auto`; a no goes to suppression |
| 8 | Follow matched pairs | Schedule `30 19 * * *` | sales | Where the pair is stuck | Every send, until `auto` |
| 9 | Guides | Schedule `0 15 * * 2,4` | seo | Which question is worth a page; is every claim true | First public post waits for Justin (GATES.md) |
| 10 | Measure | Schedule `0 16 * * 5` | seo | What the records say worked | None |
| 11 | Watchdog | Schedule `0 * * * *` | lead | None: code decides | None |
| 12 | Report | Schedule `30 23 * * *` | lead | Proof check on each number | None |

## Every schedule and event, by role

### lead

| Kind | When or what | Does |
|---|---|---|
| Schedule | `30 13 * * *` | Morning plan |
| Schedule | `0 * * * *` | Watchdog |
| Schedule | `30 23 * * *` | Evening scoreboard and vault daily note |

### seo

| Kind | When or what | Does |
|---|---|---|
| Schedule | `0 15 * * *` | Site check: health, sitemap, every listed area page loads, no draft is public |
| Schedule | `0 15 * * 2,4` | Guides: one brief, one draft, saved to the site as a draft |
| Schedule | `0 16 * * 5` | Measure: sign-ups by source, pages, the fixed question panel |

### leads

| Kind | When or what | Does |
|---|---|---|
| Schedule | `30 14 * * *` | Find prospects in the launch area |
| Schedule | `0 16 * * *` | Draft outreach for today's prospects |
| Schedule | `0 19 * * *` | Replies and follow-ups |

### sales

| Kind | When or what | Does |
|---|---|---|
| Schedule | `0 14,18,22 * * *` | Intake: sign-ups, listings, connection requests, removals |
| Schedule | `0 17 * * *` | Match and draft introductions |
| Schedule | `30 19 * * *` | Follow matched pairs |
