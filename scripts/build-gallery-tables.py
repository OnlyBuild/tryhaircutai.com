#!/usr/bin/env python3
"""Build GitHub-compatible HTML gallery tables from hairstyle image folders.

Usage: python3 scripts/build-gallery-tables.py
Writes docs/gallery-female.md and docs/gallery-male.md snippets that get
pasted into README.md / README.zh-CN.md.
"""

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


def filename_to_style_name(stem: str) -> str:
    """a_line_bob -> A-Line Bob"""
    if stem in STEM_OVERRIDES:
        return STEM_OVERRIDES[stem]
    words = []
    for token in stem.split("_"):
        words.append(NAME_OVERRIDES.get(token, token.capitalize()))
    return " ".join(words)


def build_table(image_dir: Path, asset_prefix: str) -> str:
    images = sorted(p for p in image_dir.iterdir() if p.suffix == ".jpg")
    cells = []
    for img in images:
        name = filename_to_style_name(img.stem)
        cells.append(
            f'    <td align="center"><a href="https://tryhaircutai.com">'
            f'<img src="{asset_prefix}/{img.name}" width="{IMG_WIDTH}" '
            f'alt="{name} hairstyle AI try-on preview" /></a><br />'
            f"<sub>{name}</sub></td>"
        )
    rows = []
    for i in range(0, len(cells), PER_ROW):
        row_cells = cells[i : i + PER_ROW]
        # Pad the last row so the table stays aligned.
        row_cells += ["    <td></td>"] * (PER_ROW - len(row_cells))
        rows.append("  <tr>\n" + "\n".join(row_cells) + "\n  </tr>")
    return "<table>\n" + "\n".join(rows) + "\n</table>"


def main() -> None:
    GALLERY_DIR.mkdir(exist_ok=True)
    female = build_table(
        REPO_ROOT / "assets/hairstyles/female", "assets/hairstyles/female"
    )
    male = build_table(
        REPO_ROOT / "assets/hairstyles/male", "assets/hairstyles/male"
    )
    (GALLERY_DIR / "gallery-female.md").write_text(female + "\n")
    (GALLERY_DIR / "gallery-male.md").write_text(male + "\n")
    print(f"female: {female.count('<td align')} styles")
    print(f"male:   {male.count('<td align')} styles")


if __name__ == "__main__":
    main()
