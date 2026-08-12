#!/usr/bin/env python3
"""Manage Teína concerts in data/concerts.toml without AI.

Usage:
  concert.py add --date YYYY-MM-DD --city CITY [--venue VENUE] [--time HH:MM]
             [--ticket URL] [--private]
  concert.py remove (--date YYYY-MM-DD | --id N)
  concert.py update --id N [--time HH:MM | --clear-time] [--ticket URL |
             --clear-ticket] [--venue VENUE] [--city CITY] [--private | --public]
  concert.py list

data/concerts.toml is the single source of truth: templates/conciertos.html
loops over it to render both the visible list and the JSON-LD MusicEvent array,
and base.html JS splits past events client-side. This script just edits the TOML;
run `zola build` afterwards to verify.
"""

import argparse
import re
import sys
import tomllib
from datetime import date as date_cls
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOML = ROOT / "data" / "concerts.toml"
CONCIERTOS_PAGES = [ROOT / "content" / "conciertos" / "_index.md",
                    ROOT / "content" / "conciertos" / "_index.en.md"]

HEADER = """# Concerts data — single source for visible list + JSON-LD structured data.
# date: "YYYY-MM-DD" (used for sorting, past/future split, data-date attr)
# display: visible venue label (language-neutral, e.g. "City - Venue")
# time: visible time like "22.00h", or "--:--" if unknown. Omit for private.
# private: true hides time, shows "Privado/Private" badge, skips JSON-LD.
# ticket_url: optional; renders a Tickets button + JSON-LD offer.
# schema_*: only for public events (JSON-LD MusicEvent). schema_start is full
#   ISO 8601 with timezone, or date-only "YYYY-MM-DD" if time unknown.
#
# Managed by scripts/concert.py — keep fields in the canonical order below.
"""

FIELD_ORDER = ["date", "display", "time", "private", "ticket_url",
               "schema_name", "schema_loc", "schema_city", "schema_start"]


def load():
    data = tomllib.loads(TOML.read_text(encoding="utf-8"))
    return data.get("concert", [])


def save(concerts):
    concerts.sort(key=lambda c: c["date"])
    body = "\n\n".join(emit(c) for c in concerts)
    TOML.write_text(HEADER + "\n" + body + "\n", encoding="utf-8")
    stamp_updated()


def stamp_updated():
    """Refresh conciertos `extra.updated` so <lastmod> tracks real edits, not build time."""
    today = date_cls.today().isoformat()
    for page in CONCIERTOS_PAGES:
        text = page.read_text(encoding="utf-8")
        if re.search(r'^updated = "', text, flags=re.MULTILINE):
            text = re.sub(r'^updated = "[^"]*"$', f'updated = "{today}"',
                          text, count=1, flags=re.MULTILINE)
        elif re.search(r"^\[extra\]$", text, flags=re.MULTILINE):
            text = re.sub(r"^\[extra\]$", f'[extra]\nupdated = "{today}"',
                          text, count=1, flags=re.MULTILINE)
        else:
            # Zola sections reject a top-level `updated`, so it has to live under [extra]
            text = re.sub(r"\n\+\+\+", f'\n\n[extra]\nupdated = "{today}"\n+++',
                          text, count=1)
        page.write_text(text, encoding="utf-8")


def emit(c):
    lines = ["[[concert]]"]
    for k in FIELD_ORDER:
        if k not in c:
            continue
        v = c[k]
        if isinstance(v, bool):
            lines.append(f"{k} = {'true' if v else 'false'}")
        else:
            esc = str(v).replace("\\", "\\\\").replace('"', '\\"')
            lines.append(f'{k} = "{esc}"')
    return "\n".join(lines)


def make_start(date, time):
    if not time:
        return date
    mth = int(date.split("-")[1])
    offset = "+02:00" if 3 <= mth <= 10 else "+01:00"  # approx Spain DST
    return f"{date}T{time}:00{offset}"


def fmt_time(time):
    return time.replace(":", ".") + "h" if time else "--:--"


def build(date, city, venue, time, ticket, private):
    same = bool(venue) and venue.lower() == city.lower()
    display = city + (f" - {venue}" if venue and not same else "")
    c = {"date": date, "display": display, "private": bool(private)}
    if private:
        return c
    c["time"] = fmt_time(time)
    if ticket:
        c["ticket_url"] = ticket
    c["schema_name"] = venue if venue and not same else city
    c["schema_loc"] = venue or city
    c["schema_city"] = city
    c["schema_start"] = make_start(date, time)
    return c


def current_city(c):
    return c.get("schema_city") or c["display"].split(" - ", 1)[0]


def current_venue(c):
    loc = c.get("schema_loc", "")
    if loc and loc.lower() != current_city(c).lower():
        return loc
    return c["display"].split(" - ", 1)[1] if " - " in c["display"] else ""


