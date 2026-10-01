---
name: Teína
description: A modern band site in the colours of the butterfly logo, led by the real logo and live photos.
colors:
  plaster: "#f4ead9"
  sand: "#e6d2b3"
  leaf: "#1f5b37"
  fern: "#3f8a54"
  forest: "#0f2619"
  ink: "#131612"
  ink-soft: "#3d3a33"
typography:
  display:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "clamp(3.2rem, 9vw, 7rem)"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "-0.03em"
    fontVariation: "'wdth' 112"
  headline:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "clamp(2.8rem, 7.5vw, 6rem)"
    fontWeight: 800
    lineHeight: 1.02
    letterSpacing: "-0.03em"
    fontVariation: "'wdth' 112"
  title:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "clamp(2.1rem, 4.4vw, 3.8rem)"
    fontWeight: 800
    lineHeight: 1.04
    letterSpacing: "-0.02em"
    fontVariation: "'wdth' 112"
  row-title:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "clamp(1.2rem, 2vw, 1.7rem)"
    fontWeight: 800
    lineHeight: 1.15
  tag:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "clamp(1.05rem, 1.7vw, 1.35rem)"
    fontWeight: 700
    lineHeight: 1.2
    fontVariation: "'wdth' 104"
  button:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "1.05rem"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "0"
  lede:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "clamp(1.125rem, 1.6vw, 1.375rem)"
    fontWeight: 400
    lineHeight: 1.45
    fontVariation: "'wdth' 100"
  body:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.55
    fontVariation: "'wdth' 100"
  label:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "clamp(0.85rem, 1.1vw, 1rem)"
    fontWeight: 700
    letterSpacing: "0.06em"
    fontVariation: "'wdth' 118"
  label-nav:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "0.95rem"
    fontWeight: 700
    letterSpacing: "0.05em"
    fontVariation: "'wdth' 112"
rounded:
  none: "0"
  pill: "999px"
  circle: "50%"
spacing:
  gutter: "clamp(1rem, 4vw, 3rem)"
  max-width: "88rem"
  rule: "3px"
  section: "clamp(3rem, 8vw, 6.5rem)"
  section-head: "clamp(2rem, 4vw, 3rem)"
  page-head-top: "clamp(2.5rem, 7vw, 5.5rem)"
  page-head-bottom: "clamp(2rem, 5vw, 4rem)"
  hero-gap: "clamp(1.5rem, 4vw, 4rem)"
  row: "1.1rem"
  tag-gap: "0.5rem"
components:
  ticket:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.plaster}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: "0.85em 1.4em 0.85em 1.5em"
  ticket-paper:
    backgroundColor: "{colors.plaster}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: "0.85em 1.4em 0.85em 1.5em"
  ticket-sand:
    backgroundColor: "{colors.sand}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: "0.85em 1.4em 0.85em 1.5em"
  ticket-leaf:
    backgroundColor: "{colors.leaf}"
    textColor: "{colors.plaster}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: "0.85em 1.4em 0.85em 1.5em"
  ticket-sm:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.plaster}"
    rounded: "{rounded.none}"
    padding: "0.7em 1em 0.7em 1.1em"
  tag:
    textColor: "{colors.ink}"
    typography: "{typography.tag}"
    rounded: "{rounded.pill}"
    padding: "0.4em 0.95em"
  tag-on-dark:
    textColor: "{colors.plaster}"
    typography: "{typography.tag}"
    rounded: "{rounded.pill}"
    padding: "0.4em 0.95em"
  hero-logo:
    width: "clamp(8rem, 13vw, 11.5rem)"
  lang-switch:
    textColor: "{colors.ink}"
    typography: "{typography.label-nav}"
    rounded: "{rounded.none}"
    padding: "0.35rem 0.5rem"
  lang-switch-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.plaster}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.label-nav}"
    padding: "0.3rem 0"
  event-badge:
    textColor: "{colors.ink}"
    typography: "{typography.label-nav}"
    rounded: "{rounded.none}"
    padding: "0.35em 0.7em"
  event-badge-today:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.plaster}"
    rounded: "{rounded.none}"
    padding: "0.3em 0.75em"
  dock-call:
    backgroundColor: "{colors.plaster}"
    textColor: "{colors.ink}"
    height: "3.5rem"
  dock-book:
    backgroundColor: "{colors.leaf}"
    textColor: "{colors.plaster}"
    height: "3.5rem"
  play-button:
    backgroundColor: "{colors.leaf}"
    textColor: "{colors.plaster}"
    rounded: "{rounded.circle}"
    size: "5.5rem"
  play-button-hover:
    backgroundColor: "{colors.forest}"
