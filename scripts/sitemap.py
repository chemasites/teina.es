#!/usr/bin/env python3
"""Regenerate media section of templates/sitemap.xml from templates/media.html.

Only the `/media/` and `/en/media/` blocks are rewritten. Homepage, banda,
and page-level entries are left untouched.

Parses `<a href="media/...">` gallery entries and `<lite-youtube videoid=...
data-title=...>` videos from templates/media.html, then emits matching
`<image:image>` and `<video:video>` blocks with ES/EN titles and captions.

Usage:
  scripts/sitemap.py regen [--dry-run]
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEDIA_HTML = ROOT / "templates" / "media.html"
SITEMAP = ROOT / "templates" / "sitemap.xml"

BASE_URL = "https://teina.es"
CAPTION_ES = "Teína, banda de indie pop rock"
CAPTION_EN = "Teína, indie pop rock band"

GALLERY_RE = re.compile(
    r'<section class="section section-alt" id="galeria">.*?'
    r'<div class="gallery gallery-large">\n(.*?)\n        </div>\n    </section>',
    re.DOTALL,
)
GALLERY_ENTRY_RE = re.compile(
    r"<a href=\"\{\{ get_url\(path='media/([^']+)'\) \}\}\".*?"
    r"alt=\"\{% if lang == 'en' %\}([^{]*?)\{% else %\}([^{]*?)\{% endif %\}\"",
    re.DOTALL,
)

VIDEO_RE = re.compile(
    r'<lite-youtube videoid="([^"]+)" data-title="'
    r"Teína - \{% if lang == 'en' %\}([^{]*?)\{% else %\}([^{]*?)\{% endif %\}\""
)

SITEMAP_ES_RE = re.compile(
    r'(\{% if sitemap_entry\.permalink is ending_with\("/media/"\) '
    r'and not "/en/" in sitemap_entry\.permalink %\}\n)'
    r'(.*?)'
    r'(        \{% endif %\}\n        \{# Media page images and videos - English #\})',
    re.DOTALL,
)
SITEMAP_EN_RE = re.compile(
    r'(\{% if "/en/media/" in sitemap_entry\.permalink %\}\n)'
    r'(.*?)'
    r'(        \{% endif %\}\n    </url>)',
    re.DOTALL,
)


def parse_gallery() -> list[tuple[str, str, str]]:
    content = MEDIA_HTML.read_text(encoding='utf-8')
    m = GALLERY_RE.search(content)
    if not m:
        sys.exit("error: gallery section not found")
    out = []
    for em in GALLERY_ENTRY_RE.finditer(m.group(1)):
        out.append((em.group(1), em.group(3), em.group(2)))  # name, alt_es, alt_en
    return out


def parse_videos() -> list[tuple[str, str, str]]:
    content = MEDIA_HTML.read_text(encoding='utf-8')
    out = []
    for vm in VIDEO_RE.finditer(content):
        out.append((vm.group(1), vm.group(3), vm.group(2)))  # id, title_es, title_en
    return out


def build_image_block(name: str, title: str, caption: str) -> str:
    return (
        '        <image:image>\n'
        f'            <image:loc>{BASE_URL}/media/{name}</image:loc>\n'
        f'            <image:title>{title}</image:title>\n'
        f'            <image:caption>{caption}</image:caption>\n'
        '        </image:image>'
    )


def build_video_block(vid: str, title: str, description: str) -> str:
    return (
        '        <video:video>\n'
        f'            <video:thumbnail_loc>https://img.youtube.com/vi/{vid}/maxresdefault.jpg</video:thumbnail_loc>\n'
        f'            <video:title>Teína - {title}</video:title>\n'
        f'            <video:description>{description}</video:description>\n'
        f'            <video:player_loc>https://www.youtube.com/embed/{vid}</video:player_loc>\n'
        '        </video:video>'
    )


def build_block(images, videos, lang: str) -> str:
    lines = []
    for name, alt_es, alt_en in images:
        title = alt_en if lang == 'en' else alt_es
        caption = CAPTION_EN if lang == 'en' else CAPTION_ES
        lines.append(build_image_block(name, title, caption))
    for vid, title_es, title_en in videos:
        title = title_en if lang == 'en' else title_es
        if lang == 'en':
            description = f"{title} of Teína, indie pop rock band from Calasparra, Murcia, Spain"
        else:
            description = f"{title} de Teína, banda de indie pop rock de Calasparra, Murcia"
        lines.append(build_video_block(vid, title, description))
    return '\n'.join(lines) + '\n'


def cmd_regen(args: argparse.Namespace) -> None:
    images = parse_gallery()
    videos = parse_videos()
    print(f"found {len(images)} image(s), {len(videos)} video(s) in media.html")

    es_block = build_block(images, videos, 'es')
    en_block = build_block(images, videos, 'en')

    content = SITEMAP.read_text(encoding='utf-8')
    m_es = SITEMAP_ES_RE.search(content)
    if not m_es:
        sys.exit("error: Spanish media block markers not found in sitemap.xml")
    content2 = (content[:m_es.start()] + m_es.group(1) + es_block
                + m_es.group(3) + content[m_es.end():])
    m_en = SITEMAP_EN_RE.search(content2)
    if not m_en:
        sys.exit("error: English media block markers not found in sitemap.xml")
    content3 = (content2[:m_en.start()] + m_en.group(1) + en_block
                + m_en.group(3) + content2[m_en.end():])

    if args.dry_run:
        print("DRY: would rewrite /media/ and /en/media/ blocks")
        print(f"  ES block: {len(es_block)} chars")
        print(f"  EN block: {len(en_block)} chars")
        return
    SITEMAP.write_text(content3, encoding='utf-8')
    print(f"rewrote templates/sitemap.xml "
          f"({len(images)} image entries, {len(videos)} video entries per locale)")


def main() -> None:
    p = argparse.ArgumentParser(
        description="Regenerate media entries in templates/sitemap.xml")
    sub = p.add_subparsers(dest='cmd', required=True)
    r = sub.add_parser('regen', help='regenerate media blocks from media.html')
    r.add_argument('--dry-run', action='store_true')
    r.set_defaults(func=cmd_regen)
    args = p.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
