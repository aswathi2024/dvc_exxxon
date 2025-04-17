from pathlib import Path
import shutil

# Paths
raw_path = Path("data/raw")
annotated_path = Path("data/annotated")
output_path = Path("data/non_annotated")

# Step 1: Clear output folder
if output_path.exists():
    shutil.rmtree(output_path)
output_path.mkdir(parents=True, exist_ok=True)

# Step 2: Get file stems
raw_stems = {f.stem for f in raw_path.glob("*")}
annotated_stems = {f.stem for f in annotated_path.glob("*")}

# Step 3: Determine non-annotated
non_annotated = raw_stems - annotated_stems

# Step 4: Copy updated non-annotated files
for stem in non_annotated:
    matches = list(raw_path.glob(f"{stem}.*"))
    for match in matches:
        shutil.copy(match, output_path / match.name)

print(f"Copied {len(non_annotated)} non-annotated files to {output_path}")