def current_time(c):
    t = c.get("time", "")
    if not t or t == "--:--":
        return None
    return t[:-1].replace(".", ":")  # "22.00h" -> "22:00"


def cmd_add(args):
    validate_date(args.date)
    if args.time:
        validate_time(args.time)
    concerts = load()
    if any(c["date"] == args.date for c in concerts):
        sys.exit(f"error: concert on {args.date} already exists; remove first")
    concerts.append(build(args.date, args.city, args.venue, args.time,
                          args.ticket, args.private))
    save(concerts)
    label = f"{args.venue} - {args.city}" if args.venue else args.city
    print(f"added: {args.date} {label}")


def cmd_remove(args):
    if (args.date is None) == (args.id is None):
        sys.exit("error: pass exactly one of --date or --id")
    concerts = load()
    date = resolve_id(concerts, args.id) if args.id is not None else args.date
    if args.date is not None:
        validate_date(date)
    kept = [c for c in concerts if c["date"] != date]
    if len(kept) == len(concerts):
        sys.exit(f"error: no concert found on {date}")
    save(kept)
    print(f"removed: {date}")


def cmd_update(args):
    concerts = load()
    date = resolve_id(concerts, args.id)
    c = next(c for c in concerts if c["date"] == date)
    city = args.city if args.city is not None else current_city(c)
    venue = args.venue if args.venue is not None else current_venue(c)
    time = current_time(c)
    if args.time is not None:
        validate_time(args.time)
        time = args.time
    if args.clear_time:
        time = None
    ticket = c.get("ticket_url")
    if args.ticket is not None:
        ticket = args.ticket
    if args.clear_ticket:
        ticket = None
    private = c["private"]
    if args.private:
        private = True
    if args.public:
        private = False
    rebuilt = build(date, city, venue, time, ticket, private)
    concerts = [x for x in concerts if x["date"] != date] + [rebuilt]
    save(concerts)
    print(f"updated id={args.id} date={date}")


def cmd_list(_args):
    concerts = sorted(load(), key=lambda c: c["date"])
    rows = []
    for idx, c in enumerate(concerts, start=1):
        status = "PRIVATE" if c["private"] else c.get("time", "")
        rows.append((str(idx), c["date"], c["display"], status,
                     c.get("ticket_url", "")))
    headers = ("ID", "DATE", "VENUE", "TIME/STATUS", "TICKET")
    widths = [max(len(h), max((len(r[i]) for r in rows), default=0))
              for i, h in enumerate(headers)]
    fmt = "  ".join("{:<" + str(w) + "}" for w in widths)
    print(fmt.format(*headers))
    print("  ".join("-" * w for w in widths))
    for r in rows:
        print(fmt.format(*r))


def resolve_id(concerts, idx):
    ordered = sorted(c["date"] for c in concerts)
    if idx < 1 or idx > len(ordered):
        sys.exit(f"error: invalid id {idx}; valid 1..{len(ordered)}")
    return ordered[idx - 1]


def validate_date(s):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", s):
        sys.exit(f"error: date must be YYYY-MM-DD, got {s!r}")


def validate_time(s):
    if not re.fullmatch(r"\d{2}:\d{2}", s):
        sys.exit(f"error: time must be HH:MM, got {s!r}")


def main():
    p = argparse.ArgumentParser(
        description="Manage Teína conciertos in data/concerts.toml")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add", help="add a concert")
    a.add_argument("--date", required=True, help="YYYY-MM-DD")
    a.add_argument("--city", required=True)
    a.add_argument("--venue", default="", help="venue name (optional)")
    a.add_argument("--time", help="HH:MM (optional)")
    a.add_argument("--ticket", help="ticket URL (optional)")
    a.add_argument("--private", action="store_true",
                   help="mark as private event (no time, Privado badge)")
    a.set_defaults(func=cmd_add)

    r = sub.add_parser("remove", help="remove concert by date or ID")
    r.add_argument("--date", help="YYYY-MM-DD")
    r.add_argument("--id", type=int, help="ID from `list`")
    r.set_defaults(func=cmd_remove)

    u = sub.add_parser("update", help="update concert by ID (see `list`)")
    u.add_argument("--id", type=int, required=True)
    u.add_argument("--time", help="set time HH:MM")
    u.add_argument("--clear-time", action="store_true",
                   help="clear time (display --:--)")
    u.add_argument("--ticket", help="set ticket URL")
    u.add_argument("--clear-ticket", action="store_true", help="remove ticket")
    u.add_argument("--venue", help="set venue name")
    u.add_argument("--city", help="set city")
    u.add_argument("--private", action="store_true", help="mark as private")
    u.add_argument("--public", action="store_true", help="unmark private")
    u.set_defaults(func=cmd_update)

    l = sub.add_parser("list", help="list all concerts")
    l.set_defaults(func=cmd_list)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
