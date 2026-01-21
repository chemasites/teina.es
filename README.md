# Teína

Website for Teína, an indie pop rock band from Calasparra, Murcia.

## Prerequisites

- [Zola](https://www.getzola.org/documentation/getting-started/installation/) (static site generator)

## Development

Run the development server:

```bash
zola serve
```

The site will be available at `http://127.0.0.1:1111/`

## Build

Generate the static site:

```bash
zola build
```

The output will be in the `public/` directory.

## Deployment

The site is automatically deployed to GitHub Pages via GitHub Actions on push to `main`.

## Structure

```
├── content/          # Markdown content
├── sass/             # SCSS styles
├── static/           # Static assets (images, fonts)
├── templates/        # HTML templates
├── config.toml       # Zola configuration
└── public/           # Generated site (gitignored)
```
