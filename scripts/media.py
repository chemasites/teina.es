#!/usr/bin/env python3
"""Copy + optimize images from local/imgs/ into the media gallery.

For each image in the source dir:
  - Sanitize the filename (lowercase, safe chars)
  - Resize full image to --max width, write to static/media/<name>.<ext>
  - Generate a JPEG thumbnail to static/media/thumbs/<name>.jpg at --thumb width
  - Strip EXIF metadata (if exiftool is available)
  - Append an <a class="gallery-item"> entry to the gallery in
    templates/media.html (#galeria section)
  - Optionally remove the source file after successful import (--move)

Requires: sips (macOS built-in). Optional: exiftool.

Usage:
  scripts/media.py import [SRC] [--max W] [--thumb W] [--quality Q]
                          [--alt-es TEXT] [--alt-en TEXT]
                          [--move] [--dry-run]

SRC defaults to local/imgs/.
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SRC = ROOT / "local" / "imgs"
MEDIA_DIR = ROOT / "static" / "media"
THUMBS_DIR = MEDIA_DIR / "thumbs"
TEMPLATE = ROOT / "templates" / "media.html"

CONVERT_TO_JPG_EXTS = {".heic", ".heif", ".webp", ".jpeg"}
SUPPORTED_EXTS = {".jpg", ".jpeg", ".png", ".heic", ".heif", ".webp"}

GALLERY_RE = re.compile(
    r'(<section class="section section-alt" id="galeria">.*?'
    r'<div class="gallery gallery-large">\n)(.*?)'
    r'(\n        </div>\n    </section>)',
    re.DOTALL,
)


def sanitize(stem: str) -> str:
    s = stem.strip().lower()
    s = re.sub(r'[\s_]+', '-', s)
    s = re.sub(r'[^a-z0-9.\-]', '', s)
    s = re.sub(r'-+', '-', s).strip('-.')
    return s or 'img'


def target_ext(src_ext: str) -> str:
    e = src_ext.lower()
    if e in CONVERT_TO_JPG_EXTS:
        return '.jpg'
    return e  # .jpg or .png


def run(cmd: list[str]) -> None:
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"error: {' '.join(cmd)}\n{r.stderr.strip()}")


def process_full(src: Path, dst: Path, max_w: int, quality: int) -> None:
    ext = dst.suffix.lower()
    fmt = 'png' if ext == '.png' else 'jpeg'
    cmd = ['sips', '-Z', str(max_w), '-s', 'format', fmt]
    if fmt == 'jpeg':
        cmd += ['-s', 'formatOptions', str(quality)]
    cmd += [str(src), '--out', str(dst)]
    run(cmd)


def process_thumb(src: Path, dst: Path, thumb_w: int, quality: int) -> None:
    run(['sips', '-Z', str(thumb_w),
         '-s', 'format', 'jpeg',
         '-s', 'formatOptions', str(quality),
         str(src), '--out', str(dst)])


def strip_exif(path: Path) -> None:
    if shutil.which('exiftool') is None:
        return
    subprocess.run(
        ['exiftool', '-all=', '-overwrite_original', str(path)],
        capture_output=True,
    )


def next_alt_index(content: str) -> int:
    nums = [int(n) for n in re.findall(r'Foto Teína (\d+)', content)]
    return (max(nums) + 1) if nums else 1


def build_gallery_entry(name: str, alt_es: str, alt_en: str) -> str:
    thumb = Path(name).stem + '.jpg'
    return (
        f'            <a href="{{{{ get_url(path=\'media/{name}\') }}}}" '
        f'class="gallery-item" data-lightbox>\n'
        f'                <img data-src="{{{{ get_url(path=\'media/thumbs/{thumb}\') }}}}" '
        f'alt="{{% if lang == \'en\' %}}{alt_en}{{% else %}}{alt_es}{{% endif %}}" '
        f'loading="lazy" decoding="async">\n'
        f'            </a>'
    )


def append_to_gallery(entries: list[str]) -> None:
    content = TEMPLATE.read_text(encoding='utf-8')
    m = GALLERY_RE.search(content)
    if not m:
        sys.exit("error: #galeria gallery-large block not found in templates/media.html")
    new_body = m.group(2) + '\n' + '\n'.join(entries)
    updated = content[:m.start()] + m.group(1) + new_body + m.group(3) + content[m.end():]
    TEMPLATE.write_text(updated, encoding='utf-8')


GALLERY_ENTRY_RE = re.compile(
    r"            <a href=\"\{\{ get_url\(path='media/([^']+)'\) \}\}\" "
    r"class=\"gallery-item\" data-lightbox>\n"
    r"                <img data-src=\"\{\{ get_url\(path='media/thumbs/[^']+'\) \}\}\" "
    r"alt=\"\{% if lang == 'en' %\}([^{]*?)\{% else %\}([^{]*?)\{% endif %\}\" "
    r"loading=\"lazy\" decoding=\"async\">\n"
    r"            </a>"
)


def parse_gallery_entries() -> list[tuple[str, str, str]]:
    content = TEMPLATE.read_text(encoding='utf-8')
    m = GALLERY_RE.search(content)
    if not m:
        sys.exit("error: #galeria gallery-large block not found")
    body = m.group(2)
    return [(em.group(1), em.group(3), em.group(2))
            for em in GALLERY_ENTRY_RE.finditer(body)]


def cmd_list(_args: argparse.Namespace) -> None:
    entries = parse_gallery_entries()
    rows = [(str(i + 1), name, alt_es, alt_en)
            for i, (name, alt_es, alt_en) in enumerate(entries)]
    headers = ("ID", "FILE", "ALT (ES)", "ALT (EN)")
    widths = [max(len(h), max((len(r[i]) for r in rows), default=0))
              for i, h in enumerate(headers)]
    fmt = "  ".join("{:<" + str(w) + "}" for w in widths)
    print(fmt.format(*headers))
    print("  ".join("-" * w for w in widths))
    for r in rows:
        print(fmt.format(*r))


def remove_from_gallery(name: str) -> bool:
    content = TEMPLATE.read_text(encoding='utf-8')
    m = GALLERY_RE.search(content)
    if not m:
        sys.exit("error: #galeria gallery-large block not found")
    body = m.group(2)
    new_body, n = re.subn(
        r'\n?            <a href="\{\{ get_url\(path=\''
        + re.escape('media/' + name)
        + r"'\) \}\}\" class=\"gallery-item\" data-lightbox>\n"
          r"                <img data-src=\"[^\"]+\" alt=\"[^\"]+\" "
          r"loading=\"lazy\" decoding=\"async\">\n"
          r"            </a>",
        '', body)
    if n == 0:
        return False
    updated = content[:m.start()] + m.group(1) + new_body + m.group(3) + content[m.end():]
    TEMPLATE.write_text(updated, encoding='utf-8')
    return True


def cmd_remove(args: argparse.Namespace) -> None:
    entries = parse_gallery_entries()
    if args.id is not None:
        if args.id < 1 or args.id > len(entries):
            sys.exit(f"error: invalid id {args.id}; valid 1..{len(entries)}")
        name = entries[args.id - 1][0]
    elif args.name:
        name = args.name
    else:
        sys.exit("error: pass --id or --name")
    removed_tpl = remove_from_gallery(name)
    stem = Path(name).stem
    removed_files = []
    if not args.keep_files:
        for p in (MEDIA_DIR / name, THUMBS_DIR / (stem + '.jpg')):
            if p.exists():
                p.unlink()
                removed_files.append(p.name)
    print(f"removed: {name} (template={removed_tpl}, "
          f"files={','.join(removed_files) or 'none'})")


def cmd_import(args: argparse.Namespace) -> None:
    src_dir = Path(args.src).expanduser()
    if not src_dir.is_dir():
        sys.exit(f"error: source dir not found: {src_dir}")
    files = sorted(
        p for p in src_dir.iterdir()
        if p.is_file() and p.suffix.lower() in SUPPORTED_EXTS
    )
    if not files:
        print(f"no images found in {src_dir}")
        return
    MEDIA_DIR.mkdir(parents=True, exist_ok=True)
    THUMBS_DIR.mkdir(parents=True, exist_ok=True)
    template_content = TEMPLATE.read_text(encoding='utf-8')
    alt_idx = next_alt_index(template_content)

    entries: list[str] = []
    imported: list[Path] = []
    skipped = 0

    for src in files:
        stem = sanitize(src.stem)
        name = stem + target_ext(src.suffix)
        dst = MEDIA_DIR / name
        thumb_dst = THUMBS_DIR / (stem + '.jpg')
        if dst.exists():
            print(f"skip (exists): {name}")
            skipped += 1
            continue
        if args.dry_run:
            print(f"DRY: {src.name} -> media/{name} + thumbs/{stem}.jpg")
            alt_idx += 1
            continue
        print(f"import: {src.name} -> media/{name}")
        process_full(src, dst, args.max, args.quality)
        process_thumb(src, thumb_dst, args.thumb, args.thumb_quality)
        strip_exif(dst)
        alt_es = args.alt_es or f"Foto Teína {alt_idx}"
        alt_en = args.alt_en or f"Teína Photo {alt_idx}"
        alt_idx += 1
        entries.append(build_gallery_entry(name, alt_es, alt_en))
        imported.append(src)

    if entries and not args.dry_run:
        append_to_gallery(entries)
        print(f"added {len(entries)} entry(ies) to templates/media.html")
    if args.move and not args.dry_run:
        for src in imported:
            src.unlink()
            print(f"removed source: {src.name}")
    print(f"done. imported={len(imported)} skipped={skipped}")


def main() -> None:
    p = argparse.ArgumentParser(
        description="Copy and optimize local images into the media gallery")
    sub = p.add_subparsers(dest='cmd', required=True)

    i = sub.add_parser('import', help='import from source dir')
    i.add_argument('src', nargs='?', default=str(DEFAULT_SRC),
                   help=f'source dir (default {DEFAULT_SRC})')
    i.add_argument('--max', type=int, default=2048,
                   help='max full-image width (px, default 2048)')
    i.add_argument('--thumb', type=int, default=600,
                   help='thumbnail width (px, default 600)')
    i.add_argument('--quality', type=int, default=75,
                   help='JPEG quality for full image 1-100 (default 75)')
    i.add_argument('--thumb-quality', type=int, default=70,
                   help='JPEG quality for thumbnail 1-100 (default 70)')
    i.add_argument('--alt-es', help='Spanish alt text (default "Foto Teína N")')
    i.add_argument('--alt-en', help='English alt text (default "Teína Photo N")')
    i.add_argument('--move', action='store_true',
                   help='delete source after successful import')
    i.add_argument('--dry-run', action='store_true',
                   help='print actions without writing')
    i.set_defaults(func=cmd_import)

    ls = sub.add_parser('list', help='list gallery entries')
    ls.set_defaults(func=cmd_list)

    rm = sub.add_parser('remove', help='remove a gallery entry by --id or --name')
    rm.add_argument('--id', type=int, help='ID from `list`')
    rm.add_argument('--name', help='filename (e.g. 01-primera.jpg)')
    rm.add_argument('--keep-files', action='store_true',
                    help='remove template entry only; keep image + thumb')
    rm.set_defaults(func=cmd_remove)

    args = p.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
