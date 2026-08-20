#!/usr/bin/env python3
"""Validate the basic shape of a Termbase Commons wide multilingual CSV."""
import argparse
import csv
import gzip
from pathlib import Path

FORBIDDEN = {"source_term", "target_term", "source_locale", "target_locale", "term_role", "term_type"}

def open_text(path: Path):
    if str(path).endswith(".gz"):
        return gzip.open(path, "rt", encoding="utf-8-sig", newline="")
    return open(path, "r", encoding="utf-8-sig", newline="")

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_path", type=Path)
    args = ap.parse_args()
    with open_text(args.csv_path) as f:
        reader = csv.reader(f)
        header = next(reader)
        forbidden_present = sorted(set(header) & FORBIDDEN)
        if forbidden_present:
            raise SystemExit(f"Forbidden columns present: {forbidden_present}")
        term_columns = [c for c in header if c.startswith("term_")]
        if not term_columns:
            raise SystemExit("No locale term_* columns found")
        rows = 0
        for rows, _ in enumerate(reader, start=1):
            pass
    print(f"PASS rows={rows} locale_term_columns={len(term_columns)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
