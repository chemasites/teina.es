---
paths:
  - "sass/**/*.scss"
---

# SCSS rules

- The site is a modern band site in the logo's colours, led by the real logo (`static/imgs/teina-logo-trim.*`) and live photos. `DESIGN.md` at the repository root is the design system; read it before a visual change.
- Colours come only from the tokens in `:root` (`--plaster`, `--sand`, `--leaf`, `--fern`, `--forest`, `--ink`). No new hex values outside `:root`. No bright inks (pink, lemon, cobalt): the band rejected them.
- Each page is a field: `field--plaster`, `field--sand`, `field--leaf` or `field--forest` on `<body>` (via the `field` block) and on sections. The field sets `--field`, `--on-field` and `--ghost`.
- One light theme. There is no dark mode and no theme toggle.
- Type: Archivo only (self-hosted, subset, in `static/fonts/`), mixed case for headings. Uppercase only for small labels. No condensed or poster faces: the band said the condensed caps looked like a bullfight poster.
- Lists of names (artists, towns, event types) use `.bill`, rendered as outlined tags. No dot-separated name rows.
- Buttons are `.ticket` stubs (`ticket--paper`, `ticket--sand`, `ticket--leaf`, `ticket--sm`). Rules are 3px ink.
- Mobile first; check 390px and 1440px. Zola compiles Sass during `zola build`; a Sass error fails the build.
