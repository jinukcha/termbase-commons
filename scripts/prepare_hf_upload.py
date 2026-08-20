#!/usr/bin/env python3
"""Create a Hugging Face upload folder from a dedup CSV."""
import argparse
import gzip
import shutil
from pathlib import Path

def gzip_copy(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    with open(src, "rb") as fin, gzip.open(dst, "wb", compresslevel=6) as fout:
        shutil.copyfileobj(fin, fout)

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()
    out_file = args.out / "data" / "loinc_terms_multilingual_dedup.csv.gz"
    gzip_copy(args.csv, out_file)
    print(f"wrote {out_file}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
