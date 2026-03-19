---
name: add-song
description: Add a new original song to the Teína music page
user-invocable: true
argument-hint: "<song-name> <year> [spotify-url] [youtube-url]"
allowed-tools: Read, Edit, Bash, Grep
---

Add a new original song to the music page. Arguments: $ARGUMENTS

## Steps

1. Read `templates/musica.html` to understand the current song list structure
2. Add the new song entry in the correct chronological position (newest first)
3. If Spotify or YouTube URLs are provided, add the appropriate links
4. Update both Spanish and English content if the template has i18n sections
5. Run `zola build` to verify