---

# Design System: Teína

## Overview

**Creative North Star: "The Real Band"**

The site presents Teína as a working band. The real logo and a real photo of all six members share the home page's first screen. Below them, the copy is plain modern type, and booking is never more than one tap away. Pages are flat fields of the logo's colours: plaster cream, sand, leaf green and deep forest green, with black ink for text and rules. Headings are Archivo ExtraBold in sentence case. Lists of names are outlined pill tags. Buttons are ticket stubs, the one playful shape in an otherwise plain system.

The look is flat and ruled. There are no shadows, no gradients on surfaces and no blur. Structure comes from 3px ink rules, field colour changes and type weight. Photography carries the energy: live and band photos are framed in a 3px ink border with square corners, except the unframed home hero photo. Motion is small and functional: tickets lift and tilt on hover, photos zoom slightly inside their frames, the mobile menu wipes down.

The palette is pinned to the butterfly logo and was chosen by the band. There is one light theme and no dark mode. The band rejected the earlier festival-poster direction (condensed uppercase display type, name rows separated by dots, an offset second print layer) because it read as a bullfight poster. That look is retired.

**Key Characteristics:**

- The band-supplied logo (butterfly plus script wordmark) appears as an image, never redrawn in type.
- The home hero pairs the logo and booking copy with a large, unframed band photo.
- Archivo is the only typeface; headings are ExtraBold in sentence case.
- Lists of names are outlined pill tags that wrap freely.
- Whole-page colour fields: each template sets one field on `<body>`, and sections switch field.
- 3px ink rules as the structural device; no shadows.
- Ticket-stub buttons with notched ends and a dashed perforation.
- Booking reachable in one tap on every page: header ticket, booking band, and a fixed dock on phones.

## Colors

Flat colours from the butterfly logo: two warm paper tones, greens, and a green-black ink.

### Primary

- **Leaf Green** (leaf): the booking colour. It fills the booking band above the footer, the tribute and contact page fields, the leaf ticket, the Book half of the phone dock, the video play button and text selection. On plaster it also sets the "+ 6 temas de Teína" line in the home lineup. Plaster on leaf measures 6.75:1.

### Secondary

- **Deep Forest** (forest): the dark field. Used for the music page, the home occasions section and the 404 page, and as the hover fill of the play button. Plaster on forest measures 13.4:1.

### Tertiary

- **Fern** (fern): declared in `:root` as part of the logo palette. No rendered element uses it since the offset print layer was removed. It measures 3.5:1 on plaster, so it is not a text colour.

### Neutral

- **Plaster Cream** (plaster): the default paper and the `theme-color`. It is the body background on every page, the field for home, media and legal, and the text colour on leaf and forest. `--paper` is an alias of it.
- **Warm Sand** (sand): the second paper. It is the field for the concerts and band pages and for alternating sections: home live, music promo, contact services, tribute area and media videos. It also fills the sand ticket that sits on leaf.
- **Black Ink** (ink): all text on paper fields, every rule and border, the default ticket fill, the phone dock frame and focus outlines on paper. The lightbox scrim is ink at 96% (`color-mix`). Ink on plaster measures 15.3:1.
- **Soft Ink** (ink-soft): secondary text. It sets the shared-stage sentence in the home hero (the artist names inside it stay full ink) and the footer's bottom line. It measures 9.5:1 on plaster.

### Named Rules

**The Logo Inks Rule.** Every colour comes from the tokens in `:root`, or from `color-mix` of them. No new hex values outside `:root`, no gradients on surfaces, no bright accents (pink, lemon, cobalt). The band pinned these colours to their logo.

