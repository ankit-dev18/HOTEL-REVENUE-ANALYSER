# PS 85 – Hotel Revenue Analyzer

**Author:** Ankit Kumar
**Course:** B.Tech (CSE), Rungta International Skills University, Bhilai
**Language:** Python 3
**Libraries:** Pandas, Matplotlib, os (standard library)

---

## 1. Overview

**Hotel Revenue Analyzer** is a command-line Python program that reads hotel room sales data from a CSV file, validates it, calculates revenue, and presents the results as both text output and charts.

It answers two business questions:

1. **How much revenue did the hotel earn each day?** (and which day was the best)
2. **Which room type contributes how much to total revenue?** (with percentage share)

The program is designed as a **"Run button" script** for VS Code: when you press Run, it automatically creates the sample data file, executes all 4 test cases, and then opens an interactive menu.

---

## 2. Features

- Auto-generates `hotel_sales.csv` with sample data (no manual setup).
- Robust **data validation** with clear warnings for bad rows.
- **Daily revenue report** with total revenue and best day.
- **Revenue by room type** report with percentage share.
- **Charts** saved as PNG files (bar chart and pie chart).
- Built-in **4 test cases** covering normal, boundary, invalid and alternate scenarios.
- **Interactive menu** for exploring the data after tests finish.
- Safe file handling: the script always reads/writes files in its own folder.

---

## 3. Requirements & Installation

- Python 3.8 or higher
- Install the dependencies once:

```bash
pip install pandas matplotlib
```

---

## 4. How to Run

1. Open the project folder in **VS Code**.
2. Open `hotel_revenue_vscode .py`.
3. Click the **Run** button (or run in terminal):

```bash
python "hotel_revenue_vscode .py"
```

The program will:
1. Create `hotel_sales.csv`.
2. Run and print all 4 test cases.
3. Show the menu:

```
1. Daily revenue
2. Revenue by room type
3. Exit
```

---

## 5. Input Format

The CSV file must contain exactly these columns:

| Column      | Description                      | Rule                       |
|-------------|----------------------------------|----------------------------|
| `Date`      | Date of sale (e.g. 2026-10-01)   | Must not be empty          |
| `RoomType`  | Category of room (Standard etc.) | Must not be empty          |
| `RoomsSold` | Number of rooms sold that day    | Numeric, 0 or more         |
| `Rate`      | Price per room (in Rs.)          | Numeric, 0 or more         |

### Sample data

```csv
Date,RoomType,RoomsSold,Rate
2026-10-01,Standard,10,2000
2026-10-01,Deluxe,5,3500
2026-10-02,Standard,12,2000
2026-10-02,Deluxe,6,3500
2026-10-03,Standard,8,2000
2026-10-03,Deluxe,4,3500
```

### Formula used

```
Revenue = RoomsSold × Rate
```

---

## 6. Sample Output

**Daily revenue**

```
2026-10-01 : Rs. 37500
2026-10-02 : Rs. 45000
2026-10-03 : Rs. 30000
Total revenue: Rs. 112500
Best day: 2026-10-02 (Rs. 45000)
```

**Revenue by room type**

```
Standard : Rs. 60000 (53.33%)
Deluxe : Rs. 52500 (46.67%)
Total revenue: Rs. 112500
```

**Generated charts**

| File                  | Chart type | Content                    |
|-----------------------|------------|----------------------------|
| `daily_revenue.png`   | Bar chart  | Revenue for each date      |
| `room_type_share.png` | Pie chart  | Revenue share by room type |

---

## 7. Code Structure

| Function / Block        | Purpose                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------|
| `BASE_DIR` + `os.chdir` | Makes all files load/save beside the script, regardless of where it is run from.          |
| `SAMPLE_CSV`            | Built-in sample dataset used to create `hotel_sales.csv`.                                 |
| `fmt(x)`                | Formats numbers: `37500.0 → 37500`, `37500.5 → 37500.50`.                                 |
| `write_file()`          | Writes text to a file (used for sample and test CSVs).                                    |
| `to_number()`           | Safely converts text to a float; returns `None` for invalid or NaN values.                |
| `load_data()`           | Reads the CSV, checks columns, validates each row, adds the `Revenue` column.             |
| `finish_chart()`        | Saves a chart as PNG and optionally displays it.                                          |
| `daily_revenue()`       | Groups by date, prints totals and best day, draws bar chart.                              |
| `revenue_by_room()`     | Groups by room type, prints amount and percentage, draws pie chart.                       |
| `header()`              | Prints formatted section headings.                                                        |
| `run_all_test_cases()`  | Executes the 4 test cases automatically and cleans up temporary files.                    |
| `menu()`                | Interactive loop for the user (options 1, 2, 3).                                          |

---

## 8. Data Validation

`load_data()` checks every row and **skips** invalid ones with a warning that includes the row number:

| Problem                         | Message shown                                      |
|---------------------------------|----------------------------------------------------|
| Missing Date or RoomType        | `Row n skipped - Date/RoomType missing.`           |
| Non-numeric RoomsSold           | `Row n skipped - RoomsSold must be numeric.`       |
| Non-numeric Rate                | `Row n skipped - Rate must be numeric.`            |
| Negative RoomsSold              | `Row n skipped - RoomsSold must be 0 or more.`     |
| Negative Rate                   | `Row n skipped - Rate must be 0 or more.`          |
| File does not exist             | `Error: File '...' not found.`                     |
| Missing required columns        | `Error: CSV must have columns: Date,RoomType,...`  |

After validation it prints how many valid records were analysed.

---

## 9. Test Cases

| # | Scenario                | Input                                        | Expected result                                              |
|---|-------------------------|----------------------------------------------|--------------------------------------------------------------|
| 1 | Normal input            | Sample CSV (6 rows)                          | Daily revenue for 3 days, total Rs. 112500, best day 2026-10-02 |
| 2 | Boundary / minimum      | CSV with 1 row (1 room × Rs. 2000)           | Revenue Rs. 2000 for that single day                         |
| 3a| Invalid input (bad row) | Sample CSV + row with `RoomsSold = -3`       | Warning: row skipped; other 6 rows still analysed            |
| 3b| Invalid input (no file) | `sales_old.csv` (does not exist)             | `Error: File 'sales_old.csv' not found.`                     |
| 4 | Different valid scenario| Sample CSV, revenue by room type             | Standard 53.33%, Deluxe 46.67%                               |

Temporary files (`test_one_row.csv`, `test_invalid.csv`) are deleted automatically after the tests.

---

## 10. Files Generated

```
project-folder/
├── hotel_revenue_vscode .py   # main program
├── hotel_sales.csv            # auto-created sample data
├── daily_revenue.png          # bar chart (after running option 1)
├── room_type_share.png        # pie chart (after running option 2)
└── README.md
```

---

## 11. Possible Future Improvements

- Accept the CSV filename from the command line.
- Add monthly and weekly revenue summaries.
- Add occupancy rate (needs total rooms available).
- Export reports to Excel or PDF.
- Build a simple GUI or web dashboard.

---

## 12. Author

**Ankit Kumar**
B.Tech CSE (1st Year), Rungta International Skills University, Bhilai, Chhattisgarh
