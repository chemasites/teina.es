---
name: add-concert
description: Add a new concert/event to the Teína website concerts page
user-invocable: true
argument-hint: "<date> <venue> <city> [ticket-url]"
allowed-tools: Read, Edit, Bash, Grep
---

Add a new concert event to the website. Arguments: $ARGUMENTS

## Steps

1. Read `templates/conciertos.html` to find the existing concert list and JSON-LD events
2. Parse the arguments: date, venue name, city, and optional ticket URL
3. Add the new event HTML block in chronological order among existing events, following the exact same HTML structure as other events
4. Add the corresponding MusicEvent JSON-LD structured data entry
5. If a ticket URL is provided, add a link button; otherwise use the standard contact CTA
6. Make sure the event is added in both the visible HTML list AND the JSON-LD script block
7. Run `zola build` to verify the site compiles

## HTML structure reference (match this exactly)

Look at existing events in `templates/conciertos.html` for the exact class names, date format (`DD mon YYYY`), and structure. Each event needs:
- The visual event card in the events list section
- A MusicEvent JSON-LD entry in the structured data script

## Date format
- Display: `28 mar 2026` (lowercase Spanish month abbreviation)
- JSON-LD: `2026-03-28T21:00:00+02:00` (ISO 8601 with timezone)
