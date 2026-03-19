---
paths:
  - "templates/sitemap.xml"
---

# Sitemap Rules

- Every image referenced in templates needs an `<image:image>` entry
- Every YouTube video needs a `<video:video>` entry
- ALL entries need localized titles/captions for both ES and EN
- Priority: 1.0 homepage, 0.8 main sections (banda, media, musica, contacto), 0.5 others
- Use `<changefreq>` based on update frequency: weekly for homepage, monthly for sections
- Image URLs must use the full `https://teina.es/` base URL
- Band member images are under `/banda/`, gallery images under `/media/`
