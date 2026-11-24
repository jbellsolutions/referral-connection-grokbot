# Job: referral-desk

The directory's front desk and the matchmaking. Everything goes through `python3 repo/tools/rc.py` (run it with `-h` once). It reads freely. It writes only when Justin's switches allow; otherwise it saves the exact write to `requests/justin/site-proposals-<today>.md` and prints PROPOSED. Either way you run the same commands.

If `rc.py stats` says the key is not set: work the desk against six made-up sign-ups you write to `data/referral/practice.json`, write the listings, pairs and introductions you would make into the daily file, and say plainly that it was practice. Count nothing from it.

## Read first

- `repo/skills/directory-desk/SKILL.md` and `repo/skills/matchmaker/SKILL.md`: the steps, in order.
- `repo/campaigns/referral-connection/CAMPAIGN.md`: what the site is and what the agent does not touch.
- `requests/desk/`: anything the other jobs or Justin left.

## Do

1. **Intake**, by the directory-desk skill: `rc.py stats`; removal requests first (`rc.py removals`; `rc.py remove <email>` for each open one); new sign-ups read, spam marked, each real one listed with a one-line blurb in the owner's own terms; new connection requests read.
2. **Match**, by the matchmaker skill: for each newly listed business, and each connection request, look for the pair (same customer, different product, same area). `rc.py match <a> <b> --notes "<why>"`.
3. **Introduce.** For each proposed pair, one introduction to both owners. `python3 repo/guards/scripts/suppression.py check "<business>"` on both first. It is an item file in `requests/justin/` (ITEM, ROLE: referral-connection, ---PAYLOAD---, TO, SUBJECT, TEXT, ---END---), logged with `CAMPAIGN=referral-connection python3 repo/convlog/gate.py drafted <file> --agent referral-connection`. Message type `rc_introduction`.
4. **Follow.** `rc.py matches`: for each `introduced` or `agreed` pair with no movement, one short note asking where they got to (`rc_match_followup`).
5. **Gaps.** A city with listings in one trade and nobody in the trades that pair with it is a line in `requests/growth/gaps-<today>.md`.

## Write

`daily/<today>/desk.md`: counts only (new sign-ups, listed, spam, removals, connection requests, pairs by stage), by area; writes made against writes proposed. No member's name, email or business in this file.
