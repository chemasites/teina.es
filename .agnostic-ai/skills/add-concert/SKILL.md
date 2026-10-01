---
name: add-concert
description: Add, change, or remove a Teína concert in data/concerts.toml. Use when given a date, venue, city, time, or ticket link.
user-invocable: true
argument-hint: "<date> <venue> <city> [time] [ticket-url]"
x-claude:
  allowed-tools: Read, Edit, Bash, Grep
---

Update the concert list. Request: $ARGUMENTS

`data/concerts.toml` is the only source. `templates/conciertos.html` renders the visible list and the `MusicEvent` JSON-LD from it, sorts by date, and hides past events from JSON-LD. Never edit that template's list or JSON-LD by hand.

## Steps

1. `python3.12 scripts/concert.py list` to see current entries and IDs.
2. Apply each concert in the request (several may come separated by `;` or "and"):
   - Add: `python3.12 scripts/concert.py add --date YYYY-MM-DD --city "City" [--venue "Venue"] [--time HH:MM] [--ticket URL] [--price EUR] [--region "Región de Murcia"] [--private]`
   - Change: `python3.12 scripts/concert.py update --id N [--time HH:MM] [--ticket URL] [--clear-ticket] [--price EUR] [--venue ...] [--city ...] [--public|--private]`
   - Remove: `python3.12 scripts/concert.py remove --date YYYY-MM-DD` or `--id N`
3. `zola build`. Confirm the new date shows in `public/conciertos/index.html` and `public/en/conciertos/index.html`.
4. Commit as `feat(concerts): ...` and push to `main`.

## Notes

- The script derives `display`, `schema_*`, and the `+01:00`/`+02:00` Spain offset, keeps entries sorted, and stamps `extra.updated` on both concerts sections.
- A private event needs only `--date`, `--city`, `--private`; it shows a Privado/Private badge and no JSON-LD.
- Google drops a ticket `Offer` without a price, so pass `--price` with `--ticket` when the price is known ("0" if free).
- Do not ask for a missing time or ticket link; add what you have and say what is missing.
