---
name: optimize-images
description: Audit Teína images for missing WebP variants, thumbnails, large copies, and width/height attributes, and fix them.
user-invocable: true
x-claude:
  allowed-tools: Bash, Read, Edit, Write, Glob, Grep
---

1. List images in `static/banda/`, `static/media/`, `static/media/large/`, `static/media/thumbs/`, `static/conciertos/`, `static/imgs/`.
2. For each JPEG/PNG without a WebP sibling: `cwebp -q 80 in.jpg -o in.webp`.
3. For each gallery entry in `templates/media.html`, check that `static/media/large/` (1600px) and `static/media/thumbs/` (600px) hold both JPEG and WebP. Create a missing size from the `large/` JPEG with `sips -Z` and `cwebp`.
4. Find `<img>` tags in `templates/` without `width` and `height`; set them from `sips -g pixelWidth -g pixelHeight`.
5. `zola build`, then report bytes saved and anything left to fix.
