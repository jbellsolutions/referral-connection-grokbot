# Job: referral-guides

The site's guides, its health, and whether it is being found.

## Read first

- `repo/skills/guide-publisher/SKILL.md` and `repo/skills/site-check/SKILL.md`.
- `repo/campaigns/referral-connection/MESSAGING.md`: the eight pillars. One guide per pillar first.
- `requests/guides/`: questions members and prospects actually asked.

## Do

1. **Site check**, by the skill. Read-only. A fault is one line at the top of the daily file and one file in `requests/justin/`: the site's code is Justin's, and the agent never changes or deploys it.
2. **One guide**, by the guide-publisher skill: choose the question, write it, check it, and save it with `python3 repo/tools/rc.py page-put <slug> --title ... --description ... --html <file>` (no `--publish`: a guide goes public only once `rc_guide: auto`; `rc.py` holds it otherwise). The item file for Justin goes in `requests/justin/` and is logged with `CAMPAIGN=referral-connection python3 repo/convlog/gate.py drafted <file> --agent referral-connection`.
3. **On Tuesdays, the read.** The panel is `data/referral/panel.md`: ten questions an owner would ask a search engine or an AI assistant (write it the first time). For each, search the public web and note whether findreferralpartners.com is named and who is named instead. Write `data/referral/read-<today>.md`: named on N of 10, the three questions closest to a win, and the guide that would win each.
4. A guide published since the last run: its link goes to `requests/growth/` as something to post about.

## Write

`daily/<today>/guides.md`: URLs in the sitemap, URLs failing, guides saved as draft and published, and on Tuesdays the read's N of 10.
