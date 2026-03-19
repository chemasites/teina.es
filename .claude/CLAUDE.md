# Teína Website - Project Instructions

## Tech Stack

- **Static site generator**: [Zola](https://www.getzola.org/) (Rust-based, config in `config.toml`)
- **Styling**: Sass (`sass/style.scss`, compiled by Zola)
- **Templates**: Tera templating engine (Jinja2-like)
- **Languages**: Spanish (default) and English
- **Hosting**: GitHub Pages, deployed via GitHub Actions on push to `main`
- **CI/CD**: `.github/workflows/main.yml` (Zola 0.22.0 build + deploy)

## Project Structure

- `config.toml` - Zola site config (base_url, languages, extra vars)
- `content/` - Markdown content pages (`.md` for ES, `.en.md` for EN)
- `templates/` - Tera HTML templates (`base.html` is the layout)
- `templates/partials/` - Reusable components (navbar, footer)
- `templates/sitemap.xml` - Custom sitemap template
- `sass/` - Stylesheets (compiled to CSS by Zola)
- `static/` - Static assets (images, manifest, robots.txt, llms.txt)

## Development Commands

- `zola build` - Build the site into `public/`
- `zola serve` - Dev server with live reload (default: localhost:1111)
- `zola check` - Validate internal links and config

## OpenClaw / Telegram Bot Workflow

This project is managed via an OpenClaw Telegram bot for quick website updates. Common bot-triggered tasks:

- **Add concert**: Provide date, venue, city, ticket URL → use `/add-concert`
- **Add media**: Provide image file or YouTube URL → use `/add-media`
- **Add song**: Provide song name, year, links → use `/add-song`
- **Style changes**: Describe the visual change → delegate to `style-designer` agent
- **SEO updates**: Sitemap or structured data changes → delegate to `seo-optimizer` agent
- **Image optimization**: Run `/optimize-images` after adding new images

After any content change: build, commit, and push to `main` to trigger GitHub Pages deploy.

## Available Agents

- `content-editor` - Edit pages, text, translations, band info, concerts, songs
- `seo-optimizer` - Sitemap, structured data, meta tags, Schema.org
- `image-manager` - Image optimization, WebP conversion, thumbnails
- `style-designer` - SCSS styling, dark/light themes, responsive design

## Available Skills

- `/add-concert <date> <venue> <city> [ticket-url]` - Add a concert event
- `/add-media <image-or-youtube-url> [caption-es] [caption-en]` - Add gallery media
- `/add-song <name> <year> [spotify-url] [youtube-url]` - Add an original song
- `/update-sitemap` - Audit and sync sitemap with current content
- `/optimize-images` - Find and optimize all images
- `/build` - Build site and report errors

## Sitemap Maintenance

When modifying any of these files, **always check if `templates/sitemap.xml` needs updating**:

- `templates/banda.html` - If band member images change, update sitemap image entries
- `templates/media.html` - If gallery images or YouTube videos change, update sitemap image/video entries
- `templates/index.html` - If homepage images change, update sitemap image entries
- `static/banda/*` - New band member photos need sitemap entries
- `static/media/*` - New media images need sitemap entries

The sitemap includes localized image titles/captions for both Spanish (ES) and English (EN) versions.

### Sitemap structure

- Image entries: `<image:image>` with `<image:loc>`, `<image:title>`, `<image:caption>`
- Video entries: `<video:video>` with `<video:thumbnail_loc>`, `<video:title>`, `<video:description>`, `<video:player_loc>`

## Image Conventions

- Use WebP format with JPEG/PNG fallbacks where possible
- Band photos in `static/banda/`, concert/media in `static/media/`
- Always include width/height attributes for CLS optimization
- Use `sips` (macOS) or `cwebp` for image conversion

## i18n

- Default language is Spanish (`es`)
- English translations use `.en.md` suffix for content and Tera `trans()` macro in templates
- URL structure: `/en/...` for English, `/...` for Spanish

## Band Members

Juanjo (guitar/vocals), Nacho (sax/percussion/backing vocals), AJ Ruíz (bass), J.A. Garre (keyboards), Adri (drums), Darwin (guitar/backing vocals)
