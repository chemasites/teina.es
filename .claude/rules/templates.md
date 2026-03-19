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
