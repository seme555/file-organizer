# File Organizer

A small Python utility that groups loose files into category folders
(images, documents, spreadsheets, archives, code, other).

## Features

- Standard-library only
- Dry-run by default (safe preview)
- Collision-safe renaming when a target name already exists
- Simple logging summary

## Usage

```bash
# preview what would move
python organizer.py ./sample-folder

# actually move files
python organizer.py ./sample-folder --apply
```

## Author
