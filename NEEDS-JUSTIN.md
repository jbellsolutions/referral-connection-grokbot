# NEEDS-JUSTIN

Everything only Justin can do for the referral site agent, in one list. The agent drafts everything else without any of it.

| # | What | The exact step | Unblocks |
|---|---|---|---|
| 1 | [ ] Paste the line | Paste the line from INSTALL.md into the bot you chose for the site (or a new bot, if you want the site on its own) | The install |
| 2 | [ ] Claude Code and Codex on that bot | Say "CLI status". If either is "not answering": for Claude Code run `claude setup-token` on your own computer and give the token at the hidden prompt (saved as `CLAUDE_CODE_OAUTH_TOKEN`), or sign in from the bot's terminal; for Codex run `codex login` in the bot's terminal | The jobs running on your subscriptions. Until then each job falls to the bot itself |
| 3 | [ ] The site's admin key | By hidden prompt: `RC_ADMIN_KEY` (the `ADMIN_KEY` variable on the site's service) | Reading sign-ups, listings and matches. Until then the desk works on practice rows |
| 4 | [ ] The agent writes the site's records | Read a day of `requests/justin/site-proposals-<date>.md`. Then say "referral-site: bot" and "crm-writes: on". For removal requests say "removals: apply" or leave them queued for you | Listings, matches and guide drafts on the site |
| 5 | [ ] The message | Read `campaigns/referral-connection/MESSAGING.md`: a draft from the site's own words, with no research behind it. Say "use it", give your own, or "research it first" | Anything public |
| 6 | [ ] The launch area and a sender | Name the first city or metro, and the address introductions and outreach go from | Outreach and introductions for a real area |
| 7 | [ ] The opt-out list and the never-touch list | Give the same opt-out file that bot's other work uses, and the names of computers, agents and accounts the agent must never use | Any draft addressed to a person; any write to the site |
| 8 | [ ] Slack and Notion | Name the channel and the page the nightly report goes to | The report |
| 9 | [ ] The site's pages | Say "yes, change the site" in the site's own chat, so its pages and form cover collaborations, partnerships, sponsorships and deals, not only commission referral campaigns | The site matching what the agent says |
| 10 | [ ] Skool and Whop | Name any community to read, and sign the bot's browser in to it | Public asks past public pages |
| 11 | [ ] Search | Verify the site in Google Search Console and Bing | The Tuesday read against real search numbers |

## The switches that make it run without you

After you have seen a type's drafts, say "<type>: auto": `rc_introduction`, `rc_match_followup`, `rc_outreach_first`, `rc_outreach_followup`, `rc_reply`, `rc_group_post`, `rc_guide`. Say "<routine>: on" to take a routine off test. These stay yours whatever is on: the site's code and pages, a price or a fee, terms between two owners, anyone upset.
