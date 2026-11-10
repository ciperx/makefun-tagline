#!/usr/bin/env python3
"""Write make.fun's tagline to /output/entry.txt (deterministic, no network)."""
import os
TAGLINE = 'Where AI agents build real software and win real money.'
out = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TAGLINE)
