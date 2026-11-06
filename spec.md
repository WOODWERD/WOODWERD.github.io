# WOODWERD Toolkit Guides — spec

Project code **WG**. x0.0.1, 2026-11-06.

## 1. Brief
Drew, 2026-11-06: the reference for setting up a private GitHub repo "should just be in a WOODWERD info page (and not necessarily buried under one or the other)." Box Ctrl, Tool Ctrl and soon File Ctrl each sync to a person's own private repo. The step-by-step page lived on Box Ctrl's site, which made other tools' docs lean on Box Ctrl.

## 2. Rules
| ID | Rule |
| --- | --- |
| WG-R1 | The site lives at `woodwerd.github.io`, from the public repo `WOODWERD/WOODWERD.github.io`, chosen by Drew 2026-11-06. It is not a tool and isn't listed in All tools. |
| WG-R2 | A page goes here only when more than one tool needs it. It stays generic. What one tool writes, where its buttons are and its exact messages go in that tool's guide, which the page links to. |
| WG-R3 | Set up GitHub covers: why, how one repo serves several tools, which tools use it, what you need, a GitHub account, a private repo, a fine-grained token for that repo with Contents read and write only, connecting a tool, a read-only token for review-only phones, more devices, common fixes, words used, and privacy. |
| WG-R4 | Set up GitHub keeps the section anchors of the old Box Ctrl page where the section still exists (`why`, `how`, `need`, `account`, `repo`, `token`, `connect`, `more`, `fix`, `words`), so old links land in the right place. |
| WG-R5 | Box Ctrl's `github.html` stays as a pointer to this page, carrying the anchor across. Its Box Ctrl-only sections, `tool` and `daily`, go to Box Ctrl's guide. |
| WG-R6 | A tool joins the Which tools use it table when it is public and syncs, with a link to its guide's GitHub section. Unreleased tools are not listed. |
| WG-R7 | WOODWERD Digital Draft 2: toolkit strip, product header, content, footer mark; spec tokens in both themes; bundled fonts; three-state theme. As a docs surface it has no live status. No "You are here" in All tools, since the site isn't a tool. |
| WG-R8 | Links for reading go to `woodwerd.github.io` pages, never to repos, and never to a private repo. |
| WG-R9 | Plain pages. The only script is the theme switch and closing the All tools menu. No analytics and no network requests beyond the page's own files. |

## 3. Open questions
| # | Question | Default |
| --- | --- | --- |
| Q1 | The site's name. "Toolkit Guides" follows the strip's "WOODWERD Toolkit", and the toolkit's own name is an open decision in WOODWERD Digital. | Toolkit Guides until that decision is made |
| Q2 | Should All tools, in the six places it repeats, gain a link to the guides? | Not yet; the tools' own guides link here |

## 4. Log
- **2026-11-06** — x0.0.1 built, not committed. Set up GitHub rewritten from Box Ctrl's x0.1.4 page as a generic page. Box Ctrl x0.1.8 and Tool Ctrl x0.0.11 point to it.
