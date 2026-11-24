# Job: referral-report

The nightly report, and tomorrow's focus. The bot posts the file you write, as it is, to Slack and Notion.

## Run and read

- `python3 repo/tools/rc.py stats` (if the key is not set, every site number is "?").
- `python3 repo/tools/job.py audit --days 1`: how many jobs each engine carried today.
- `python3 repo/guards/scripts/beat.py status`.
- `CAMPAIGN=referral-connection python3 repo/convlog/gate.py day`.
- Today's `daily/<today>/*.md`; `requests/justin/` (oldest first); `repo/campaigns/referral-connection/LAUNCH.md` (the next open step).

## Write `daily/<today>/report.md`, under 200 words

```
Referral Connection, <date>
Site: N sign-ups (N new), N listings, N areas with a listing. Pairs: N proposed, N introduced, N agreed, N paid.
Growth: N prospects, N outreach drafts, N asks answered in draft. Guides: N draft, N live. Site check: ok or the fault.
Engines: Claude Code N jobs, Codex N, the bot itself N (why).
Waiting on you: <the three oldest items, one line each, with the file>
Tomorrow: <the next open step of LAUNCH.md, and the weakest number>
```

Counts only. No member's name, email or business.

## Also write

- `vault/Daily/<today>.md`: the report. `vault/status.md`: one scrubbed status line for the single brain, replacing the last.
- On Mondays, `vault/Decisions.md`: the week's one decision with the number behind it (which source brought sign-ups that became listed and matched).
