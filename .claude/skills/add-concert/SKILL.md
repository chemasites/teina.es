---
name: add-concert
description: Add a new concert/event to the Teína website concerts page
user-invocable: true
argument-hint: "<date> <venue> <city> [ticket-url]"
allowed-tools: Read, Edit, Bash, Grep
---

Add a new concert event to the website. Arguments: $ARGUMENTS

Concerts are **data-driven**: the single source is `data/concerts.toml`. The template
`templates/conciertos.html` loops over it to render BOTH the visible list and the
JSON-LD structured data, and auto-splits upcoming vs past by today's date. You only
edit the TOML — never hand-edit the HTML/JSON-LD.

## Steps

1. Read `data/concerts.toml` to see the existing entries and field conventions
2. Parse the arguments: date, venue name, city, optional time, optional ticket URL.
   Multiple concerts may be given (separated by `;` or `and`) — add each as its own `[[concert]]`.
3. Append a new `[[concert]]` block. Order does NOT matter — the template sorts by `date`.
4. Run `zola build` to verify the site compiles and JSON-LD stays valid.

## `[[concert]]` fields

| field | required | notes |
|-------|----------|-------|
| `date` | yes | `"YYYY-MM-DD"`. Drives sorting, past/future split, `data-date` attr. |
| `display` | yes | Visible label, language-neutral. Convention: `"City - Venue"` (e.g. `"Murcia - La Puerta Falsa"`); use just the place if there's no separate venue. |
| `private` | yes | `true` → shows "Privado/Private" badge, no time, NO JSON-LD. `false` → public. |
| `time` | public only | Visible time like `"22.00h"`, or `"--:--"` if unknown. Omit for private. |
| `ticket_url` | optional | Adds a Tickets button + JSON-LD `offers`. |
| `schema_name` | public only | Place shown in JSON-LD event name: `Teína en <schema_name>`. |
| `schema_loc` | public only | JSON-LD `location.name` (venue/street). |
| `schema_city` | public only | JSON-LD `addressLocality`. |
| `schema_start` | public only | Full ISO 8601 with timezone, e.g. `"2026-08-28T00:00:00+02:00"`. Use date-only `"2026-08-24"` if time unknown. Spain TZ: `+02:00` summer (CEST, ~late Mar–late Oct), `+01:00` winter (CET). |

For a **private** event, only `date`, `display`, `private = true` are needed.

## Example — public event

```toml
[[concert]]
date = "2026-08-28"
display = "Calasparra - Gran Vía 31"
time = "00.00h"
private = false
ticket_url = ""
schema_name = "Calasparra"
schema_loc = "Gran Vía 31"
schema_city = "Calasparra"
schema_start = "2026-08-28T00:00:00+02:00"
```

(omit `ticket_url` line entirely if there's no ticket link)

## Example — private event

```toml
[[concert]]
date = "2026-09-26"
display = "Hotel Nelva"
private = true
```

## Notes
- The template renders one flat sorted `<li>` list; `base.html` JS moves past events
  (date < today) into a collapsible "Ver todos los conciertos pasados" section and adds
  the year + a HOY/TODAY badge client-side. Do not add a second past section in the template.
- Public past events are auto-excluded from JSON-LD (server-side date filter) — no manual cleanup.
- Never edit the `<li>` list or `<script type="application/ld+json">` in the template;
  they are generated from the TOML.
