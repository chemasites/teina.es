# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Primary: people deciding whether to hire Teína for an event. Town hall culture officers planning fiestas patronales, festival organizers, couples planning a wedding, and companies planning a private or corporate party, mostly in the Region of Murcia and bordering provinces. They arrive from search or a recommendation, often on a phone, and need to judge quickly whether the band fits their event, then get a date and terms.

Secondary: fans and locals who want upcoming concert dates, tickets, songs, and videos.

## Product Purpose

The site turns interest into bookings. Success is a booker calling 661 892 704 or emailing teinaband@gmail.com with a date, a town, and an event type. Secondary success: fans find the next concert and its ticket link, and stream the originals.

## Positioning

Teína sells a live show first: a two-hour set of reinterpreted Spanish and international indie pop rock hits, played by six musicians with a saxophone in the line-up. Six original singles (2017 to 2025) prove they are a real band with their own sound, not a jukebox. They have shared stages with Revolver, Second, Álvaro de Luna, Loquillo, Danza Invisible, and Efecto Mariposa.

## Operating Context

- Bilingual: Spanish default at `/`, English at `/en/`. Both versions carry the same facts.
- Booking happens off-site, by phone or email. There is no form backend and no payment.
- Concerts come from `data/concerts.toml` (managed with `scripts/concert.py`); past events collapse client-side; private events show a badge and no venue details.
- The site is updated through short requests to a Telegram bot, so content structures must stay data-driven and script-friendly (`scripts/concert.py`, `scripts/media.py`, `scripts/sitemap.py`).
- Search matters: local SEO for "banda tributo indie pop rock Murcia", JSON-LD (MusicGroup with `@id /#band`, MusicEvent, FAQPage, VideoObject), image and video sitemap, `llms.txt`.

## Capabilities and Constraints

- Zola 0.23 static site, Tera v2 templates, one Sass stylesheet, minimal vanilla JS. Hosted on GitHub Pages from `main`.
- Pages: home, conciertos, musica, tributo, banda, media, contacto, legal, 404. Keeping current URLs avoids SEO loss; the user did not make them binding.
- Copy may be rewritten. Facts may not change: members and roles, song titles and years, artists shared stage with, area served, contact details, set length.
- Theme: the user did not require light and dark; one strong theme is allowed.

## Brand Commitments

- Name: Teína, with the accent on the i.
- The butterfly mark (`static/imgs/teina-logo.png`, `static/imgs/mariposa-teina.jpg`) stays as the brand identity.

## Evidence on Hand

- Band and live photos: `static/banda/` (six member portraits), `static/media/large/` and `thumbs/` (53 gallery photos), `static/media/hero-*`, `static/conciertos/conciertos-25.*`.
- Two YouTube videos: promo video (XDiUv8ba55I) and "Sentimiento Arrocero (Himno oficial Ciudad Calasparra)" (_ue01WuY4bQ).
- Six singles: A contratiempo (2025), Sentimiento arrocero (2025), Volver a empezar (2024), Quiero (2023), Salvaje (2019), Calavera (2017). Spotify artist 3DNeaFbVbrX0Z23VLr8J2J.
- FAQ in `data/faq.toml`. Instagram @teinaband, YouTube @teina8932.
- No testimonials, press quotes, audience numbers, or prices exist. Do not invent them.

## Product Principles

1. Booking is one tap away on every page, in both languages.
2. Show the live energy with real photos and video before describing it.
3. Facts and structured data stay true and in sync with what the visitor sees.
4. Content stays data-driven so a short bot request can update it safely.
5. Fast on a phone over mobile data.
