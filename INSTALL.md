# Install

One line, pasted into a bot Justin already runs:

> Add the Referral Connection site agent. Download https://github.com/jbellsolutions/referral-connection-grokbot/releases/latest/download/referral-connection.zip, unpack it into /workspace/referral-connection/repo/, run python3 /workspace/referral-connection/repo/tools/install.py and do what it prints, in order. Ask me nothing until it is all done, then send me one message that ends with the checklist. Nothing sends, posts, spends or writes to a CRM or a site until I say yes.

That is the whole install for Justin. The same line works in a new bot of its own, if he would rather the site had its own bot. The rest of this page is what the bot does.

## It is an add-on

Everything it makes is inside `/workspace/referral-connection/`: its own files, switches, opt-out list, log and secrets. It reads and changes nothing in the bot's other workspace. In the bot itself it adds three things and replaces none: one section of memory, one skill (`referral-site-cli`) and four routines whose names start "Referral".

## What the bot does

1. **Unpack and run the installer.** It makes the workspace, the switch files and the setup page, runs the checks and prints the next steps. It asks nothing and can be run again.
2. **Set the agent up.** `python3 /workspace/referral-connection/repo/tools/team.py setup` prints four things: the memory section to add, the skill to save, the four routines to create, and one command to run.
3. **Check the two CLIs** with `python3 /workspace/referral-connection/repo/tools/job.py status`, installing them if they are not there.
4. **Send Justin one message**: what is set up, what `job.py status` said, any failed check, then the whole checklist from `/workspace/referral-connection/requests/justin/CHECKLIST.md`, starting `NEEDS-JUSTIN:`. Then stop.

## The rule this agent is built on

The bot orchestrates. Every referral site task is handed to the Claude Code CLI with `tools/job.py`; the Codex CLI is the second engine. `job.py audit` counts each day's jobs by engine, and the nightly report prints the count. The whole rule is in [skills/claude-code-cli/SKILL.md](skills/claude-code-cli/SKILL.md).

## What can go wrong, and what to do

| If | Then |
|---|---|
| The download fails | Ask Justin once to attach `referral-connection.zip` from the release, then carry on from step 1 |
| The bot's memory has no room for the section | Save the section as a note the four routines' prompts point to, and say so in the one message |
| A CLI is not installed or not answering | Carry on. Each job then falls to the bot itself and is recorded as such, until Justin signs the CLI in |
| A check fails | Carry on, and put the failed line in the one message |
| The site's earlier pack (several referral agents) is installed on any bot | Say so in the one message. Two writers must not write the same site records: one is switched off first |

## What is on after the install

Every routine runs on **test**: its job runs and makes drafts. Nothing reaches a person or the site, and nothing is spent, until Justin turns that switch on. The switches are four small files in `/workspace/referral-connection/context/`. He changes one by saying it in the bot's chat.

## One line for Auto-review

If the bot's Auto-review rules do not already cover it, Justin adds:

- Ask first before creating, updating or deleting a record in the referral site's admin API, or publishing a page there.
