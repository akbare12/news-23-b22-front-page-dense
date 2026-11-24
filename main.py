#!/usr/bin/env python3
"""news-23 b22 front-page-dense: copy entry.png (1024x1024) to $MAKEFUN_OUTPUT_DIR/entry.png.

Stdlib only. Never writes next to itself: it writes only to MAKEFUN_OUTPUT_DIR,
so it also works from a read-only copy (with MAKEFUN_OUTPUT_DIR pointed elsewhere).
"""
import os
import struct
import sys

EXPECTED_W, EXPECTED_H = 1024, 1024
MAX_BYTES = 1024 * 1024


def main():
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    if not os.path.isfile(src):
        print("error: entry.png missing next to main.py", file=sys.stderr)
        return 1
    if os.path.getsize(src) > MAX_BYTES:
        print(f"error: entry.png is {os.path.getsize(src)} bytes, over 1 MiB", file=sys.stderr)
        return 1
    with open(src, "rb") as fh:
        data = fh.read()
    # Parse the PNG header by hand: signature + IHDR chunk.
    if len(data) < 8 or data[:8] != b"\x89PNG\r\n\x1a\n":
        print("error: not a PNG file", file=sys.stderr)
        return 1
    if len(data) < 33:
        print("error: PNG too short for IHDR", file=sys.stderr)
        return 1
    (ihdr_len,) = struct.unpack(">I", data[8:12])
    if data[12:16] != b"IHDR" or ihdr_len != 13:
        print("error: bad IHDR chunk", file=sys.stderr)
        return 1
    w, h = struct.unpack(">II", data[16:24])
    if (w, h) != (EXPECTED_W, EXPECTED_H):
        print(f"error: expected {EXPECTED_W}x{EXPECTED_H}, got {w}x{h}", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(f"error: {len(data)} bytes exceeds 1 MiB", file=sys.stderr)
        return 1
    # IEND trailer must be a well-formed 12-byte chunk at the end.
    if data[-12:] != b"\x00\x00\x00\x00IEND\xaeB`\x82":
        print("error: missing or malformed IEND trailer", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    # Guard: never write into the repo directory itself.
    repo = os.path.dirname(os.path.abspath(__file__))
    if os.path.abspath(out_dir) == repo:
        print("error: MAKEFUN_OUTPUT_DIR must not be the repo dir", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(dst, "wb") as fh:
        fh.write(data)
    # Re-read the output and confirm it is byte-identical to the source.
    with open(dst, "rb") as fh:
        written = fh.read()
    if written != data:
        print("error: output differs from source", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({len(data)} bytes, {w}x{h})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
