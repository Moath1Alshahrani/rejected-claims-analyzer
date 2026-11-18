# Rejected Claims Analyzer

A Python (pandas) project that cleans and analyzes a synthetic healthcare claims dataset to identify why claims are rejected and how much revenue is affected.

> All data in this project is **synthetic**. No real patient information is used.

## What it does
- Cleans the data: removes duplicate rows, fixes spacing and letter case in codes and payer names, and detects missing values
- Calculates rejection reasons (count and percentage)
- Calculates rejection rate for each insurance payer
- Calculates the rejected amount (SAR) for each rejection reason
- Exports an Excel report and a chart

## Tools
Python, pandas, matplotlib, openpyxl

## How to run
1. Install the libraries: `python -m pip install pandas openpyxl matplotlib`
2. Run: `python analysis.py`

## Outputs
- `rejection_report.xlsx`: summary by payer and by rejection reason
- `rejected_amount_by_reason.png`: chart of rejected amount by reason