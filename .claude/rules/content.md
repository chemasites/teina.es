---
paths:
  - "content/**/*.md"
---

# Content Rules

- Spanish is the default language (`.md` files)
- English translations use `.en.md` suffix
- Always update BOTH language versions when changing content
- Frontmatter uses TOML format (`+++` delimiters)
- Section index files are `_index.md` / `_index.en.md`
- `template` field in frontmatter maps to the Tera template to use
- English pages have `path` overrides for clean URL structure (e.g., `path = "en/band"`)
