# The Referral Connection team: GrokBot pack

Four GrokBot agents, one per role (lead, seo, leads, sales), that run SEO, leads and sales for The Referral Connection, the directory site at findreferralpartners.com where local businesses sign up to swap commission referral campaigns ("You send to my list. I send to yours."). Built from the GrokBot Factory template.

Install: create the four agents, then paste the one line from HANDOFF.md Part 1 into each (the lead first). Each downloads or reads the pack from `https://github.com/jbellsolutions/referral-connection-grokbot/releases/latest/download/referral-connection.zip` and sets itself up as its own role.

| File | What |
|---|---|
| [HANDOFF.md](HANDOFF.md) | Paste or attach to GrokBot: The four agents, Justin's steps, then each agent's |
| [NEEDS-JUSTIN.md](NEEDS-JUSTIN.md) | Sign-ins, keys by name, yeses |
| [MASTER-PROMPT.md](MASTER-PROMPT.md) | The team's master prompt; each agent saves it with its own role |
| [CHARTER.md](CHARTER.md) | Purpose, the loop, KPIs, handoffs, workspace, milestones. Wins over a role charter |
| [roles/](roles/) | lead, seo, leads, sales: one agent each: a charter with the system prompt section that agent saves |
| [TRIGGER-MAP.md](TRIGGER-MAP.md) | Every step: started by, role, judgment call, gate. 12 routines, 3 per agent |
| [GATES.md](GATES.md) | The gates and the Ask-first lines for Auto-review |
| [guards/](guards/SKILL.md) | The guard skill and its scripts: suppression, send, spend, heartbeat |
| [skills.json](skills.json), [SKILLS-MAP.md](SKILLS-MAP.md), [skills/](skills/) | Which role uses which skill and account, and the six skills |
| `tools/rc.py` | The site's operator CLI: sign-ups, listings, connection requests, removals, matches, guides, stats |
| [.env.example](.env.example) | Key names only |
| `tools/check.py` | Completeness and secret check: `python3 tools/check.py` |

The site itself (its code and its data) is not in this pack. The agents reach it only through the admin API with a key Justin gives by hidden prompt.
