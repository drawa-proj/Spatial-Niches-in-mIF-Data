
# Spatial Tumour Microenvironment Analysis

## Overview

This project analyses spatial cell organisation in tumour tissue using single-cell spatial coordinates.

The analysis includes:

- Immune-Cell Infiltration Profiles Analysis
- oran’s I Spatial Clustering
- Stratification from Spatial Features

## Repository structure


project/
│
├── README.md
│
├── analysis.ipynb
│
├── outputs/
│   ├── D1_ranked.csv
│   ├── *all figures*
│
└── data/


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


## Expected input

Raw data:
https://drive.google.com/file/d/1UDzdZbo-OhQ2Mm_pInUCPzrcHAuIJIu7/view?usp=share_link


The notebook requires preprocessed patient-level `.tsv` files containing spatial cell information.
The `.tsv` files used in this analysis were generated using the preprocessing script:

`preprocessing_script.py`

which internally calls:
`helper_script.py`


This script prepares the raw input data by properly formatting the files used by the analysis notebook.


## Notebook order




