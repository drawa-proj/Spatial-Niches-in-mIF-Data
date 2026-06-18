from pathlib import Path
from add_cell_type import add_cell_type

folder = Path(
    "lung-cohort-tabular-data-small/tsv/cells_properties"
)

for file in folder.glob("*.tsv.gz"):
    print(f"Processing {file.name}")
    add_cell_type(str(file))
