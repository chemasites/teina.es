# Teína website

Bilingual site for Teína, an indie pop rock band from Calasparra, Murcia: https://teina.es

## Stack

- [Zola](https://www.getzola.org/) 0.23 (pinned in `.github/workflows/main.yml`), config in `zola.toml`
- Tera v2 templates in `templates/`, Sass in `sass/style.scss`
- Visual design: `DESIGN.md` (festival lineup poster in the logo colours); product facts and audience: `PRODUCT.md`
- Spanish is the default language (`/...`), English lives under `/en/...`
- GitHub Pages: every push to `main` runs `zola check`, `zola build`, and deploys

## Layout

- `content/` - pages and section front matter (`.md` ES, `.en.md` EN)
- `data/concerts.toml` - every concert, the single source for the list and its JSON-LD
- `data/faq.toml` - FAQ, rendered visibly and as JSON-LD
- `templates/` - `base.html` layout, one template per page, `partials/` for navbar and footer
- `templates/sitemap.xml` - hand-maintained sitemap with ES/EN image and video entries
- `static/` - images (`banda/`, `media/`, `conciertos/`, `imgs/`), `robots.txt`, `llms.txt`, `llms-full.txt`
- `scripts/` - Python helpers, documented in `scripts/README.md`
- `local/` - untracked input drop zone (`local/imgs/` feeds `scripts/media.py`)

## Commands

- `zola build` - build into `public/`; run after every change
- `zola check` - validate templates and links without writing `public/`, same as CI
- `zola serve` - live preview on http://127.0.0.1:1111
- Scripts need Python 3.11+ (`tomllib`); macOS `python3` is 3.9, so call `python3.12`

## Common requests

The site is often updated from short requests sent through a Telegram bot. Do the task, build, commit, and push to `main`.

| Request | How |
|---|---|
| Add, change, or remove a concert | `add-concert` skill (`scripts/concert.py`) |
| Add photos or a YouTube video | `add-media` skill (`scripts/media.py`, then `scripts/sitemap.py regen`) |
| Add an original song | `add-song` skill |
| Sitemap audit | `update-sitemap` skill |
| Missing WebP or thumbnails | `optimize-images` skill |
| Text and translations | `content-editor` agent |
| Visual change | `style-designer` agent |
| Meta tags, JSON-LD, sitemap | `seo-optimizer` agent |
| Image conversion | `image-manager` agent |

## Cross-file rules

- Change Spanish and English together, in content and in `{% if lang == "en" %}` template branches.
- Adding, removing, or renaming an image or video in `templates/index.html`, `banda.html`, or `media.html` needs a matching `templates/sitemap.xml` entry with ES and EN text.
- Every image ships as WebP plus a JPEG/PNG fallback in a `<picture>`, with `width` and `height`.

## Band

Juanjo (guitar, vocals), Nacho (sax, percussion, backing vocals), AJ Ruíz (bass), J.A. Garre (keyboards), Adri (drums), Darwin (guitar, backing vocals).
