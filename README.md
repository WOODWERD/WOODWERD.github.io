# WOODWERD Toolkit Guides

How-tos shared by every WOODWERD tool, at [woodwerd.github.io](https://woodwerd.github.io/).

- [Set up GitHub](https://woodwerd.github.io/github.html): one private repo and one fine-grained token for the tools that sync.

Each tool keeps its own user guide on its own site. A page belongs here only when more than one tool needs it, and it stays generic: what a single tool writes or where its buttons are goes in that tool's guide.

## Working on it

The pages are plain files that GitHub Pages publishes from `main` as they are. The strip, theme switch and footer are shared, so edit `tools/*.html` and run:

```
python3 tools/build.py
```

Serve locally with `python3 -m http.server 8151`. Every committed version adds an entry to [CHANGELOG.md](CHANGELOG.md).

MIT licence. Inter and JetBrains Mono are bundled under the SIL Open Font License, in `fonts/`.
