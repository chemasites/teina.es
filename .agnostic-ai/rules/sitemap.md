---
paths:
  - "templates/sitemap.xml"
---

# Sitemap rules

- List each image under the page that renders it, with full `https://teina.es/` URLs. Google ignores images the page never shows.
- Every image needs `<image:image>` and every YouTube video `<video:video>`, each with ES text on the Spanish URL and EN text on the `/en/` URL.
- Image titles must match the `alt` text of the same image in the template.
- Gallery entries point at the `static/media/large/` WebP, the file the lightbox opens. Never hand-edit the `/media/` blocks: run `python3.12 scripts/sitemap.py regen`.
- Priority: 1.0 home, 0.9 conciertos and tributo, 0.8 banda, musica, media, 0.7 contacto, 0.5 the rest. `changefreq` is weekly for home and conciertos, monthly otherwise.

## lastmod

- Emit `<lastmod>` only from real content dates: `updated` on pages, `extra.updated` on sections.
- Never fall back to `now()`: a build date on every page teaches Google to ignore lastmod.
- Date only (`YYYY-MM-DD`), no hand-written timezone.
- `scripts/concert.py` stamps `extra.updated` on both `content/conciertos/_index*.md` on every save.
