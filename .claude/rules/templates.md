---
paths:
  - "templates/**/*.html"
---

# Template Rules

- This is a Zola site using Tera templates (Jinja2-like syntax)
- `base.html` is the layout - all pages extend it with `{% extends "base.html" %}`
- Use `{% block content %}{% endblock %}` for page content
- i18n: use `{% if lang == "en" %}` for language-specific content
- Partials are in `templates/partials/` and included with `{% include "partials/navbar.html" %}`
- Images must use `<picture>` with WebP source + fallback, and include `width`/`height`
- After ANY template change, run `zola build` to verify
- If images or videos are added/changed, update `templates/sitemap.xml`
- Never interpolate `config.base_url`, `section.permalink` or `page.permalink` into a `<script type="application/ld+json">` block without `| safe` — Tera escapes `/` to `&#x2F;` and script content is not entity-decoded, so the URL reaches Google corrupted
- The band entity is declared once with `"@id": "{{ config.base_url | safe }}/#band"`; other pages reference that `@id` instead of restating the MusicGroup
- FAQ content lives in `data/faq.toml` and is rendered both visibly and as JSON-LD from that one source — Google requires FAQ markup to match text the visitor can see
- Gallery images use a real `src` plus native `loading="lazy"`; never a JS-only `data-src`, which hides them from crawlers
