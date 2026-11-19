# Referral Connection Bot: GrokBot pack

One GrokBot that runs SEO, leads and sales for The Referral Connection, the directory site at findreferralpartners.com where local businesses sign up to swap commission referral campaigns ("You send to my list. I send to yours."). Built from the GrokBot Factory template.

Install: tell a new GrokBot to download `https://github.com/jbellsolutions/referral-connection-grokbot/releases/latest/download/referral-connection.zip` and follow HANDOFF.md.

| File | What |
|---|---|
| [HANDOFF.md](HANDOFF.md) | Paste or attach to GrokBot: Justin's steps, then the bot's |
| [NEEDS-JUSTIN.md](NEEDS-JUSTIN.md) | Sign-ins, keys by name, yeses |
| [MASTER-PROMPT.md](MASTER-PROMPT.md) | The bot's master prompt |
| [CHARTER.md](CHARTER.md) | Purpose, the loop, KPIs, handoffs, workspace, milestones. Wins over a role charter |
| [roles/](roles/) | lead, seo, leads, sales: one charter each, with a system prompt section to paste |
| [TRIGGER-MAP.md](TRIGGER-MAP.md) | Every step: started by, role, judgment call, gate. 12 routines |
| [GATES.md](GATES.md) | The gates and the Ask-first lines for Auto-review |
| [guards/](guards/SKILL.md) | The guard skill and its scripts: suppression, send, spend, heartbeat |
| [skills.json](skills.json), [SKILLS-MAP.md](SKILLS-MAP.md), [skills/](skills/) | Which role uses which skill and account, and the six skills |
| `tools/rc.py` | The site's operator CLI: sign-ups, listings, connection requests, removals, matches, guides, stats |
| [.env.example](.env.example) | Key names only |
| `tools/check.py` | Completeness and secret check: `python3 tools/check.py` |

The site itself (its code and its data) is not in this pack. The bot reaches it only through the admin API with a key Justin gives it by hidden prompt.
