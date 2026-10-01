---
name: update-sitemap
description: Audit templates/sitemap.xml against the images and videos each page renders, and fix drift.
user-invocable: true
x-claude:
  allowed-tools: Read, Edit, Write, Bash, Grep, Glob
---

1. `python3.12 scripts/sitemap.py regen` to rebuild the `/media/` and `/en/media/` blocks from `templates/media.html`.
2. For the other pages (`index.html`, `banda.html`, `tributo.html`), list the images each template renders and compare with that page's entries in `templates/sitemap.xml`. Add missing ones with ES and EN text matching the `alt`; remove entries for images the page no longer shows.
3. Check priorities and `changefreq` against the sitemap rules.
4. `zola build` and confirm `public/sitemap.xml` parses as XML (`python3 -c "import xml.dom.minidom,sys;xml.dom.minidom.parse('public/sitemap.xml')"`).

## Entry formats

```xml
<image:image>
  <image:loc>https://teina.es/path/to/image.webp</image:loc>
  <image:title>Título</image:title>
  <image:caption>Descripción</image:caption>
</image:image>
```

```xml
<video:video>
  <video:thumbnail_loc>https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg</video:thumbnail_loc>
  <video:title>Título</video:title>
  <video:description>Descripción</video:description>
  <video:player_loc>https://www.youtube.com/embed/VIDEO_ID</video:player_loc>
</video:video>
```