**The Field Rule.** A field sets the background (`--field`) and the text colour on it (`--on-field`) together. Plaster and sand carry ink text; leaf and forest carry plaster text. Never set one without the other.

**The Page Field Rule.** Each template declares one field on `<body>`, and the sticky header takes that field's colour. Home, media and legal are plaster; concerts and band are sand; tribute and contact are leaf; music and 404 are forest. Sections without a field fall back to the plaster body.

## Typography

**Font:** Archivo (fallback system-ui, then sans-serif). It is self-hosted as one Latin subset file, weights 400 to 800 and width axis 100 to 120, and it is preloaded.

**Character:** Archivo is a sturdy grotesque. Headings use ExtraBold slightly widened (width 112) with tight negative tracking, so they read confident without shouting. Small labels widen further (112 to 118) and go uppercase with open tracking. Body text stays at normal width and regular weight.

### Hierarchy

- **Display** (800, clamp(3.2rem, 9vw, 7rem), line height 1, tracking -0.03em): the 404 page headline.
- **Headline** (800, clamp(2.8rem, 7.5vw, 6rem), line height 1.02): the page name in each inner page's head. Long page names (tribute, media, legal) drop to clamp(2.4rem, 5.6vw, 4.8rem).
- **Title** (800, clamp(2.1rem, 4.4vw, 3.8rem), line height 1.04, tracking -0.02em): section headings. The booking band title runs at clamp(2.6rem, 6vw, 5.2rem).
- **Row title** (800, about 1.15rem to 1.7rem, line height 1.05 to 1.25): song titles, venues, member names, FAQ questions and service names. The music tracklist runs larger, at clamp(1.6rem, 4vw, 3rem). Contact values (phone and email) reach clamp(2rem, 6vw, 4.6rem).
- **Tag** (700, width 104, clamp(1rem, 1.6vw, 1.25rem) to clamp(1.15rem, 2vw, 1.6rem) by context, line height 1.2): names inside pill tags.
- **Lede** (400, clamp(1.125rem, 1.6vw, 1.375rem), line height 1.45, max 38rem): the paragraph under a headline or title.
- **Body** (400, 1.0625rem, line height 1.55): running text. Prose blocks cap at 40rem.
- **Label** (700, width 112 to 118, 0.8rem to 1rem, tracking 0.05em to 0.08em, uppercase): straps, nav links, roles, years, badges, captions, credit links and footer links.
- **Numbers** (800): date days (2rem on the home strip, 2.6rem on the concert list) and the phone number (1.6rem in the hero, up to 3rem on the booking band).

### Named Rules

**The One Face Rule.** Archivo only. No display face, no condensed face, no italic headings.

**The Sentence Case Rule.** Headings, names and button labels are in sentence case. Uppercase is reserved for small tracked labels at 1rem or less. The mobile nav drawer is the one exception in the current build.

**The Numbers Rule.** Years and times use tabular figures. Dates print the day in ExtraBold, with the month as a label beside it.

## Layout

The layout is one centred column, max width 88rem, with a fluid side gutter of clamp(1rem, 4vw, 3rem). Sections are full-bleed bands of field colour, and their content sits inside that column. Section padding is clamp(3rem, 8vw, 6.5rem), with a 3px ink rule between consecutive sections. Section heads (title plus lede) sit clamp(2rem, 4vw, 3rem) above their content.

The home first viewport is a two-column grid (5fr text, 7fr photo, gap clamp(1.5rem, 4vw, 4rem), vertically centred), followed by a "Próximos conciertos" block under a 3px rule: a heading with a link to all dates, then up to six date cards (2px ink border, dashed for private events) with the day, month, place, and time, "Evento privado" or "Entradas a la venta". Six columns on desktop, three under 1100px, two under 560px; the card fills with ink on hover.

- **Left column, left-aligned:** the h1 holds the logo image (clamp(8rem, 13vw, 11.5rem) wide) above the uppercase strap "Banda murciana" ("Band from Murcia, Spain" in English). Below it are the description lede (max 34rem), the shared-stage sentence in soft ink (max 34rem), and the box office: the Contrata a Teína ticket followed by the phone number.
- **Right column:** the band photo with no frame, height min(68vh, 44rem) (at least 20rem), `object-fit: cover` at focal point 50% 30%.

