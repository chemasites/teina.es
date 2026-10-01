---
name: build
description: Build the Teína site with Zola, as CI does, and fix or report errors.
user-invocable: true
x-claude:
  allowed-tools: Bash, Read, Edit
---

1. Run `zola check`, then `zola build`, from the repository root.
2. On a Tera error, read the file and line it names. Zola 0.23 uses Tera v2; see the template rules for syntax that changed.
3. Report the result in one line, plus each warning or fix made.
