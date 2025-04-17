from pathlib import Path
import shutil

# Paths
raw_path = Path("data/raw/pdf")
annotated_path = Path("data/annotated/Metablock")
output_path = Path("data/non_annotated/Metablock")

# Step 1: Clear output folder
if output_path.exists():
    shutil.rmtree(output_path)
output_path.mkdir(parents=True, exist_ok=True)

# Step 2: Get file stems
raw_stems = {f.stem for f in raw_path.glob("*.pdf")}
annotated_stems = {f.stem for f in annotated_path.glob("*.json")}

# Step 3: Determine non-annotated
non_annotated = raw_stems - annotated_stems

# Step 4: Copy non-annotated PDFs
for stem in non_annotated:
    src_file = raw_path / f"{stem}.pdf"
    if src_file.exists():
        shutil.copy(src_file, output_path / src_file.name)

print(f"Copied {len(non_annotated)} non-annotated files to {output_path}")