Inner pages open with a page head: the page name at headline size, then a lede.

Lists of records are rows divided by 3px rules: songs, concerts, FAQ entries, services and contact lines. Lists of names (repertoire artists, shared-stage artists, towns, occasions) are wrapping pill tags with a 0.5rem gap. The home repertoire tags are centred under a centred section head. Media uses a CSS columns masonry (3 columns, min 18rem). Band members sit in a 3-column grid of 4:5 portraits.

Responsive behaviour, by observed breakpoint:

- 960px: nav links move into a full-screen drawer with large ExtraBold links.
- 900px: the box office aligns left.
- 860px: the home hero stacks with the photo first at 4:3 and the logo, text and box office centred below it (logo 7.5rem). Splits and the booking band collapse to one column; services go to 2 columns (1 at 560px).
- 800px: the home live split and the members grid collapse (members to 2 columns).
- 700px: concert rows reflow to date plus details; the header ticket hides and a fixed two-button dock (call and book) appears at the bottom of the screen.
- 420px: the brand name hides beside the butterfly mark.

### Named Rules

**The One Tap Rule.** Every page offers booking in one tap: the header ticket on wide screens, the booking band above the footer, and the fixed dock on phones. A phone shows only one Contratar at a time.

**The Faces First Rule.** The home photo is cropped around the faces (focal point 50% 30%), so all six members stay visible in both the tall desktop crop and the 4:3 phone crop.

## Elevation & Depth

The system is flat. There are no box shadows anywhere. Depth comes from a field colour change, a 3px ink rule or an ink border around a photo. Overlays (the sticky header, the mobile drawer, the dock, the lightbox) sit on solid field or ink fills with a 3px ink rule at their edge. The lightbox scrim is ink at 96%, without blur.

### Named Rules

**The Flat Rule.** Nothing floats. If a surface needs to separate from what is behind it, give it a field fill and a 3px ink rule.

## Shapes

The system has three shapes:

- **Square corners** (radius 0) on everything structural: photos, rows, the header, badges, the language switch and the lightbox buttons.
- **Pills** (radius 999px) for name tags only, outlined in 2px `currentColor` with no fill.
- **A circle** for the video play button only.

Borders are 3px solid ink for rules, photo frames and the header edge. Small outlined elements (tags, language switch, private badge, past-events toggle) and the footer's bottom line use 2px.

The ticket stub is a rectangle with a half-circle notch cut from the middle of each short end (radius 0.42em, drawn by a CSS mask). A 2px dashed perforation separates the label from the arrow icon. The plus and minus signs on toggles are drawn from straight bars, not glyphs.

## Components

### Buttons (ticket stubs)

Friendly, tactile and plain.

- **Shape:** notched ticket stub, square corners, dashed perforation between the label and the arrow icon.
- **Default:** ink fill with plaster text, Archivo 800 at 1.05rem in sentence case, padding 0.85em 1.4em 0.85em 1.5em.
- **Variants:**
  - Paper (plaster fill, ink text): for forest and leaf fields.
  - Sand (sand fill, ink text): on the leaf booking band and the 404 page.
  - Leaf (leaf fill, plaster text): a second action beside an ink ticket.
  - Small (0.92rem): in the header. Concert-row tickets are 1.05rem.
- **Hover / Active:** lifts 3px and tilts -1.5deg over 0.35s on the ease-out curve, then snaps flat on press. Focus is a 3px outline offset by 3px: ink on paper fields, plaster on green fields.

### Name tags

Wrapping lists of outlined pills, used for the repertoire artists, the bands Teína shared a stage with, towns and occasions.

- **Style:** no fill, 2px `currentColor` outline, radius 999px, padding 0.4em 0.95em, Archivo 700 at width 104, no wrapping inside a tag.
- **Colour:** they take the field's text colour, so they are ink on paper fields and plaster on forest and leaf.
- **State:** static. Tags are not links and have no hover.

### Text links and credit links

Underlined at 2px with a 0.18em offset, thickening to 3px on hover. Credit links are uppercase labels with an arrow icon, used for secondary routes ("Todas las fotos y vídeos").

