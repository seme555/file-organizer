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