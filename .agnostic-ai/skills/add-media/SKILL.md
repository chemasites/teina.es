---
name: add-media
description: Add photos or YouTube videos to the Teína media gallery, with WebP, thumbnails, and sitemap entries.
user-invocable: true
argument-hint: "<image-path-or-youtube-url> [caption-es] [caption-en]"
x-claude:
  allowed-tools: Read, Edit, Write, Bash, Grep, Glob
---

Add media to the gallery in `templates/media.html`. Request: $ARGUMENTS

## Photos

1. Copy the images into `local/imgs/`.
2. `python3.12 scripts/media.py import --dry-run`, check the plan, then run it without `--dry-run`. It writes `large/` (1600px) and `thumbs/` (600px) as JPEG and WebP and appends a `<picture>` entry with `width` and `height`.
3. Give each photo a short ES and EN description: pass `--alt-es`/`--alt-en` for a single photo, or replace the generic "Foto Teína N" / "Teína Photo N" alt text afterwards.

## YouTube videos

1. Take the video ID from the URL.
2. Copy an existing `<lite-youtube>` block in `templates/media.html` and set `videoid` and `data-title`. Add a matching `VideoObject` to the page JSON-LD.

## Finish

1. `python3.12 scripts/sitemap.py regen` to rebuild the `/media/` sitemap blocks.
2. `zola build`.
3. Commit as `feat(media): ...` and push to `main`.
