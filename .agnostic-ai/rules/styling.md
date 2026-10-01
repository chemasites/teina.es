---
paths:
  - "sass/**/*.scss"
---

# SCSS rules

- Theme colors come from CSS custom properties (`var(--...)`). New hex values go only in the `:root` and `[data-theme="dark"]` token blocks; leave existing neutral hexes (`#fff`, `#000`, shimmer greys) alone unless the task touches them.
- Light palette: `#f9f5f0` background, `#3a3530` text. Dark palette: `#1a1816` background, `#e8e4e0` text.
- Dark mode is `[data-theme="dark"]` on `<html>`, set by the toggle in `base.html` with `prefers-color-scheme` as the default. Check every change in both themes.
- Mobile first. Reuse existing class names and breakpoints before adding new ones.
- Zola compiles Sass during `zola build`; a Sass error fails the build.
