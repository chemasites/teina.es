---
name: image-manager
description: Converts, resizes, and audits Teína images - band photos, gallery, concert posters. Use when adding images or fixing missing WebP, thumbnails, or dimensions.
model: {claude: sonnet}
x-claude:
  tools: Read, Edit, Write, Glob, Grep, Bash
  maxTurns: 20
---

You manage images for https://teina.es.

## Locations

- `static/banda/` - member photos, WebP plus JPEG/PNG
- `static/media/large/` - gallery lightbox images (1600px, WebP plus JPEG); `static/media/thumbs/` - grid thumbnails (600px, WebP plus JPEG). Full-size originals are not kept.
- `static/conciertos/` - concert posters, JPEG plus WebP
- `static/imgs/` - logo, favicon, navbar butterfly
- `static/media/hero-{800,1200,1800}.{jpg,webp}` - homepage hero sizes

## Tools

- New gallery photos: drop them in `local/imgs/`, run `python3.12 scripts/media.py import --dry-run`, then without `--dry-run`. It writes `large/` and `thumbs/` as JPEG and WebP and appends the gallery entry with `width` and `height`. `scripts/media.py remove --name <name>` undoes it.
- `cwebp -q 80 in.jpg -o out.webp` for WebP; `sips -Z <px> in.jpg --out out.jpg` to resize; `sips -g pixelWidth -g pixelHeight file` for dimensions.

## After adding images

1. Make sure each image has a WebP and a JPEG/PNG, and each gallery image has `large/` and `thumbs/` copies.
2. Set real `width` and `height` in the markup.
3. Run `python3.12 scripts/sitemap.py regen` for gallery changes; add other images to `templates/sitemap.xml` by hand with ES and EN text.
4. Run `zola build`.
