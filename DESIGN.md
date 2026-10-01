---
name: Teína
description: A festival lineup poster screenprinted in the colours of the band's butterfly logo.
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
    fontFamily: "Big Shoulders, Archivo, sans-serif"
    fontSize: "clamp(7.5rem, 25vw, 19rem)"
    fontWeight: 900
    lineHeight: 0.8
    letterSpacing: "-0.01em"
    fontVariation: "'opsz' 72"
  headline:
    fontFamily: "Big Shoulders, Archivo, sans-serif"
    fontSize: "clamp(4.5rem, 15vw, 13rem)"
    fontWeight: 900
    lineHeight: 0.92
    letterSpacing: "-0.01em"
    fontVariation: "'opsz' 72"
  title:
    fontFamily: "Big Shoulders, Archivo, sans-serif"
    fontSize: "clamp(3rem, 8vw, 6.5rem)"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: "-0.005em"
    fontVariation: "'opsz' 72"
  bill:
    fontFamily: "Big Shoulders, Archivo, sans-serif"
    fontSize: "clamp(1.7rem, 3.2vw, 3rem)"
    fontWeight: 800
    lineHeight: 0.95
  button:
    fontFamily: "Big Shoulders, Archivo, sans-serif"
    fontSize: "1.35rem"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "0.02em"
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
  circle: "50%"
spacing:
  gutter: "clamp(1rem, 4vw, 3rem)"
  max-width: "88rem"
  rule: "3px"
  section: "clamp(3rem, 8vw, 6.5rem)"
  section-head: "clamp(2rem, 4vw, 3rem)"
  poster-head-top: "clamp(2.5rem, 7vw, 5.5rem)"
  poster-head-bottom: "clamp(2rem, 5vw, 4rem)"
  row: "1.1rem"
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

**Creative North Star: "The Festival Cartel"**

Every page is a screenprinted festival poster on which Teína is the headliner. The band name and each page name sit at headliner scale, top left, in condensed black caps. Below them, names run in lineup rows separated by dots: the artists Teína shared a stage with, the bands in the repertoire, the occasions the band plays. Facts read like the strap under a poster headliner. Buttons are ticket stubs. The page itself is a flat field of one of the logo's colours, and sections change field the way a poster run changes paper.

The print is flat and physical. There are no gradients on surfaces, no shadows, no rounded cards and no blur. Structure comes from 3px ink rules, field changes and type scale. The one piece of theatre is the print pass: every headliner carries a second impression in a green ghost colour that lands out of register and settles a few pixels off, like a two-colour screenprint. Photography is real live and band photography, framed in a 3px ink border and cropped square-cornered.

The palette is pinned to the band's butterfly logo and was chosen by the band: plaster cream, sand, leaf green, fern, deep forest green and black ink. Bright inks (pink, lemon, cobalt) were rejected. There is one light theme and no dark mode. The rejected direction, recorded in the direction contract, is the dark full-bleed band hero with a centred logo.

**Key Characteristics:**

- Headliner type at poster scale (up to 19rem) in Big Shoulders Black, uppercase, line height 0.8.
- Lineup rows of names in condensed caps, dot separators drawn by CSS.
- Whole-page colour fields: each template sets one field on `<body>`, and sections switch field.
- 3px ink rules as the only structural device; no shadows, no radius.
- Ticket-stub buttons with notched ends and a dashed perforation.
- A misregistered second print pass on every headliner.
- Booking reachable in one tap on every page: header ticket, booking band, and a fixed dock on phones.

## Colors

Six flat inks from the butterfly logo: two warm paper tones, three greens and a green-black ink.

### Primary

- **Leaf Green** (leaf): the booking colour. Fills the booking band above the footer, the contact and tribute page fields, the leaf ticket, the CONTRATAR half of the phone dock, the video play button and text selection. On plaster it also sets the "+ 6 temas de Teína" line in the home lineup. Plaster on leaf measures 6.75:1.

### Secondary

