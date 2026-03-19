---
name: update-sitemap
description: Regenerate or update the sitemap with current images, videos, and pages
user-invocable: true
allowed-tools: Read, Edit, Write, Bash, Grep, Glob
---

Audit and update `templates/sitemap.xml` to match current site content.

## Steps

1. Scan `templates/index.html`, `templates/banda.html`, `templates/media.html`, `templates/musica.html` for all referenced images and videos
2. Scan `static/banda/`, `static/media/`, `static/conciertos/`, `static/imgs/` for all image files
3. Read current `templates/sitemap.xml`
4. Cross-reference: find images/videos in templates that are missing from sitemap
5. Add missing entries with localized titles/captions (ES and EN)
6. Remove entries for images/videos that no longer exist
7. Verify priority tiers: 1.0 homepage, 0.8 main sections, 0.5 secondary
8. Run `zola build` to verify

## Entry formats

```xml
<image:image>
  <image:loc>https://teina.es/path/to/image.webp</image:loc>
  <image:title>Título en español</image:title>
  <image:caption>Descripción en español</image:caption>
</image:image>
```

```xml
<video:video>
  <video:thumbnail_loc>https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg</video:thumbnail_loc>
  <video:title>Título del vídeo</video:title>
  <video:description>Descripción del vídeo</video:description>
  <video:player_loc>https://www.youtube.com/embed/VIDEO_ID</video:player_loc>
</video:video>
```
