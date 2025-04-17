from pathlib import Path
import shutil

# Paths
raw_path = Path("data/raw")
annotated_path = Path("data/annotated")
output_path = Path("data/non_annotated")
output_path.mkdir(parents=True, exist_ok=True)

# File stem sets (without extension)
raw_stems = {f.stem for f in raw_path.glob("*")}
annotated_stems = {f.stem for f in annotated_path.glob("*")}

# Difference = Non-annotated
non_annotated = raw_stems - annotated_stems

# Copy non-annotated files to output
for stem in non_annotated:
    matches = list(raw_path.glob(f"{stem}.*"))
    if matches:
        shutil.copy(matches[0], output_path / matches[0].name)

print(f"Copied {len(non_annotated)} non-annotated files to {output_path}")
