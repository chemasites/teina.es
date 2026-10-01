---
paths:
  - "sass/**/*.scss"
---

# SCSS rules

- The site is a festival lineup poster printed in the logo's colours. `DESIGN.md` at the repository root is the design system; read it before a visual change.
- Colours come only from the tokens in `:root` (`--plaster`, `--sand`, `--leaf`, `--fern`, `--forest`, `--ink`). No new hex values outside `:root`. No bright inks (pink, lemon, cobalt): the band rejected them.
- Each page is a field: `field--plaster`, `field--sand`, `field--leaf` or `field--forest` on `<body>` (via the `field` block) and on sections. The field sets `--field`, `--on-field` and `--ghost`.
- One light theme. There is no dark mode and no theme toggle.
- Type: Big Shoulders (display, uppercase) and Archivo (text), self-hosted in `static/fonts/`. No other faces.
- Lists of names use `.bill`; separators are drawn by CSS and clipped at line starts. Do not type dots between names.
- Buttons are `.ticket` stubs (`ticket--paper`, `ticket--sand`, `ticket--leaf`, `ticket--sm`). Rules are 3px ink.
- Mobile first; check 390px and 1440px. Zola compiles Sass during `zola build`; a Sass error fails the build.
