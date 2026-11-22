"""Entrypoint: copy the pre-rendered entry image to the output directory.

The image itself is drawn by draw.py (run locally, with the Lexend fonts
shipped in fonts/); this program only copies the finished PNG, so the
graded run is deterministic and needs nothing but the standard library.
"""
import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst)


if __name__ == "__main__":
    main()
