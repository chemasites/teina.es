---
paths:
  - "content/**/*.md"
---

# Content rules

- Spanish is `<name>.md`, English is `<name>.en.md`. Change both in the same commit.
- Front matter is TOML between `+++` lines. Sections use `_index.md` / `_index.en.md`.
- `template` picks the Tera template. Most page text lives in that template, not in the Markdown body.
- English URLs keep the Spanish slugs under `/en/` (`/en/banda/`, `/en/conciertos/`). Do not add `path` overrides.
- Sections reject a top-level `updated`; put it under `[extra]` as `updated = "YYYY-MM-DD"` so the sitemap gets a real `<lastmod>`.
