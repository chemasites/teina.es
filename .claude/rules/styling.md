---
paths:
  - "sass/**/*.scss"
---

# SCSS Rules

- Always use CSS custom properties (`var(--xxx)`) for colors, never hardcode hex values
- Both light and dark modes must work - test both theme states
- Light palette: cream/beige (#f9f5f0 bg, #3a3530 text)
- Dark palette: dark brown (#1a1816 bg, #e8e4e0 text)
- Theme is toggled via `[data-theme="dark"]` attribute on `<html>`
- Mobile-first responsive design
- After SCSS changes, `zola build` compiles Sass automatically - verify no errors
