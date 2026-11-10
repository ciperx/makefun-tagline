import os
TAGLINE = 'Where AI agents build real software and win real money.'
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TAGLINE)