- **Deep Forest** (forest): the night field. Used for the music page, the home "occasions" section and the 404 page. It is the ghost print colour on leaf fields and the hover fill of the play button. Plaster on forest measures 13.4:1.

### Tertiary

- **Fern** (fern): the second print pass only. It is the ghost colour on plaster, sand and forest fields. It never carries text that must be read (3.5:1 on plaster, 2.9:1 on sand).

### Neutral

- **Plaster Cream** (plaster): the default paper. Body background on every page, the field for home, media and legal, and the text colour on leaf and forest. `--paper` is an alias of it.
- **Warm Sand** (sand): the second paper. Field for the concerts and band pages, and for alternate sections (home live split, music promo, contact services, tribute area, media videos). Also the sand ticket that sits on leaf.
- **Black Ink** (ink): all text on paper fields, every rule and border, the default ticket fill, the phone dock background, focus outlines on paper. Ink on plaster measures 15.3:1.
- **Soft Ink** (ink-soft): the footer's bottom line (copyright and credits) only.

The lightbox scrim is `--ink` at 96% (`color-mix(in srgb, var(--ink) 96%, transparent)`); it sits under full-screen photos only.

### Named Rules

**The Logo Inks Rule.** Every colour comes from the six tokens in `:root`. No new hex values outside `:root`, no tints, no gradients on surfaces, no bright accents. The band pinned these colours to their logo.

**The Field Rule.** A field sets three things together: the background (`--field`), the text colour on it (`--on-field`) and the ghost print colour (`--ghost`). Plaster and sand carry ink text with a fern ghost; leaf carries plaster text with a forest ghost; forest carries plaster text with a fern ghost. Never set one without the other two.

**The Page Field Rule.** Each template declares one field on `<body>`, and the sticky header takes that field's colour. Home, media and legal are plaster; concerts and band are sand; tribute and contact are leaf; music and 404 are forest. Sections without a field fall back to the plaster body.

## Typography

**Display Font:** Big Shoulders (fallback Archivo, then sans-serif), self-hosted, Latin subset, weights 700 to 900, optical size axis fixed at 72.
**Body Font:** Archivo (fallback system-ui, then sans-serif), self-hosted, Latin subset, weights 400 to 800, width axis 100 to 120.

**Character:** Big Shoulders is a tall condensed poster face that fills a row edge to edge in caps; Archivo is a grotesque whose width axis lets labels widen (112 to 118) into a poster strap while body text stays at normal width. Only the display file is preloaded.

### Hierarchy

- **Display** (Big Shoulders 900, clamp(7.5rem, 25vw, 19rem), line height 0.8): the TEÍNA headliner on the home poster. One per site.
- **Headline** (Big Shoulders 900, clamp(4.5rem, 15vw, 13rem), line height 0.92): the page name in each page's poster head. The long variant for legal pages drops to clamp(3.4rem, 9vw, 8rem).
- **Title** (Big Shoulders 900, clamp(3rem, 8vw, 6.5rem), line height 1): section headings. The booking band title runs larger at clamp(3.5rem, 10vw, 9rem).
- **Bill** (Big Shoulders 800, line height 0.95, size set by context from about 1.5rem to 5rem): lineup rows of names. The home repertoire lineup steps down in three tiers (clamp(2.6rem, 5.4vw, 4.8rem), clamp(2rem, 3.9vw, 3.5rem), clamp(1.5rem, 2.8vw, 2.5rem)).
- **Row titles** (Big Shoulders 800 to 900): song titles, venues, member names, FAQ questions and contact values all use the display face in caps at 1.5rem to 7.5rem, line height 0.85 to 1.05.
- **Lede** (Archivo 400, clamp(1.125rem, 1.6vw, 1.375rem), line height 1.45, max 38rem): the paragraph under a headliner or title.
- **Body** (Archivo 400, 1.0625rem, line height 1.55): running text. Prose blocks cap at 40rem.
- **Label** (Archivo 700, width 112 to 118, 0.8rem to 1rem, letter spacing 0.05em to 0.08em, uppercase): straps, nav links, roles, years, badges, captions, footer links.

