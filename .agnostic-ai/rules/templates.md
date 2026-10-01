---
paths:
  - "templates/**/*.html"
---

# Template rules

## Tera v2 (Zola 0.23+)

- Tests take keyword arguments: `is ending_with(pat="/en/")`, `is starting_with(pat="...")`.
- Macros are gone; use `{% component %}` and call it as `{{ <name arg="x" /> }}`.
- Every `{% block %}` in a child template must exist in `base.html`, or the build fails.
- Prefer expressions over mutable state: `{% set lang_prefix = "/en" if lang == "en" else "" %}`, `[c for c in list if cond]`, and `loop.last` for separators instead of `set_global` flags.
- Index arrays with `list[0]`, not `list.0`. An undefined variable errors; use `a?.b` or `default(value=...)`.

## Site conventions

- Pages extend `base.html`, set the page colour with `{% block field %}field--<name>{% endblock %}` and `{% block theme_color %}`, and fill `{% block content %}`; navbar and footer come from `templates/partials/`.
- The footer partial prints the booking band on every page. Set `{% set hide_booking = true %}` before including it on a page that is already the booking page.
- Page headers use `.poster-head` with an `h1.headliner` holding `.headliner-ink` plus an `aria-hidden` `.headliner-ghost` copy of the same text.
- Bilingual text uses `{% if lang == "en" %}...{% else %}...{% endif %}` inline. There are no translation keys.
- Images use `<picture>` with a WebP `<source>`, a JPEG/PNG `<img>`, `width`, `height`, and native `loading="lazy"` below the fold. Never a JS-only `data-src`: crawlers miss it.
- Pipe `config.base_url`, `section.permalink`, and `page.permalink` through `| safe` inside `<script type="application/ld+json">`. Tera escapes `&`, `<`, `>`, `"`, and `'` as entities, and script content is not decoded, so Google reads a corrupted URL.
- The band entity is declared once as `"@id": "{{ config.base_url | safe }}/#band"`. Other JSON-LD references that `@id` instead of repeating the MusicGroup.
- Concerts render from `data/concerts.toml` and FAQ from `data/faq.toml`, both visibly and as JSON-LD. Edit the data, never the generated markup.
