# Project Summary – PS 85: Hotel Revenue Analyzer

**Author:** Ankit Kumar
**Technology:** Python 3, Pandas, Matplotlib

---

## Objective

To build a program that analyses hotel room sales data from a CSV file and reports how much revenue the hotel earns per day and per room type, with charts for easy understanding.

## Problem Statement

Hotels record daily room sales (date, room type, rooms sold, rate). Calculating revenue by hand is slow and error-prone, especially when data has mistakes. This project automates the calculation, checks the data for errors, and presents clear results.

## Approach

1. **Load** the CSV using Pandas.
2. **Validate** each row (missing values, non-numeric values, negative numbers). Invalid rows are skipped with a warning, so one bad row never crashes the program.
3. **Calculate** revenue: `Revenue = RoomsSold × Rate`.
4. **Analyse** the data using `groupby`:
   - Total revenue per date, with the best-performing day.
   - Total revenue per room type, with percentage share.
5. **Visualise** results using Matplotlib: a bar chart for daily revenue and a pie chart for room type share. Charts are saved as PNG files.
6. **Interact** through a simple menu (Daily revenue / Revenue by room type / Exit).

## Key Features

- One-click run in VS Code; the sample CSV is created automatically.
- Row-level validation with clear messages.
- Handles missing files and wrong column names gracefully.
- Four built-in test cases that run automatically.
- Clean number formatting (e.g. `37500` instead of `37500.0`).

## Results (Sample Data)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Total revenue         | Rs. 112,500               |
| Best day              | 2026-10-02 (Rs. 45,000)   |
| Standard rooms share  | Rs. 60,000 (53.33%)       |
| Deluxe rooms share    | Rs. 52,500 (46.67%)       |

## Test Cases Covered

| Type              | What it checks                                                |
|-------------------|---------------------------------------------------------------|
| Normal input      | Correct daily totals for typical data                         |
| Boundary input    | Works correctly with just one row                             |
| Invalid input     | Negative value row is skipped; missing file shows an error    |
| Different scenario| Revenue split by room type with percentages                   |

## Learning Outcomes

- Reading and cleaning CSV data with Pandas.
- Using `groupby`, aggregation and sorting.
- Input validation and error handling with `try/except`.
- Creating and saving charts with Matplotlib.
- Writing modular code with small, reusable functions.
- Designing test cases for normal, boundary and invalid inputs.

## Conclusion

The Hotel Revenue Analyzer gives hotel managers a quick, reliable way to understand their income. It validates input, produces accurate calculations, and shows results in both text and chart form, all from a single Python file.

---

*Prepared by Ankit Kumar, B.Tech CSE, Rungta International Skills University, Bhilai.*