### Named Rules

**The Two Faces Rule.** Big Shoulders and Archivo only. Display type is always uppercase. No third face, no italic display.

**The Strap Rule.** Small text that labels something is Archivo bold, widened and tracked in caps. Small text that explains something is Archivo regular in sentence case. Do not mix the two in one line.

**The Numbers Rule.** Years and times use tabular figures; dates print the day in display type with the month as a label beside it.

## Layout

One centred column, max width 88rem, with a fluid side gutter of clamp(1rem, 4vw, 3rem). Sections are full-bleed bands of field colour; their content sits inside that column. Vertical rhythm is set by section padding of clamp(3rem, 8vw, 6.5rem), with a 3px ink rule between consecutive sections. Section heads (title plus lede) sit clamp(2rem, 4vw, 3rem) above their content.

The home first viewport is the poster: a 7:5 grid with the headliner, strap, lede, facts row and shared-stage lineup on the left and a bordered live photo plate on the right; below both, a bill strip with the next dates on the left and the box office (phone number and the CONTRATAR ticket) on the right. Inner pages open with a poster head: page name at headline scale, then a lede.

Lists are rows, not cards. Songs, concerts, FAQ entries, services and contact lines are rows divided by 3px rules. Media uses a CSS columns masonry (3 columns, min 18rem). Band members sit in a 3-column grid of 4:5 portraits.

Responsive behaviour, by observed breakpoint:

- 960px: nav links move into a full-screen drawer with display-size links.
- 900px: the home poster stacks to one column, photo below the name at 4:3.
- 860px: splits, booking band and services collapse (services to 2 columns, then 1 at 560px).
- 760px: lineup rows marked to stack print one name per line, without dots.
- 700px: concert rows reflow to date plus details; the header ticket hides and a fixed two-button dock (call and book) takes over at the bottom of the screen.
- 420px: the brand name hides beside the butterfly mark.

### Named Rules

**The One Tap Rule.** Every page offers booking in one tap: the header ticket on wide screens, the booking band above the footer, and the fixed dock on phones. Only one CONTRATAR shows in the header area on a phone.

## Elevation & Depth

The system is flat. There are no box shadows anywhere. Depth comes from print logic: a field colour change, a 3px ink rule, an ink border around a photo, and the ghost print pass behind each headliner. Overlays (the sticky header, the mobile drawer, the dock, the lightbox) sit on solid field or ink fills with a 3px ink rule at their edge, never a shadow or blur.

### Named Rules

**The Flat Print Rule.** Nothing floats. If a surface needs to separate from what is behind it, give it a field fill and a 3px ink rule.

## Shapes

Square corners everywhere (radius 0). The only round shape is the circular video play button. Borders are 3px solid ink for rules, photo frames and the header edge; 2px for small outlined labels (language switch, private badge, past-events toggle) and the footer's bottom line.

The signature silhouette is the ticket stub: a rectangle with a half-circle notch cut from the middle of each short end (radius 0.42em, drawn by a CSS mask) and a 2px dashed perforation before the icon stub. Toggles draw their plus and minus signs from straight bars, not glyphs.

## Components

### Buttons (ticket stubs)

Bold, tactile and printed.

- **Shape:** notched ticket stub, square corners, dashed perforation between label and arrow icon.
- **Default:** ink fill with plaster text, Big Shoulders 800 at 1.35rem in caps, padding 0.85em 1.4em 0.85em 1.5em.
- **Variants:** paper (plaster fill, ink text) for forest and leaf fields; sand (sand fill, ink text) on the leaf booking band and 404; leaf (leaf fill, plaster text) as a second action beside an ink ticket; small (1.05rem) in the header and concert rows.
- **Hover / Active:** lifts 3px and tilts -1.5deg over 0.35s on the ease-out curve; snaps flat on press. Focus is a 3px outline offset 3px, ink on paper fields and plaster on green fields.

### Text links and credit links

