---
paths:
  - "templates/sitemap.xml"
---

# Sitemap Rules

- Every image referenced in templates needs an `<image:image>` entry
- List an image under the page that actually renders it; Google ignores entries for images the page never shows
- Every YouTube video needs a `<video:video>` entry
- ALL entries need localized titles/captions for both ES and EN
- Priority: 1.0 homepage, 0.8 main sections (banda, media, musica, contacto), 0.5 others
- Use `<changefreq>` based on update frequency: weekly for homepage, monthly for sections
- Image URLs must use the full `https://teina.es/` base URL
- Band member images are under `/banda/`, gallery images under `/media/`

## lastmod

- Emit `<lastmod>` only from real content dates: `updated` on pages, `extra.updated` on sections (Zola sections reject a top-level `updated`)
- Never fall back to `now()`: a build-time date on every page makes Google treat lastmod as noise
- Date-only format (`YYYY-MM-DD`); no hand-written timezone offset
- `scripts/concert.py` stamps `extra.updated` on both `content/conciertos/_index*.md` on every save

## Image tiers

- Gallery images ship in three tiers: `static/media/thumbs/` (grid), `static/media/large/` (lightbox, capped ~1600px), and the untouched original in `static/media/`
- Sitemap gallery entries point at the `large/` WebP, because that is the image the page actually links
- Image titles/captions in the sitemap must match the `alt` text of the same image in `templates/media.html`
