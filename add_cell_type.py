"""
Add a cell.type column to a mIF tabular data file by matching the phenotype
column against IF1_phen_to_cell_mapping.csv.

Handles marker-order mismatch: both the phenotype strings in the data and the
mapping dictionary keys are canonicalised (markers sorted alphabetically) before
matching.

Usage:
    python add_cell_type.py <input_tsv_or_tsv_gz> [output_tsv]

If no output path is given, the output is written next to the input file with
"_with_celltype" appended before the extension.
"""

import re
import sys
from pathlib import Path

import pandas as pd


MAPPING_FILE = (
    Path(__file__).parent
    / "lung-cohort-tabular-data-small"
    / "tsv"
    / "IF1_phen_to_cell_mapping.csv"
)

def parse_phenotype(pheno: str) -> dict[str, str]:
    """Return {marker: '+'/'-'} for a phenotype string like 'CD15-CK+CD3-'."""
    return {m: s for m, s in re.findall(r"([A-Za-z0-9]+)([+\-])", pheno)}


def canonical(pheno: str) -> str:
    """Canonical phenotype: markers sorted alphabetically, signs attached."""
    parsed = parse_phenotype(pheno)
    return "".join(f"{k}{v}" for k, v in sorted(parsed.items()))


def build_mapping(mapping_file: Path) -> dict[str, str]:
    df = pd.read_csv(mapping_file)
    return {canonical(row["phenotype"]): row["celltype"] for _, row in df.iterrows()}


def add_cell_type(input_path: str, output_path: str | None = None) -> None:
    inp = Path(input_path)

    # Infer output path
    if output_path is None:
        suffixes = "".join(inp.suffixes)          # e.g. ".tsv.gz" or ".tsv"
        stem = inp.name[: -len(suffixes)] if suffixes else inp.name
        output_path = str(inp.parent / f"{stem}_with_celltype.tsv")

    # Load data
    compression = "gzip" if inp.suffix == ".gz" else None
    df = pd.read_csv(inp, sep="\t", compression=compression)

    if "phenotype" not in df.columns:
        raise ValueError(f"No 'phenotype' column found in {inp}")

    # Build lookup and map
    mapping = build_mapping(MAPPING_FILE)
    df["cell.type"] = df["phenotype"].map(lambda p: mapping.get(canonical(p), "unknown"))

    n_unknown = (df["cell.type"] == "unknown").sum()
    if n_unknown:
        print(f"Warning: {n_unknown} rows could not be mapped (labelled 'unknown')")

    # Save
    df.to_csv(output_path, sep="\t", index=False)
    print(f"Saved {len(df)} rows to: {output_path}")
    print("\nCell type distribution:")
    print(df["cell.type"].value_counts().to_string())


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    add_cell_type(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