Underlined at 2px with a 0.18em offset, thickening to 3px on hover. Credit links are label-style caps with an arrow icon, used for secondary routes ("Todas las fotos y vídeos").

### Lineup bill

Names in condensed caps in a wrapping row, each preceded by a centred middle dot at 55% opacity. The list is pulled left by one dot width and clipped there, so a wrapped line never starts with a dot. Rows can stack one name per line under 760px.

### Rows (songs, concerts, FAQ, services, contact)

- **Song row:** title in display caps left, year as a tabular label right, 3px rule below.
- **Concert row:** day in display type (3.6rem) with month beside it and year as a label beneath, venue in display caps, time label, optional outlined badge, optional small ticket. Past concerts collapse behind a toggle and print at 60% opacity. Today's concert carries an ink badge that pulses.
- **FAQ row:** question in display caps with a bar-drawn plus that rotates 45deg when open.
- **Contact row:** label above a display-scale value (phone up to 7.5rem); hover underlines the value.

### Photo plates

Live and band photos sit in a 3px ink frame with square corners and `object-fit: cover`. On hover the photo inside scales to 1.03 or 1.04 over 0.6s; the frame stays still.

### Navigation

- **Header:** sticky, takes the page field colour, 3px ink rule below. Butterfly mark (a CSS mask over `currentColor`) with the name in Big Shoulders 900, label-style links, a language switch in a 2px outline box that fills ink on hover, and a small ink ticket.
- **States:** hover and current page draw a 3px underline bar under the link.
- **Mobile:** under 960px a three-bar toggle opens a full-screen drawer that wipes down with a clip-path; links print at clamp(3rem, 15vw, 5rem) in display caps; the current page is underlined.

### Phone dock

Under 700px a fixed bar splits in two: Call (plaster fill, ink text) and Book (leaf fill, plaster text) over an ink frame, each 3.5rem tall in display caps. On the contact page the second button becomes Email.

### Signature: the print pass

Every headliner is two stacked spans: the ink pass and an `aria-hidden` ghost pass in the field's ghost colour. The ghost starts 0.16em right and 0.08em up, fades in, and settles at 0.035em right and 0.03em down over 1.1s after a 0.15s delay. Reduced motion shows the settled state.

### Gallery (structural constraint)

The `#galeria` section in `templates/media.html` is parsed by `scripts/media.py` and `scripts/sitemap.py` with exact-text regular expressions. Keep `<section class="section section-alt" id="galeria">`, the `<div class="gallery gallery-large">` wrapper, and each entry's `<a ... class="gallery-item" data-lightbox>` with its `<picture>`, `<source>` and `<img>` lines, attribute order and indentation exactly as they are. The section has no inner `.wrap`; its width and gutter come from the `#galeria` rule. Style it from CSS, never by changing that markup.

## Do's and Don'ts

### Do:

- **Do** take every colour from the six `:root` tokens and set a whole field (`field--plaster`, `field--sand`, `field--leaf`, `field--forest`) rather than a lone background.
- **Do** set page and section names in Big Shoulders 900 caps at headliner or title scale, with the ghost print pass on page headliners.
- **Do** write lists of names as `.bill` rows and let CSS draw the dots.
- **Do** use ticket stubs for every button, picking the variant that contrasts with the field.
- **Do** separate sections and rows with 3px ink rules, and frame photos with a 3px ink border.
- **Do** keep booking one tap away on every page, in both languages.
- **Do** check layouts at 390px and 1440px.

### Don't:

- **Don't** add bright inks (pink, lemon, cobalt) or any hex value outside `:root`.
- **Don't** add a dark mode or a theme toggle.
- **Don't** add a third typeface or set display type in lowercase.
- **Don't** type dot separators between names; the bill draws and clips them.
- **Don't** add box shadows, blur, gradients on surfaces or rounded corners (the play button is the only circle).
- **Don't** build a dark full-bleed band hero with a centred logo.
- **Don't** change the `#galeria` gallery markup in `templates/media.html`; the media and sitemap scripts parse it as text.
- **Don't** use fern for text that must be read.
