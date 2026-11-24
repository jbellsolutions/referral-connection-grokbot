#!/usr/bin/env python3
"""Operator CLI for the site's admin API. Standard library only.

Needs RC_SITE (e.g. https://findreferralpartners.com) and RC_ADMIN_KEY, from the environment or from
.secrets/site.env in the agent's workspace (KEY=value lines).

Reads are free. A write goes to the site only when context/owners.md says `referral-site: bot` and
context/routines-on.md says `crm-writes: on` (and there is no context/STOP). `remove` also needs `removals: apply`,
and `page-put --publish` also needs `rc_guide: auto` in context/standing-approvals.md. Otherwise the write is not
made: the exact command is added to requests/justin/site-proposals-<date>.md and PROPOSED is printed.

  rc.py stats
  rc.py signups [--status new] [--area austin] [--since 2026-11-18T00:00:00Z] [--csv FILE]
  rc.py signup-set <id> [--status new|listed|matched|spam|paused] [--notes TEXT]
  rc.py list <signup id> [--blurb "One line about the business"]
  rc.py listings | listing-set <id> [--blurb T] [--wants T] | unlist <listing id>
  rc.py connections | connection-set <id> --status new|introduced|declined|spam
  rc.py removals | remove <email>
  rc.py matches | match <signup a> <signup b> [--notes T] | match-set <id> [--status S] [--notes T]
  rc.py pages | page-get <slug> | page-put <slug> --title T --description D --html FILE [--publish] | page-delete <slug>
"""
import argparse, datetime, json, os, re, subprocess, sys, urllib.error, urllib.parse, urllib.request


REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WS = os.environ.get("BOT_HOME") or (os.path.dirname(REPO) if os.path.basename(REPO) == "repo" else REPO)


def _line(name, key):
    f = os.path.join(WS, "context", name)
    for l in open(f, errors="ignore").read().splitlines() if os.path.exists(f) else []:
        if re.match(rf"\s*{re.escape(key)}\s*:", l, re.I):
            return l.split(":", 1)[1].strip().lower()
    return ""


def held(method, path, body):
    """Why this write may not be made, or "" if it may."""
    if os.path.exists(os.path.join(WS, "context", "STOP")):
        return "context/STOP exists"
    r = subprocess.run([sys.executable, os.path.join(REPO, "guards", "scripts", "owner_guard.py"), "check", "referral-site"],
                       capture_output=True, text=True, env=dict(os.environ, BOT_HOME=WS))
    if r.returncode != 0:
        return "owner guard says " + (r.stdout.strip().splitlines() or ["?"])[-1]
    if _line("routines-on.md", "crm-writes") != "on":
        return "crm-writes is not on"
    if path == "/remove" and _line("routines-on.md", "removals") != "apply":
        return "removals are queued for Justin"
    if path.startswith("/pages/") and method == "PUT" and (body or {}).get("published") and "auto" not in _line("standing-approvals.md", "rc_guide"):
        return "rc_guide is not auto, so a guide is saved as a draft only: run it again without --publish"
    return ""


def propose(why):
    d = os.path.join(WS, "requests", "justin")
    os.makedirs(d, exist_ok=True)
    f = os.path.join(d, f"site-proposals-{datetime.datetime.now(datetime.timezone.utc):%Y-%m-%d}.md")
    new = not os.path.exists(f)
    with open(f, "a") as h:
        if new:
            h.write("# Site writes the agent would have made\n\nNot written, because a switch is off. Each line is the exact command.\n\n")
        h.write("- `python3 repo/tools/rc.py " + " ".join(a if re.fullmatch(r"[\w@.:/,+-]+", a) else json.dumps(a) for a in sys.argv[1:]) + f"`  ({why})\n")
    print(f"PROPOSED, not written ({why}): {f}")
    sys.exit(0)


def call(method, path, body=None, raw=False):
    if method != "GET":
        why = held(method, path, body)
        if why:
            propose(why)
    here = os.path.dirname(os.path.abspath(__file__))
    for f in (os.path.join(os.getcwd(), ".secrets", "site.env"), os.path.join(here, "..", "..", ".secrets", "site.env"), os.path.join(here, "..", ".env.local")):
        if os.path.exists(f):  # KEY=value lines; the environment wins
            for line in open(f):
                k, _, v = line.strip().partition("=")
                if k in ("RC_SITE", "RC_ADMIN_KEY") and v and k not in os.environ:
                    os.environ[k] = v.strip().strip('"')
    site, key = os.environ.get("RC_SITE", "").rstrip("/"), os.environ.get("RC_ADMIN_KEY", "")
    if not site or not key:
        sys.exit("Set RC_SITE and RC_ADMIN_KEY (environment, or .secrets/site.env in the workspace).")
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(site + "/admin" + path, data=data, method=method,
                                 headers={"authorization": "Bearer " + key, "content-type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            t = r.read().decode()
            return t if raw else json.loads(t)
    except urllib.error.HTTPError as e:
        sys.exit(f"{method} {path} -> {e.code}: {e.read().decode()[:400]}")


def show(x):
    print(json.dumps(x, indent=1))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd"); ap.add_argument("args", nargs="*")
    for f in ("status", "area", "since", "csv", "notes", "blurb", "wants", "title", "description", "html"):
        ap.add_argument("--" + f)
    ap.add_argument("--publish", action="store_true")
    a = ap.parse_args(); c, x = a.cmd, a.args
    pick = lambda *ks: {k: getattr(a, k) for k in ks if getattr(a, k) is not None}
    if c == "stats": show(call("GET", "/stats"))
    elif c == "signups":
        qs = urllib.parse.urlencode({**pick("status", "area", "since"), **({"format": "csv"} if a.csv else {})})
        if a.csv:
            open(a.csv, "w").write(call("GET", "/signups?" + qs, raw=True)); print("wrote", a.csv)
        else: show(call("GET", "/signups?" + qs))
    elif c == "signup-set": show(call("PATCH", f"/signups/{x[0]}", pick("status", "notes")))
    elif c == "list": show(call("POST", "/listings", {"signup_id": int(x[0]), **pick("blurb")}))
    elif c == "listings": show(call("GET", "/listings"))
    elif c == "listing-set": show(call("PATCH", f"/listings/{x[0]}", pick("blurb", "wants")))
    elif c == "unlist": show(call("DELETE", f"/listings/{x[0]}"))
    elif c == "connections": show(call("GET", "/connections"))
    elif c == "connection-set": show(call("PATCH", f"/connections/{x[0]}", pick("status")))
    elif c == "removals": show(call("GET", "/removals"))
    elif c == "remove": show(call("POST", "/remove", {"email": x[0]}))
    elif c == "matches": show(call("GET", "/matches"))
    elif c == "match": show(call("POST", "/matches", {"a_signup": int(x[0]), "b_signup": int(x[1]), **pick("notes")}))
    elif c == "match-set": show(call("PATCH", f"/matches/{x[0]}", pick("status", "notes")))
    elif c == "pages": show(call("GET", "/pages"))
    elif c == "page-get": show(call("GET", f"/pages/{x[0]}"))
    elif c == "page-put":
        show(call("PUT", f"/pages/{x[0]}", {"title": a.title, "description": a.description, "body_html": open(a.html).read(), "published": a.publish}))
    elif c == "page-delete": show(call("DELETE", f"/pages/{x[0]}"))
    else: sys.exit("Unknown command. Run with -h.")


if __name__ == "__main__":
    main()
