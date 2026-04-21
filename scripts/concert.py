#!/usr/bin/env python3
"""Update Teina concerts in templates/index.html without AI.

Usage:
  concert.py add --date YYYY-MM-DD --city CITY [--venue VENUE] [--time HH:MM]
             [--ticket URL] [--private]
  concert.py remove --date YYYY-MM-DD
  concert.py list

Matches existing event on date. `add` inserts into both the JSON-LD MusicEvent
array and the visible <ul class="event-list">, keeping chronological order.
`remove` deletes both. `list` prints all scheduled dates.
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "templates" / "index.html"

MONTH_ES = {1: "Ene", 2: "Feb", 3: "Mar", 4: "Abr", 5: "May", 6: "Jun",
            7: "Jul", 8: "Ago", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dic"}
MONTH_EN = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
            7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}

ARRAY_RE = re.compile(
    r'(<script type="application/ld\+json">\n\[\n)(.*?)(\n\]\n</script>)',
    re.DOTALL,
)
SCHEMA_EVENT_RE = re.compile(
    r'    \{\n        "@context": "https://schema\.org",\n'
    r'        "@type": "MusicEvent",.*?\n    \}',
    re.DOTALL,
)
SCHEMA_DATE_RE = re.compile(r'"startDate": "(\d{4}-\d{2}-\d{2})')

UL_RE = re.compile(
    r'(<ul class="event-list">\n)(.*?)(\n        </ul>)',
    re.DOTALL,
)
LI_RE = re.compile(
    r'            <li class="event-item[^"]*" data-date="(\d{4}-\d{2}-\d{2})">'
    r'.*?</li>',
    re.DOTALL,
)


def load():
    return HTML.read_text(encoding="utf-8")


def save(text):
    HTML.write_text(text, encoding="utf-8")


def parse_schema(html):
    m = ARRAY_RE.search(html)
    if not m:
        sys.exit("error: JSON-LD MusicEvent array not found")
    items = []
    for block in SCHEMA_EVENT_RE.findall(m.group(2)):
        dm = SCHEMA_DATE_RE.search(block)
        items.append((dm.group(1) if dm else "", block))
    return m, items


def write_schema(html, m, items):
    items.sort(key=lambda x: x[0])
    body = ",\n".join(b for _, b in items)
    return html[:m.start()] + m.group(1) + body + m.group(3) + html[m.end():]


def parse_lis(html):
    m = UL_RE.search(html)
    if not m:
        sys.exit("error: <ul class=\"event-list\"> not found")
    return m, [(lm.group(1), lm.group(0)) for lm in LI_RE.finditer(m.group(2))]


def write_lis(html, m, items):
    items.sort(key=lambda x: x[0])
    body = "\n".join(b for _, b in items)
    return html[:m.start()] + m.group(1) + body + m.group(3) + html[m.end():]


def build_schema_block(date, time, venue, city, ticket):
    if time:
        mth = int(date.split("-")[1])
        offset = "+02:00" if 3 <= mth <= 10 else "+01:00"
        start = f"{date}T{time}:00{offset}"
    else:
        start = date
    loc_name = venue or city
    same = venue and venue.lower() == city.lower()
    name_suffix = f"{venue} ({city})" if venue and not same else (venue or city)
    lines = [
        "    {",
        '        "@context": "https://schema.org",',
        '        "@type": "MusicEvent",',
        f"        \"name\": \"Teína {{% if lang == 'en' %}}at{{% else %}}en{{% endif %}} {name_suffix}\",",
        f'        "startDate": "{start}",',
        f'        "location": {{ "@type": "Place", "name": "{loc_name}", '
        f'"address": {{ "@type": "PostalAddress", "addressLocality": "{city}", '
        f'"addressCountry": "ES" }} }},',
        '        "performer": { "@type": "MusicGroup", "name": "Teína" },',
    ]
    if ticket:
        lines.append(
            f'        "offers": {{ "@type": "Offer", "url": "{ticket}", '
            f'"availability": "https://schema.org/InStock" }},'
        )
    lines += [
        '        "eventStatus": "https://schema.org/EventScheduled",',
        '        "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode"',
        "    }",
    ]
    return "\n".join(lines)


def build_li_block(date, time, venue, city, ticket, private):
    _, m, d = map(int, date.split("-"))
    klass = "event-item event-private" if private else "event-item"
    same = venue and venue.lower() == city.lower()
    venue_txt = city + (f" - {venue}" if venue and not same else "")
    parts = [
        f'            <li class="{klass}" data-date="{date}">',
        f'                <span class="event-date">{d} '
        f'{{% if lang == "en" %}}{MONTH_EN[m]}'
        f'{{% else %}}{MONTH_ES[m]}{{% endif %}}</span>',
        f'                <span class="event-venue">{venue_txt}</span>',
    ]
    if ticket and not private:
        parts.append(
            '                <span class="event-actions">\n'
            f'                    <a href="{ticket}" target="_blank" '
            'rel="noopener noreferrer" class="event-btn event-btn-tickets">\n'
            '                        <svg width="16" height="16" viewBox="0 0 24 24" '
            'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
            'stroke-linejoin="round"><path d="M2 9a3 3 0 010-6h20a3 3 0 010 6"/>'
            '<path d="M2 15a3 3 0 000 6h20a3 3 0 000-6"/>'
            '<line x1="2" y1="9" x2="2" y2="15"/><line x1="22" y1="9" x2="22" y2="15"/>'
            '<line x1="9" y1="3" x2="9" y2="21"/></svg>\n'
            '                        <span>{% if lang == "en" %}Tickets'
            '{% else %}Entradas{% endif %}</span>\n'
            '                    </a>\n'
            '                </span>'
        )
    else:
        parts.append('                <span class="event-actions"></span>')
    if private:
        parts.append(
            '                <span class="event-badge">'
            '{% if lang == "en" %}Private{% else %}Privado{% endif %}</span>'
        )
    else:
        t = time.replace(":", ".") + "h" if time else "--:--"
        parts.append(f'                <span class="event-time">{t}</span>')
    parts.append('            </li>')
    return "\n".join(parts)


def cmd_add(args):
    validate_date(args.date)
    if args.time:
        validate_time(args.time)
    html = load()
    m_s, items = parse_schema(html)
    if any(d == args.date for d, _ in items):
        sys.exit(f"error: concert on {args.date} already exists; remove first")
    items.append((args.date, build_schema_block(
        args.date, args.time, args.venue, args.city, args.ticket)))
    html = write_schema(html, m_s, items)
    m_l, lis = parse_lis(html)
    lis.append((args.date, build_li_block(
        args.date, args.time, args.venue, args.city, args.ticket, args.private)))
    html = write_lis(html, m_l, lis)
    save(html)
    label = f"{args.venue} - {args.city}" if args.venue else args.city
    print(f"added: {args.date} {label}")


def cmd_remove(args):
    if (args.date is None) == (args.id is None):
        sys.exit("error: pass exactly one of --date or --id")
    html = load()
    m_s, items = parse_schema(html)
    m_l, lis = parse_lis(html)
    if args.id is not None:
        ordered = sorted(set(d for d, _ in items) | set(d for d, _ in lis))
        if args.id < 1 or args.id > len(ordered):
            sys.exit(f"error: invalid id {args.id}; valid 1..{len(ordered)}")
        date = ordered[args.id - 1]
    else:
        validate_date(args.date)
        date = args.date
    kept_schema = [x for x in items if x[0] != date]
    removed_schema = len(items) - len(kept_schema)
    html = write_schema(html, m_s, kept_schema)
    m_l, lis = parse_lis(html)
    kept_lis = [x for x in lis if x[0] != date]
    removed_lis = len(lis) - len(kept_lis)
    if removed_schema == 0 and removed_lis == 0:
        sys.exit(f"error: no concert found on {date}")
    html = write_lis(html, m_l, kept_lis)
    save(html)
    print(f"removed: {date} (schema={removed_schema}, li={removed_lis})")


def cmd_list(_args):
    html = load()
    _, lis = parse_lis(html)
    rows = []
    for idx, (d, block) in enumerate(sorted(lis), start=1):
        vm = re.search(r'<span class="event-venue">([^<]*)</span>', block)
        venue = vm.group(1) if vm else ""
        if 'event-private' in block:
            status = "PRIVATE"
        else:
            tm = re.search(r'<span class="event-time">([^<]*)</span>', block)
            status = tm.group(1) if tm else ""
        am = re.search(r'<a href="([^"]+)"[^>]*class="event-btn event-btn-tickets"', block)
        ticket = am.group(1) if am else ""
        rows.append((str(idx), d, venue, status, ticket))

    headers = ("ID", "DATE", "VENUE", "TIME/STATUS", "TICKET")
    widths = [max(len(h), max((len(r[i]) for r in rows), default=0))
              for i, h in enumerate(headers)]
    fmt = "  ".join("{:<" + str(w) + "}" for w in widths)
    print(fmt.format(*headers))
    print("  ".join("-" * w for w in widths))
    for r in rows:
        print(fmt.format(*r))


def parse_event(schema_block, li_block):
    sm = re.search(
        r'"startDate": "(\d{4}-\d{2}-\d{2})(?:T(\d{2}):(\d{2}))?', schema_block)
    date = sm.group(1) if sm else ""
    time = f"{sm.group(2)}:{sm.group(3)}" if sm and sm.group(2) else None
    cm = re.search(r'"addressLocality": "([^"]+)"', schema_block)
    city = cm.group(1) if cm else ""
    vm = re.search(
        r'"location": \{ "@type": "Place", "name": "([^"]+)"', schema_block)
    loc_name = vm.group(1) if vm else ""
    venue = loc_name if loc_name and loc_name.lower() != city.lower() else ""
    om = re.search(
        r'"offers": \{ "@type": "Offer", "url": "([^"]+)"', schema_block)
    ticket = om.group(1) if om else None
    private = 'event-private' in li_block
    return {"date": date, "time": time, "venue": venue, "city": city,
            "ticket": ticket, "private": private}


def cmd_update(args):
    html = load()
    m_s, items = parse_schema(html)
    m_l, lis = parse_lis(html)
    ordered = sorted(set(d for d, _ in items) | set(d for d, _ in lis))
    if args.id < 1 or args.id > len(ordered):
        sys.exit(f"error: invalid id {args.id}; valid 1..{len(ordered)}")
    date = ordered[args.id - 1]
    schema_block = next((b for d, b in items if d == date), "")
    li_block = next((b for d, b in lis if d == date), "")
    cur = parse_event(schema_block, li_block)

    if args.time is not None:
        validate_time(args.time)
        cur["time"] = args.time
    if args.clear_time:
        cur["time"] = None
    if args.ticket is not None:
        cur["ticket"] = args.ticket
    if args.clear_ticket:
        cur["ticket"] = None
    if args.venue is not None:
        cur["venue"] = args.venue
    if args.city is not None:
        cur["city"] = args.city
    if args.private:
        cur["private"] = True
    if args.public:
        cur["private"] = False

    kept_schema = [(d, b) for d, b in items if d != date]
    kept_schema.append((date, build_schema_block(
        date, cur["time"], cur["venue"], cur["city"], cur["ticket"])))
    html = write_schema(html, m_s, kept_schema)

    m_l, lis = parse_lis(html)
    kept_lis = [(d, b) for d, b in lis if d != date]
    kept_lis.append((date, build_li_block(
        date, cur["time"], cur["venue"], cur["city"],
        cur["ticket"], cur["private"])))
    html = write_lis(html, m_l, kept_lis)
    save(html)
    print(f"updated id={args.id} date={date}")


def validate_date(s):
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', s):
        sys.exit(f"error: date must be YYYY-MM-DD, got {s!r}")


def validate_time(s):
    if not re.fullmatch(r'\d{2}:\d{2}', s):
        sys.exit(f"error: time must be HH:MM, got {s!r}")


def main():
    p = argparse.ArgumentParser(
        description="Update Teína conciertos in templates/index.html")
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
    u.add_argument("--clear-ticket", action="store_true",
                   help="remove ticket")
    u.add_argument("--venue", help="set venue name")
    u.add_argument("--city", help="set city")
    u.add_argument("--private", action="store_true",
                   help="mark as private")
    u.add_argument("--public", action="store_true",
                   help="unmark private")
    u.set_defaults(func=cmd_update)

    l = sub.add_parser("list", help="list all concerts")
    l.set_defaults(func=cmd_list)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
