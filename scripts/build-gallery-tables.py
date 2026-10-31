#!/usr/bin/env python3
"""Build GitHub-compatible HTML gallery tables from hairstyle image folders.

Usage: python3 scripts/build-gallery-tables.py [locale ...]

Locales: en (default, all). Writes docs/gallery-{female,male}[-{locale}].md
snippets (en keeps the legacy unsuffixed filename) that get injected into the
README files. Style captions stay in English — salon terminology (bob, pixie,
undercut) is borrowed as-is across these markets — while the alt text uses
each locale's native search keywords.
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GALLERY_DIR = REPO_ROOT / "docs"

# Whole filenames that need a human-friendly rewrite.
STEM_OVERRIDES = {"a_line_bob": "A-Line Bob"}

# Filename tokens that need a human-friendly rewrite (title case is wrong).
NAME_OVERRIDES = {
    "a_line": "A-Line",
    "ombre": "Ombré",
    "lob": "LOB",
    "updo": "Updo",
    "updos": "Updos",
    "ai": "AI",
}

PER_ROW = 5
IMG_WIDTH = 150

# Alt-text templates per locale. {name} is the style caption. The templates
# front-load each market's native try-on keywords for image search.
ALT_TEMPLATES = {
    "en": "{name} hairstyle AI try-on preview",
    "it": "Anteprima prova taglio capelli con IA: {name}",
    "es": "Vista previa del probador virtual de peinados con IA: {name}",
    "pt": "Prévia do provador virtual de penteados com IA: {name}",
    "fr": "Aperçu essayage virtuel de coiffure IA : {name}",
}


def filename_to_style_name(stem: str) -> str:
    """a_line_bob -> A-Line Bob"""
    if stem in STEM_OVERRIDES:
        return STEM_OVERRIDES[stem]
    words = []
    for token in stem.split("_"):
        words.append(NAME_OVERRIDES.get(token, token.capitalize()))
    return " ".join(words)


def build_table(image_dir: Path, asset_prefix: str, alt_template: str) -> str:
    images = sorted(p for p in image_dir.iterdir() if p.suffix == ".jpg")
    cells = []
    for img in images:
        name = filename_to_style_name(img.stem)
        alt = alt_template.format(name=name)
        cells.append(
            f'    <td align="center"><a href="https://tryhaircutai.com">'
            f'<img src="{asset_prefix}/{img.name}" width="{IMG_WIDTH}" '
            f'alt="{alt}" /></a><br />'
            f"<sub>{name}</sub></td>"
        )
    rows = []
    for i in range(0, len(cells), PER_ROW):
        row_cells = cells[i : i + PER_ROW]
        # Pad the last row so the table stays aligned.
        row_cells += ["    <td></td>"] * (PER_ROW - len(row_cells))
        rows.append("  <tr>\n" + "\n".join(row_cells) + "\n  </tr>")
    return "<table>\n" + "\n".join(rows) + "\n</table>"


def build_locale(locale: str) -> None:
    suffix = "" if locale == "en" else f".{locale}"
    template = ALT_TEMPLATES[locale]
    for gender in ("female", "male"):
        table = build_table(
            REPO_ROOT / f"assets/hairstyles/{gender}",
            f"assets/hairstyles/{gender}",
            template,
        )
        (GALLERY_DIR / f"gallery-{gender}{suffix}.md").write_text(table + "\n")
        print(f"{locale} {gender}: {table.count('<td align')} styles")


def main() -> None:
    GALLERY_DIR.mkdir(exist_ok=True)
    locales = sys.argv[1:] or list(ALT_TEMPLATES)
    for locale in locales:
        if locale not in ALT_TEMPLATES:
            raise SystemExit(f"unknown locale: {locale} (known: {list(ALT_TEMPLATES)})")
        build_locale(locale)


if __name__ == "__main__":
    main()
