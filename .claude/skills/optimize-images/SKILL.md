---
name: optimize-images
description: Scan and optimize all images on the site - create missing WebP variants, thumbnails, and check dimensions
user-invocable: true
allowed-tools: Bash, Read, Edit, Write, Glob, Grep
---

Audit and optimize all images on the Teína website.

## Steps

1. List all images in `static/banda/`, `static/media/`, `static/conciertos/`, `static/imgs/`
2. For each JPEG/PNG without a WebP variant, create one: `cwebp -q 80 input.jpg -o output.webp`
3. For each gallery image in `static/media/` without a thumbnail in `static/media/thumbs/`, create one
4. Check all `<img>` and `<picture>` tags in templates for missing `width`/`height` attributes
5. Report total size savings and any issues found
6. If HTML changes were made, run `zola build` to verify
