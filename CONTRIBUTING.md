# Contributing to TryHaircutAI

Thanks for your interest in contributing!

The highest-value contributions, in order:

1. **New styles for the library** — see the contribution checklist in [`PROJECT_PLAN.md` §3](./PROJECT_PLAN.md). Every style needs a reference render and a tested prompt fragment.
2. **Prompt tuning reports** — if a style renders poorly on certain face shapes or lighting, open an issue with the style name and a description of the failure (never upload your photo to the issue).
3. **Docs and translations** — README locale variants and blog content.

## How to submit

1. Fork, create a branch (`style/lob-reference` or `docs/zh-readme`)
2. If you add styles, run `python3 scripts/build-gallery-tables.py` and commit the regenerated tables
3. Open a pull request describing **which style** changed and **how the prompt was tested**

## Ground rules

- Reference renders must be images you own or generated yourself — no scraped salon photos, no identifiable third parties
- Keep filenames `snake_case` and consistent with existing salon terminology
- Do not commit real API keys, account IDs, or user photos
- Be kind in issues and reviews

## Reporting bugs in the hosted product

For bugs in the hosted app at [tryhaircutai.com](https://tryhaircutai.com), use the [contact form](https://tryhaircutai.com/contact) — this repository tracks the style library and site copy. Security issues go to [`SECURITY.md`](./SECURITY.md) instead.
