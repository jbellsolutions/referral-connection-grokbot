# Job: referral-growth

Fill the directory, one area at a time. Everything here is a draft: the agent never sends, posts, comments or joins.

## Read first

- `repo/skills/prospect-finder/SKILL.md` and `repo/skills/outreach-drafts/SKILL.md`.
- `repo/campaigns/referral-connection/MESSAGING.md`: the position, the pillars, the voice. It is a draft until Justin confirms it; so is everything made from it.
- `context/launch-area.md`: the area. If it is not there, work one sample metro, name it in the daily file, and add one line to `requests/justin/open-questions.md`, once.
- `requests/growth/`: the gaps the desk job found, and the guides just published.
- `context/revenue-os/referral-connection/lead-radar.json`; `data/communities/<today>/*.txt` if the bot saved any.

## Do

1. **Prospects**, by the prospect-finder skill: up to 25 local businesses a run in the trades that are missing, each with the public page it came from, into `data/prospects.csv`. Public sources only; no paid data.
2. **Outreach drafts**, by the outreach-drafts skill: a first message for each new prospect and the follow-ups that are due, every link tagged with its source. Message types `rc_outreach_first`, `rc_outreach_followup`. `python3 repo/guards/scripts/suppression.py check "<business>"` first; `held` means skip.
3. **Public asks.** Owners asking in public for a partner, a sponsor, a collaboration or a deal, on public social pages and in the Skool and Whop communities (the saved text, or a public page read with WebFetch). For each real one: a helpful draft answer that asks for nothing and has no link (`rc_reply`).
4. **Audience holders.** Chambers, associations, networking groups, local newsletters and podcasts, coworking spaces: up to five a run into `data/referral/dream100.csv` with the public source, and a first-touch draft for each (`rc_outreach_first`).
5. **One post**, on one pillar, pointing to the sign-up page (`rc_group_post`), in `content/drafts/<today>-post.md`.

Each draft is an item file in `requests/justin/` (ITEM, ROLE: referral-connection, ---PAYLOAD---, TO, SUBJECT, TEXT, ---END---) logged with `CAMPAIGN=referral-connection python3 repo/convlog/gate.py drafted <file> --agent referral-connection`.

## Write

`daily/<today>/growth.md`: prospects added by trade, drafts by type, asks found, audience holders added, anyone skipped by the opt-out list.
