---
name: add-song
description: Add an original Teína song to the music page with its streaming links.
user-invocable: true
argument-hint: "<song-name> <year> [spotify-url] [youtube-url]"
x-claude:
  allowed-tools: Read, Edit, Bash, Grep
---

Add an original song to `templates/musica.html`.

::target claude
Request: $ARGUMENTS
::end

1. Read the song list in `templates/musica.html` and copy the structure of the newest entry.
2. Insert the song newest first, with the Spotify and YouTube links given. Fill the ES and EN branches.
3. Update the `MusicRecording` or track list in the page JSON-LD if the template has one.
4. The singles count appears in other copy (`zola.toml` description, `static/llms*.txt`, templates). Grep for it and update every hit.
5. `zola build`, then commit as `feat(music): ...` and push to `main`.
