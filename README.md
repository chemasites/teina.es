# Teína

Website for Teína, an indie pop rock band from Calasparra, Murcia.

## Prerequisites

- [Zola](https://www.getzola.org/documentation/getting-started/installation/) 0.23 (static site generator)
- Python 3.11+ for the scripts in `scripts/`
- [agnostic-ai](https://github.com/Chemaclass/agnostic-ai) for the AI assistant config

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
`scripts/concert.py` adds, removes, updates and lists concerts on the
concerts page. See [scripts/README.md](scripts/README.md) for usage.

## AI assistants

Instructions, rules, agents and skills for Claude Code and Codex live in [`.agnostic-ai/`](.agnostic-ai/). The files they generate (`CLAUDE.md`, `AGENTS.md`, `.claude/`, `.codex/`, `.agents/`) are not committed.

After cloning or pulling spec changes, regenerate them:

```bash
agnostic-ai sync
```

Edit the specs, never the generated files. `agnostic-ai sync --check` fails when they drift.
