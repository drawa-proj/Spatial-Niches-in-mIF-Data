
# Spatial Tumour Microenvironment Analysis

## Overview

This project analyses spatial cell organisation in tumour tissue using single-cell spatial coordinates.

The analysis includes:

- Immune-Cell Infiltration Profiles Analysis
- oran’s I Spatial Clustering
- Stratification from Spatial Features

## Repository structure

```
root/
│
├── README.md
│
├── process_all.py 
├── add_cell_type.p
│
├── analysis.ipynb
│
│
├── lung-cohort-tabular-data-small/
│ └── *raw data*/
│
├── outputs/
│   ├── D1_ranked.csv
│   ├── *all figures*
│
├── unzipped/ 
│ └── tsv/
│   └── cells_properties/ #tsv files for the analysis
```

## Requirements

Python >= 3.9

Required packages:

- numpy
- pandas
- matplotlib
- seaborn
- scipy
- scikit-learn


Install dependencies:

```bash
pip install numpy pandas matplotlib seaborn scipy scikit-learn
```

## Reproducibility

### Expected input

Raw data:
https://drive.google.com/file/d/1UDzdZbo-OhQ2Mm_pInUCPzrcHAuIJIu7/view?usp=share_link


The notebook requires preprocessed patient-level `.tsv` files containing spatial cell information.
The `.tsv` files used in this analysis were generated using the [process_all.py]('process_all.py'), which internally calls: a [add_cell_type.py]('add_cell_type.py').

Run the main preprocessing script in the *root* directory, then move the output tsv files to `root/unzipped/tsv/cells_properties/` or simply change the DATA_DIR at the start of the notebook.


This script prepares the raw input data by properly formatting the files used by the analysis notebook.

### Notebook
To run the complete analysis, open the [main notebook]('analysis.ipynb') and run all cells from top to botoom.




