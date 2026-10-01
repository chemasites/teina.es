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
2. `python3.12 scripts/media.py import --dry-run [--alt-es "..." --alt-en "..."]`, check the plan, then run it without `--dry-run`. It writes a resized copy to `static/media/`, a 600px JPEG thumbnail, and the gallery entry.
3. Match the existing entries: add a 600px WebP thumbnail, a 1600px `static/media/large/` JPEG and WebP (`sips -Z 1600`, `cwebp -q 80`), and point the entry's `href`, `data-fallback`, `<source>`, and `<img>` at them like its neighbours. Set real `width` and `height`. Delete the resized copy in `static/media/`; the gallery serves only `large/` and `thumbs/`.
4. Replace generic alt text ("Foto Teína N") with a short description of the photo in both languages.

## YouTube videos

1. Take the video ID from the URL.
2. Copy an existing `<lite-youtube>` block in `templates/media.html` and set `videoid` and `data-title`. Add a matching `VideoObject` to the page JSON-LD.

## Finish

1. `python3.12 scripts/sitemap.py regen` to rebuild the `/media/` sitemap blocks.
2. `zola build`.
3. Commit as `feat(media): ...` and push to `main`.
