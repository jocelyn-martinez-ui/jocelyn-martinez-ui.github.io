#!/usr/bin/env python3
"""Reconstruct the original PLAIN SIGHT static website from temporary transfer manifests.
The transfer manifests are deleted after reconstruction and are never served."""
import base64
import json
from pathlib import Path
import shutil
import sys

root=Path(__file__).resolve().parents[2]
transfer=root/".plain-sight-transfer"
if not transfer.exists():
    print("No transfer manifests found; nothing to decode.")
    sys.exit(0)

single=list(sorted(transfer.glob("batch-*.json")))
chunks=list(sorted(transfer.glob("pdf-*.json")))
if len(single)!=12 or len(chunks)!=12:
    raise RuntimeError(f"Expected 12 asset batches and 12 PDF chunks; got {len(single)} and {len(chunks)}.")

paths=set()
for manifest in single:
    payload=json.loads(manifest.read_text(encoding="utf-8"))
    for item in payload["files"]:
        rel=Path(item["path"])
        if not rel.parts or rel.parts[0]!="plain-sight" or ".." in rel.parts or rel.is_absolute():
            raise RuntimeError(f"Rejected unexpected path: {rel}")
        if str(rel) in paths:
            raise RuntimeError(f"Duplicate output path: {rel}")
        raw=base64.b64decode(item["base64"],validate=True)
        dest=root/rel
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_bytes(raw)
        paths.add(str(rel))

by_pdf={}
for manifest in chunks:
    item=json.loads(manifest.read_text(encoding="utf-8"))
    rel=Path(item["pdf_path"])
    if not rel.parts or rel.parts[0]!="plain-sight" or ".." in rel.parts or not str(rel).endswith(".pdf"):
        raise RuntimeError(f"Rejected unexpected PDF path: {rel}")
    by_pdf.setdefault(str(rel),[]).append(item)

if len(by_pdf)!=2:
    raise RuntimeError("Expected both publication PDF documents.")
for name,parts in by_pdf.items():
    parts.sort(key=lambda x:x["chunk_index"])
    if len(parts)!=parts[0]["parts"] or [x["chunk_index"] for x in parts]!=list(range(len(parts))):
        raise RuntimeError(f"Missing or reordered PDF chunks for {name}")
    raw=base64.b64decode("".join(x["data"] for x in parts),validate=True)
    if not raw.startswith(b"%PDF"):
        raise RuntimeError(f"Invalid reconstructed PDF {name}")
    dest=root/name
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_bytes(raw)
    paths.add(name)

if len(paths)!=70:
    raise RuntimeError(f"Expected 70 output files, got {len(paths)}")
if not (root/"plain-sight"/"index.html").exists():
    raise RuntimeError("Missing studio homepage")
shutil.rmtree(transfer)
print(f"Reconstructed {len(paths)} original files; removed temporary transfer manifests.")
