# Scripts

Maintenance scripts for the Teína website.

## `concert.py`

Edits `data/concerts.toml`, the single source of truth for concerts.
`templates/conciertos.html` loops over it to render both the visible event list
and the JSON-LD `MusicEvent` schema; `base.html` JS splits past events into a
collapsible section client-side. No AI. Entries are kept in chronological order
and canonical field order automatically. Run `zola build` after any change.

### List all concerts

```bash
python3.12 scripts/concert.py list
```

Prints a table with `ID`, `DATE`, `VENUE`, `TIME/STATUS`, `TICKET`. Use the
`ID` to target a row in `update`.

### Add a concert

```bash
# Public concert with time
python3.12 scripts/concert.py add --date 2026-07-24 --time 22:00 \
  --venue Cuervarrock --city Calasparra

# Public concert with ticket URL
python3.12 scripts/concert.py add --date 2026-03-28 --time 21:30 \
  --venue "Auditorio Murcia Parque" --city Murcia \
  --ticket https://www.vivaticket.com/es/ticket/...

# Private event (no time, shows "Privado" badge)
python3.12 scripts/concert.py add --date 2026-05-10 --city Calasparra --private
```

### Remove a concert

By date:

```bash
python3.12 scripts/concert.py remove --date 2026-06-13
```

Or by ID (see `list`):

```bash
python3.12 scripts/concert.py remove --id 7
```

### Update a concert by ID

Get the ID from `list`, then:

```bash
# Change time
python3.12 scripts/concert.py update --id 8 --time 22:30

# Add or replace ticket URL
python3.12 scripts/concert.py update --id 1 --ticket https://example.com/tkt

# Remove ticket URL
python3.12 scripts/concert.py update --id 1 --clear-ticket

# Change venue or city
python3.12 scripts/concert.py update --id 8 --venue "New Venue" --city Murcia

# Toggle private/public
python3.12 scripts/concert.py update --id 3 --public --time 23:00
python3.12 scripts/concert.py update --id 5 --private
```

After any change run `zola build` to verify.

## `media.py`

Copies and optimizes images from `local/imgs/` into the media gallery:

- Writes the lightbox image to `static/media/large/<name>.jpg` and `.webp`
  (1600px long side, JPEG quality 75).
- Writes the grid thumbnail to `static/media/thumbs/<name>.jpg` and `.webp`
  (600px long side, JPEG quality 70). WebP quality is 80.
- Converts HEIC, PNG and WebP sources to JPEG.
- Sanitizes filenames (lowercase, safe chars).
- Strips EXIF metadata (needs `exiftool`; optional).
- Appends a `<picture>` entry with the thumbnail's `width` and `height` to
  `templates/media.html` (section `#galeria`), with auto-incrementing alt
  text (`Foto Teína N` / `Teína Photo N`) unless `--alt-es`/`--alt-en` is set.

Requires `sips` (macOS built-in), `cwebp` (`brew install webp`) and
Python 3.11+.

### Drop files in `local/imgs/` and import

```bash
# Dry-run first to preview
python3.12 scripts/media.py import --dry-run

# Real import
python3.12 scripts/media.py import

# Custom source dir (positional), sizes and quality
python3.12 scripts/media.py import ~/Pictures/teina \
  --max 1800 --thumb 500 --quality 80 --webp-quality 85

# Custom alt text for this batch
python3.12 scripts/media.py import --alt-es "Concierto Murcia" \
  --alt-en "Murcia Concert"

# Move sources out of local/imgs/ after success
python3.12 scripts/media.py import --move
```

### List gallery entries

```bash
python3.12 scripts/media.py list
```

Prints `ID`, `NAME`, `ALT (ES)`, `ALT (EN)` for every entry in the `#galeria`
section of `templates/media.html`. Use the `ID` to target a row in `remove`.

### Remove a gallery entry

By name (see `list`):

```bash
python3.12 scripts/media.py remove --name 27
```

By ID (see `list`):

```bash
python3.12 scripts/media.py remove --id 30
```

Deletes the `.jpg` and `.webp` files in `static/media/large/` and
`static/media/thumbs/`, and the `<a>` entry in `templates/media.html`. Use
`--keep-files` to only remove the template entry.

After importing or removing, run `scripts/sitemap.py regen` to sync the
sitemap, then `zola build` to verify.

## `sitemap.py`

Regenerates the `/media/` and `/en/media/` image and video blocks in
`templates/sitemap.xml` from the current `templates/media.html`. Other
sections (homepage, banda) are left untouched.

Titles come from the `<img alt>` text in the gallery, captions use a
fixed boilerplate, and video titles come from `<lite-youtube data-title>`.
A video already in the sitemap keeps its description and any tags after
`<video:player_loc>` (duration, publication date); a new video gets a
templated description. Entries follow the gallery order.

```bash
# Preview without writing
python3.12 scripts/sitemap.py regen --dry-run

# Regenerate
python3.12 scripts/sitemap.py regen
```

Run it any time you add or remove media gallery entries.
