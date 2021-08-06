#!/usr/bin/env python3
"""Organize files in a folder into category subfolders."""

from __future__ import annotations

import argparse
import logging
import shutil
from pathlib import Path

CATEGORIES = {
    "images": {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".svg"},
    "documents": {".pdf", ".doc", ".docx", ".txt", ".md", ".rtf", ".odt"},
    "spreadsheets": {".csv", ".xls", ".xlsx", ".ods"},
    "archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "code": {".py", ".js", ".ts", ".html", ".css", ".json", ".yml", ".yaml"},
}


def setup_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


def category_for(path: Path) -> str:
    ext = path.suffix.lower()
    for name, extensions in CATEGORIES.items():
        if ext in extensions:
            return name
    return "other"


def unique_destination(folder: Path, filename: str) -> Path:
    candidate = folder / filename
    if not candidate.exists():
        return candidate
    stem = Path(filename).stem
    suffix = Path(filename).suffix
    index = 1
    while True:
        candidate = folder / f"{stem}_{index}{suffix}"
        if not candidate.exists():
            return candidate
        index += 1


def organize(target: Path, dry_run: bool = True) -> dict[str, int]:
    counts: dict[str, int] = {}
    for item in sorted(target.iterdir()):
        if item.is_dir() or item.name.startswith("."):
            continue
        category = category_for(item)
        destination_dir = target / category
        destination = unique_destination(destination_dir, item.name)