---
name: add-media
description: Add new photos or videos to the Teína media gallery
user-invocable: true
argument-hint: "<image-path-or-youtube-url> [caption-es] [caption-en]"
allowed-tools: Read, Edit, Write, Bash, Grep, Glob
---

Add new media (photos or YouTube videos) to the gallery. Arguments: $ARGUMENTS

## For photos

1. Check if the image exists in `static/media/`; if provided as a path outside static/, copy it there
2. Create a WebP version if only JPEG/PNG provided: `cwebp -q 80 input.jpg -o output.webp`
3. Create a thumbnail in `static/media/thumbs/`: `sips -Z 400 input.jpg --out static/media/thumbs/input.jpg`
4. Get image dimensions: `sips -g pixelWidth -g pixelHeight image.jpg`
5. Add the gallery entry in `templates/media.html` following existing HTML structure
6. Update `templates/sitemap.xml` with image entry (both ES and EN captions)
7. Run `zola build`

## For YouTube videos

1. Read `templates/media.html` to find existing lite-youtube embeds
2. Extract the video ID from the YouTube URL
3. Add a new `<lite-youtube>` element following existing pattern
4. Update `templates/sitemap.xml` with video entry (both ES and EN titles/descriptions)
5. Run `zola build`
