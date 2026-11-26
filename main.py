"""Entry program for make.fun news-image-20261125.

Writes the front-page image of Wednesday 25 November 2026 world news to
``$MAKEFUN_OUTPUT_DIR/entry.png`` (default ``out``).

The image itself lives in this repository as ``entry.png``; this program
only copies it, after checking that the bundled file is a well-formed
PNG within the competition limits (at most 1 MiB, at most 1024x1024 px).
No network access, no randomness: every run writes identical bytes.

Standard library only (Python 3.13).
"""

import hashlib
import os
import struct
import sys

ENTRY_NAME = "entry.png"
MAX_BYTES = 1024 * 1024
MAX_DIMENSION = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def resolve_output_dir():
    """Return the directory the image must be written to."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"


def source_image():
    """Path of the bundled front-page image next to this file."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, ENTRY_NAME)


def read_png_dimensions(data):
    """Parse width/height from a PNG IHDR chunk; raise on bad input."""
    if len(data) < 33 or data[:8] != PNG_MAGIC:
        raise ValueError("not a PNG file (bad signature)")
    if data[12:16] != b"IHDR":
        raise ValueError("not a PNG file (no IHDR chunk)")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def validate(data):
    """Check the bundled image against the competition limits."""
    if len(data) > MAX_BYTES:
        raise ValueError("entry.png is %d bytes, over the 1 MiB limit"
                         % len(data))
    width, height = read_png_dimensions(data)
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        raise ValueError("entry.png is %dx%d, over the 1024x1024 limit"
                         % (width, height))
    return width, height


def main():
    src = source_image()
    with open(src, "rb") as fh:
        data = fh.read()
    width, height = validate(data)
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, ENTRY_NAME)
    with open(out_path, "wb") as fh:
        fh.write(data)
    with open(out_path, "rb") as fh:
        written = fh.read()
    if written != data:
        raise ValueError("written bytes differ from entry.png")
    digest = hashlib.sha256(data).hexdigest()
    print("wrote %s (%dx%d, %d bytes, sha256 %s)"
          % (out_path, width, height, len(data), digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
