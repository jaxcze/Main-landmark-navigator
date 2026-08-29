#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build script for the mainLandmarkNavigator NVDA add-on.

Usage:  python build.py
Requires: Python 3.6+, gettext (msgfmt on PATH)
"""
import os, sys, subprocess, zipfile
from pathlib import Path

# Windows consoles often use a legacy codepage (e.g. cp1250) that can't
# encode the ✓ / → / … characters below; fall back to UTF-8 so the build
# doesn't fail with a UnicodeEncodeError after already succeeding.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

ADDON_NAME  = "mainLandmarkNavigator"
VERSION     = "1.0.5"
OUTPUT_FILE = f"{ADDON_NAME}-{VERSION}.nvda-addon"

ROOT       = Path(__file__).resolve().parent
ADDON_DIR  = ROOT / "addon"
LOCALE_DIR = ADDON_DIR / "locale"
INCLUDE    = {".py", ".mo", ".md"}


def compile_translations():
    for po in sorted(LOCALE_DIR.rglob("nvda.po")):
        mo   = po.with_suffix(".mo")
        lang = po.relative_to(LOCALE_DIR).parts[0]
        try:
            subprocess.run(["msgfmt", str(po), "-o", str(mo)],
                           check=True, capture_output=True, text=True)
            print(f"  [{lang}] compiled")
        except subprocess.CalledProcessError as e:
            sys.exit(f"msgfmt error [{lang}]: {e.stderr.strip()}")
        except FileNotFoundError:
            sys.exit("msgfmt not found — install gettext")


def create_addon():
    out = ROOT / OUTPUT_FILE
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(ROOT / "manifest.ini", "manifest.ini")
        for src in sorted(ADDON_DIR.rglob("*")):
            if src.is_file() and src.suffix in INCLUDE:
                zf.write(src, src.relative_to(ADDON_DIR).as_posix())
    return out


if __name__ == "__main__":
    os.chdir(ROOT)
    print(f"Building {OUTPUT_FILE} …")
    compile_translations()
    out = create_addon()
    print(f"✓ Done → {out}  ({out.stat().st_size // 1024} kB)")