### Rows (songs, concerts, FAQ, services, contact)

- **Song row:** ExtraBold title on the left, year as a tabular label on the right, 3px rule below.
- **Concert row:** the day in ExtraBold (2.6rem) with the month beside it and the year as a label beneath. The venue is a row title, followed by a time label, an optional outlined badge and an optional small ticket. Past concerts collapse behind a toggle and show at 60% opacity. Today's concert carries an ink badge that pulses.
- **FAQ row:** the question as a row title, with a bar-drawn plus that rotates 45deg when open.
- **Contact row:** a label above a large ExtraBold value. Hover underlines the value.

### Photo plates

Live and band photos sit in a 3px ink frame with square corners and `object-fit: cover`. On hover, the photo inside scales to 1.03 or 1.04 over 0.6s while the frame stays still. The home hero photo is the exception: it has no frame and does not zoom.

### Navigation

- **Header:** sticky, in the page field colour, with a 3px ink rule below. It holds the butterfly mark (a CSS mask over `currentColor`) with "Teína" in Archivo 800 at 1.3rem, uppercase label links, a language switch in a 2px outline box that fills with ink on hover, and a small ink ticket.
- **States:** on hover and on the current page, a 3px bar underlines the link.
- **Mobile:** under 960px, a three-bar toggle opens a full-screen drawer that wipes down with a clip-path. Links show at clamp(2rem, 9vw, 3rem) in ExtraBold, and the current page is underlined. They are in sentence case like every other heading.

### Phone dock

Under 700px, a fixed bar splits in two over an ink frame: Call (plaster fill, ink text) and Book (leaf fill, plaster text). Each half is 3.5rem tall, in Archivo 800 at 1.1rem. On the contact page, the second button becomes Email.

### Signature: logo and photo hero

The home h1 contains the band-supplied logo image (`static/imgs/teina-logo-trim.webp` with a PNG fallback, alt "Teína", trimmed from `teina-logo.png`) above the strap "Banda murciana". It heads the text column beside the unframed band photo; under 860px the photo comes first and the logo sits centred under it. Keep the logo as an image: its green butterfly and script wordmark are the identity, and type does not stand in for it.

### Gallery (structural constraint)

The `#galeria` section in `templates/media.html` is parsed by `scripts/media.py` and `scripts/sitemap.py` with exact-text regular expressions. Keep these lines exactly as they are, with the same attribute order and indentation:

- `<section class="section section-alt" id="galeria">`
- the `<div class="gallery gallery-large">` wrapper
- each entry's `<a ... class="gallery-item" data-lightbox>` with its `<picture>`, `<source>` and `<img>` lines

The section has no inner `.wrap`; its width and gutter come from the `#galeria` rule. Style it from CSS, never by changing that markup.

## Do's and Don'ts

### Do:

- **Do** take every colour from the `:root` tokens and set a whole field (`field--plaster`, `field--sand`, `field--leaf`, `field--forest`) rather than a lone background.
- **Do** set headings in Archivo 800 at width 112 in sentence case, with negative tracking.
- **Do** show lists of names as outlined pill tags.
- **Do** use ticket stubs for every button, picking the variant that contrasts with the field.
- **Do** separate sections and rows with 3px ink rules, and frame photos with a 3px ink border (the home hero photo is the one unframed photo).
- **Do** show the logo as the band-supplied image.
- **Do** keep booking one tap away on every page, in both languages.
- **Do** check layouts at 390px and 1440px.

### Don't:

- **Don't** bring back the poster look: condensed or uppercase display headings, dot-separated name rows, or an offset second print layer. The band read it as a bullfight poster.
- **Don't** add bright inks (pink, lemon, cobalt) or any hex value outside `:root`.
- **Don't** add a dark mode or a theme toggle.
- **Don't** add a second typeface.
- **Don't** add box shadows, blur or gradients on surfaces. Don't round anything except name tags (pill) and the play button (circle).
- **Don't** set the band name in type where the logo image belongs.
- **Don't** change the `#galeria` gallery markup in `templates/media.html`; the media and sitemap scripts parse it as text.
- **Don't** use fern for text.
