"""
PS 85 - Hotel Revenue Analyzer  (VS Code "Run" version)

Sirf Run button dabao -> hotel_sales.csv apne aap ban jayegi aur
saare 4 test cases ka output terminal me aa jayega.
Last me menu aayega (1 = Daily revenue, 2 = Revenue by room type, 3 = Exit).

Install (ek baar):  pip install pandas matplotlib
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# File hamesha isi .py file wale folder me banegi / padhi jayegi
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

SAMPLE_CSV = """Date,RoomType,RoomsSold,Rate
2026-10-01,Standard,10,2000
2026-10-01,Deluxe,5,3500
2026-10-02,Standard,12,2000
2026-10-02,Deluxe,6,3500
2026-10-03,Standard,8,2000
2026-10-03,Deluxe,4,3500
"""

COLUMNS = ["Date", "RoomType", "RoomsSold", "Rate"]


def fmt(x):
    """37500.0 -> 37500, 37500.5 -> 37500.50"""
    return str(int(x)) if float(x).is_integer() else f"{x:.2f}"


def write_file(name, text):
    with open(name, "w") as f:
        f.write(text)


def to_number(text):
    try:
        value = float(str(text).strip())
    except ValueError:
        return None
    if value != value:      # NaN
        return None
    return value


def load_data(filename):
    """CSV load + validation. Valid rows ka DataFrame return karta hai."""
    try:
        raw = pd.read_csv(filename, dtype=str, keep_default_na=False)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error: Could not read '{filename}' ({e}).")
        return None

    raw.columns = [c.strip() for c in raw.columns]
    if any(c not in raw.columns for c in COLUMNS):
        print("Error: CSV must have columns: Date,RoomType,RoomsSold,Rate")
        return None

    good = []
    for n, (_, row) in enumerate(raw.iterrows(), start=1):  # n = data row no.
        date = str(row["Date"]).strip()
        room = str(row["RoomType"]).strip()
        sold = to_number(row["RoomsSold"])
        rate = to_number(row["Rate"])

        if date == "" or room == "":
            print(f"Warning: Row {n} skipped - Date/RoomType missing.")
        elif sold is None:
            print(f"Warning: Row {n} skipped - RoomsSold must be numeric.")
        elif rate is None:
            print(f"Warning: Row {n} skipped - Rate must be numeric.")
        elif sold < 0:
            print(f"Warning: Row {n} skipped - RoomsSold must be 0 or more.")
        elif rate < 0:
            print(f"Warning: Row {n} skipped - Rate must be 0 or more.")
        else:
            good.append({"Date": date, "RoomType": room,
                         "RoomsSold": sold, "Rate": rate})

    df = pd.DataFrame(good, columns=COLUMNS)
    df["Revenue"] = df["RoomsSold"] * df["Rate"]      # Revenue = RoomsSold x Rate
    print(f"Valid records analysed: {len(df)}")
    return df


def finish_chart(fig, name, show):
    fig.savefig(name)
    print(f"(Chart saved: {name})")
    if show:
        plt.show()
    plt.close(fig)


def daily_revenue(df, show=False):
    daily = df.groupby("Date")["Revenue"].sum().sort_index()
    for d, r in daily.items():
        print(f"{d} : Rs. {fmt(r)}")
    print(f"Total revenue: Rs. {fmt(daily.sum())}")
    best = daily.idxmax()
    print(f"Best day: {best} (Rs. {fmt(daily[best])})")

    fig = plt.figure(figsize=(7, 4))
    plt.bar(daily.index, daily.values, color="steelblue")
    plt.title("Daily Revenue")
    plt.xlabel("Date")
    plt.ylabel("Revenue (Rs.)")
    plt.tight_layout()
    finish_chart(fig, "daily_revenue.png", show)


def revenue_by_room(df, show=False):
    by_room = df.groupby("RoomType")["Revenue"].sum().sort_values(ascending=False)
    total = by_room.sum()
    for room, r in by_room.items():
        pct = (r / total * 100) if total else 0
        print(f"{room} : Rs. {fmt(r)} ({pct:.2f}%)")
    print(f"Total revenue: Rs. {fmt(total)}")

    if total > 0:
        fig = plt.figure(figsize=(5, 5))
        plt.pie(by_room.values, labels=by_room.index, autopct="%.2f%%")
        plt.title("Revenue Share by Room Type")
        finish_chart(fig, "room_type_share.png", show)


def header(text):
    print("\n" + "=" * 55)
    print(text)
    print("=" * 55)


def run_all_test_cases():
    """4 test cases automatically chalata hai."""
    write_file("hotel_sales.csv", SAMPLE_CSV)

    header("TEST CASE 1: Normal Input (Daily revenue)")
    df = load_data("hotel_sales.csv")
    daily_revenue(df)

    header("TEST CASE 2: Boundary / Minimum Input (1 row)")
    write_file("test_one_row.csv", "Date,RoomType,RoomsSold,Rate\n2026-10-01,Standard,1,2000\n")
    df1 = load_data("test_one_row.csv")
    daily_revenue(df1)

    header("TEST CASE 3: Invalid Input")
    print("(a) Extra row 2026-10-04,Deluxe,-3,3500")
    write_file("test_invalid.csv", SAMPLE_CSV + "2026-10-04,Deluxe,-3,3500\n")
    load_data("test_invalid.csv")
    print("\n(b) File sales_old.csv (does not exist)")
    load_data("sales_old.csv")

    header("TEST CASE 4: Different Valid Scenario (Revenue by room type)")
    df = load_data("hotel_sales.csv")
    revenue_by_room(df)

    # temporary test files hata do
    for f in ("test_one_row.csv", "test_invalid.csv"):
        if os.path.exists(f):
            os.remove(f)


def menu():
    df = load_data("hotel_sales.csv")
    if df is None or df.empty:
        return
    while True:
        header("MENU - Hotel Revenue Analyzer")
        print("1. Daily revenue")
        print("2. Revenue by room type")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ").strip()
        if choice == "1":
            daily_revenue(df, show=True)
        elif choice == "2":
            revenue_by_room(df, show=True)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")


if __name__ == "__main__":
    run_all_test_cases()
    menu()
