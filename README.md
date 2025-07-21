# Betlémská Statistics Project

This repository contains a data analysis project focused on extracting and analyzing receipt data from a structured PDF file (`betlemska.pdf`). 

## Project Summary

The input data consists of a cadé/bar's receipts (from Klub Betlémská), embedded in a PDF report. The goal was to:

- Extract structured tabular data (e.g. date, value, number of items, tips)
- Clean and preprocess the data 
- Analyze trends in spending, tipping, and timing

## Contents

- `stats_betlemska.ipynb` – Jupyter notebook with PDF parsing, data wrangling, and analysis
- `data_extraction.py` – Python script for extracting structured data from the PDF
- `betlemska.pdf` – Input data file (receipts)
- `betlemska.pkl` – Pickled version of cleaned DataFrame (used in notebook)
