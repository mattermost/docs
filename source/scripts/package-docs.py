#!/usr/bin/env python3
"""Package Mattermost documentation for offline distribution.

Generates downloadable artifacts from built Sphinx documentation:

  - HTML package (.zip)  -- self-contained offline site
  - PDF (.pdf)           -- print-ready single document via WeasyPrint

Usage:
    # Build everything (requires HTML + singlehtml builds first)
    python package-docs.py --all

    # Build only the HTML zip package (requires `make html` first)
    python package-docs.py --html-package

    # Build only the PDF (requires `make singlehtml` first)
    python package-docs.py --pdf
"""

import argparse
import os
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent.parent
BUILD_DIR = ROOT_DIR / "build"
HTML_DIR = BUILD_DIR / "html"
SINGLEHTML_DIR = BUILD_DIR / "singlehtml"
DOWNLOADS_DIR = BUILD_DIR / "downloads"

TIMESTAMP = datetime.now(timezone.utc).strftime("%Y-%m-%d")
HTML_ZIP_NAME = f"mattermost-docs-{TIMESTAMP}.zip"
PDF_NAME = f"mattermost-docs-{TIMESTAMP}.pdf"

# Stable filenames (latest) for permanent download URLs
HTML_ZIP_LATEST = "mattermost-docs-html.zip"
PDF_LATEST = "mattermost-docs.pdf"


def build_html_package() -> Path:
    """Create a zip archive of the full HTML documentation site."""
    if not HTML_DIR.exists():
        print("Error: HTML build directory not found at", HTML_DIR, file=sys.stderr)
        print("Run `make html` first.", file=sys.stderr)
        sys.exit(1)

    DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)

    zip_path = DOWNLOADS_DIR / HTML_ZIP_LATEST
    dated_zip_path = DOWNLOADS_DIR / HTML_ZIP_NAME

    print(f"Packaging HTML docs from {HTML_DIR} ...")

    # Directories and files to skip in the zip (build artifacts, not useful offline)
    skip_prefixes = {".buildinfo", ".doctrees"}

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        file_count = 0
        for file_path in sorted(HTML_DIR.rglob("*")):
            if not file_path.is_file():
                continue
            rel = file_path.relative_to(HTML_DIR)
            # Skip hidden build artifacts
            if any(part.startswith(".") for part in rel.parts):
                continue
            if str(rel) in skip_prefixes:
                continue
            zf.write(file_path, f"mattermost-docs/{rel}")
            file_count += 1

        # Add a small README for offline users
        readme = (
            "Mattermost Documentation (Offline)\n"
            "===================================\n\n"
            f"Generated: {TIMESTAMP}\n\n"
            "Open index.html in your browser to browse the documentation offline.\n\n"
            "For the latest version, visit: https://docs.mattermost.com/\n"
        )
        zf.writestr("mattermost-docs/README.txt", readme)
        file_count += 1

    # Also create a dated copy
    import shutil
    shutil.copy2(zip_path, dated_zip_path)

    size_mb = zip_path.stat().st_size / (1024 * 1024)
    print(f"HTML package created: {zip_path} ({size_mb:.1f} MB, {file_count} files)")
    return zip_path


def build_pdf() -> Path:
    """Generate a PDF from the single-page HTML build using WeasyPrint."""
    singlehtml_index = SINGLEHTML_DIR / "index.html"
    if not singlehtml_index.exists():
        print(
            "Error: Single-page HTML not found at", singlehtml_index, file=sys.stderr
        )
        print("Run `make singlehtml` first.", file=sys.stderr)
        sys.exit(1)

    try:
        from weasyprint import HTML
    except ImportError:
        print(
            "Error: WeasyPrint is not installed. Install it with: pip install weasyprint",
            file=sys.stderr,
        )
        sys.exit(1)

    DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)

    pdf_path = DOWNLOADS_DIR / PDF_LATEST
    dated_pdf_path = DOWNLOADS_DIR / PDF_NAME

    print(f"Generating PDF from {singlehtml_index} ...")
    print("(This may take several minutes for large documentation sets.)")

    # Build PDF with WeasyPrint, using the singlehtml directory as base
    # so that relative asset paths (CSS, images) resolve correctly.
    doc = HTML(filename=str(singlehtml_index), base_url=str(SINGLEHTML_DIR))
    doc.write_pdf(
        str(pdf_path),
        presentational_hints=True,
    )

    # Also create a dated copy
    import shutil
    shutil.copy2(pdf_path, dated_pdf_path)

    size_mb = pdf_path.stat().st_size / (1024 * 1024)
    print(f"PDF created: {pdf_path} ({size_mb:.1f} MB)")
    return pdf_path


def main():
    parser = argparse.ArgumentParser(
        description="Package Mattermost documentation for offline distribution."
    )
    parser.add_argument(
        "--html-package",
        action="store_true",
        help="Create a zip archive of the HTML documentation.",
    )
    parser.add_argument(
        "--pdf",
        action="store_true",
        help="Generate a PDF from the single-page HTML build.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Build all downloadable formats (HTML zip + PDF).",
    )
    args = parser.parse_args()

    if not any([args.html_package, args.pdf, args.all]):
        parser.print_help()
        sys.exit(1)

    results = []

    if args.html_package or args.all:
        results.append(("HTML package", build_html_package()))

    if args.pdf or args.all:
        results.append(("PDF", build_pdf()))

    print("\n--- Download artifacts ---")
    for label, path in results:
        print(f"  {label}: {path}")
    print()


if __name__ == "__main__":
    main()
