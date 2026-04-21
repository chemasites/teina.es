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

## Deployment

The site is automatically deployed to GitHub Pages via GitHub Actions on push to `main`.

## Scripts

Maintenance scripts live in [`scripts/`](scripts/README.md). Notably
`scripts/concert.py` adds, removes, updates and lists concerts in the
homepage. See [scripts/README.md](scripts/README.md) for usage.
