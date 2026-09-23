---

Tools & Technologies

- Python
- Pandas
- Statsmodels
- Microsoft Excel
- GitHub

Project Files

- "clean_data.py" – Python data cleaning script
- "co2_raw.csv" – Raw CO₂ dataset
- "co2_cleaned.csv" – Cleaned dataset
- "co2_cleaned.xlsx" – Cleaned Excel file
- "co2_cleaning_result.png" – Data cleaning visualization
- "DATA_QUALITY_REPORT.md" – Data quality report

Project Objectives

- Handle missing values
- Remove duplicate records
- Correct data types
- Prepare clean and structured datasets
- Generate data quality reports and visualizations

Author

Prashant Kumar# SWYNEX Data Cleaning & Preparation

## Task 1
Clean and prepare a public dataset for analysis using Python/Pandas.

### Dataset selected
**Mauna Loa Weekly Atmospheric CO2 Data**

The dataset contains weekly atmospheric CO2 measurements from Mauna Loa Observatory, Hawaii. The public dataset is distributed by `statsmodels`; its documentation identifies the period as March 1958–December 2001 and the measurement as CO2 concentration in ppmv.

### Objective
Identify and handle:
- Missing values
- Duplicate records
- Incorrect data types
- Inconsistent ordering/formatting
- Produce a cleaned dataset and document the changes

## Project structure

```text
SWYNEX-Data-Cleaning-Preparation/
├── raw/
│   └── co2_raw.csv
├── cleaned/
│   ├── co2_cleaned.csv
│   └── co2_cleaned.xlsx
├── reports/
│   └── DATA_QUALITY_REPORT.md
├── src/
│   └── clean_data.py
├── linkedin_post.txt
├── video_script.txt
├── requirements.txt
└── README.md
```

## Cleaning performed

1. Converted `date` to a proper datetime type.
2. Converted `co2` to numeric.
3. Checked for invalid dates.
4. Checked exact duplicate records using `date + co2`.
5. Sorted observations chronologically.
6. Filled missing CO2 values using time-based interpolation.
7. Validated the final dataset to confirm no missing CO2 values remain.

## Result
The cleaned CSV is ready for analysis and visualization.

## How to run

```bash
pip install -r requirements.txt
python src/clean_data.py
```

## Source
Statsmodels — Mauna Loa Weekly Atmospheric CO2 Data.

The underlying data are attributed in the statsmodels documentation to Keeling, C.D. and T.P. Whorf (2004), with the original data source identified as the Carbon Dioxide Information Analysis Center (Oak Ridge National Laboratory). The dataset is listed as public domain.

## Submission checklist
- [x] Public dataset selected
- [x] Missing values checked and handled
- [x] Duplicate records checked
- [x] Data types checked and standardized
- [x] Data ordering standardized
- [x] Cleaned CSV included
- [x] Excel version included
- [x] README included
- [x] Data quality report included
- [x] LinkedIn post draft included
- [x] Video explanation script included
