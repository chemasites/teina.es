# Scripts

Maintenance scripts for the Teína website.

## `concert.py`

Edits the concerts section in `templates/index.html` — both the visible event
list and the JSON-LD `MusicEvent` schema. No AI, pure regex. Chronological
order kept automatically.

### List all concerts

```bash
python3 scripts/concert.py list
```

Prints a table with `ID`, `DATE`, `VENUE`, `TIME/STATUS`, `TICKET`. Use the
`ID` to target a row in `update`.

### Add a concert

```bash
# Public concert with time
python3 scripts/concert.py add --date 2026-07-24 --time 22:00 \
  --venue Cuervarrock --city Calasparra

# Public concert with ticket URL
python3 scripts/concert.py add --date 2026-03-28 --time 21:30 \
  --venue "Auditorio Murcia Parque" --city Murcia \
  --ticket https://www.vivaticket.com/es/ticket/...

# Private event (no time, shows "Privado" badge)
python3 scripts/concert.py add --date 2026-05-10 --city Calasparra --private
```

### Remove a concert

By date:

```bash
python3 scripts/concert.py remove --date 2026-06-13
```

Or by ID (see `list`):

```bash
python3 scripts/concert.py remove --id 7
```

### Update a concert by ID

Get the ID from `list`, then:

```bash
# Change time
python3 scripts/concert.py update --id 8 --time 22:30

# Add or replace ticket URL
python3 scripts/concert.py update --id 1 --ticket https://example.com/tkt

# Remove ticket URL
python3 scripts/concert.py update --id 1 --clear-ticket

# Change venue or city
python3 scripts/concert.py update --id 8 --venue "New Venue" --city Murcia

# Toggle private/public
python3 scripts/concert.py update --id 3 --public --time 23:00
python3 scripts/concert.py update --id 5 --private
```

After any change run `zola build` to verify.

## `media.py`

Copies and optimizes images from `local/imgs/` into the media gallery:

- Resizes full image to a max width (default 2048px, quality 75).
- Generates a JPEG thumbnail (default 600px, quality 70) in
  `static/media/thumbs/` (matches existing gallery sizes).
- Converts HEIC/WebP/JPEG to `.jpg`; keeps `.png` as-is.
- Sanitizes filenames (lowercase, safe chars).
- Strips EXIF metadata (needs `exiftool`; optional).
- Appends a gallery entry in `templates/media.html` (section `#galeria`)
  with auto-incrementing alt text (`Foto Teína N` / `Teína Photo N`).

Requires `sips` (macOS built-in).

### Drop files in `local/imgs/` and import

```bash
# Dry-run first to preview
python3 scripts/media.py import --dry-run

# Real import
python3 scripts/media.py import

# Custom source dir (positional), sizes and quality
python3 scripts/media.py import ~/Pictures/teina \
  --max 1800 --thumb 500 --quality 80 --thumb-quality 75

# Custom alt text for this batch
python3 scripts/media.py import --alt-es "Concierto Murcia" \
  --alt-en "Murcia Concert"

# Move sources out of local/imgs/ after success
python3 scripts/media.py import --move
```

After importing, run `zola build` and consider updating
`templates/sitemap.xml` if the images should appear in the sitemap.
