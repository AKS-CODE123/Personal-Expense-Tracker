import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import os

CSV_PATH = "data/expenses.csv"

# Create file only if it does NOT exist
if not os.path.exists(CSV_PATH):
    with open(CSV_PATH, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "category", "amount", "note"])



def load_expenses():
    expenses = []
    try:
        with open(CSV_PATH, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
        pass
    return expenses

expenses = load_expenses()

def save_expenses(expenses):
    with open(CSV_PATH, "w", newline="") as file:
        fieldnames = ["date", "category", "amount", "note"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)



def add_expenses(expenses):
    while True:
        try:
            date = input(" Enter date (YYYY-MM-DD): ")
            datetime.strptime(date, "%Y-%m-%d")
            break
        except:
            print("Invalid date. Try again.")

    category = input("Enter category: (e.g.; {Food,Shopping,Date,Party,others,etc})").strip()

    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except:
            print("Amount must be a number.")

    note = input("Enter note: ").strip()

    expenses.append({"date": date, "category": category, "amount": amount, "note": note})
    print("Expense Successfully Added")



def view_expenses_with_index(expenses):
    print("\nExpenses List:")
    print("-------------------------------------------")
    
    for i, exp in enumerate(expenses):
        print(f"{i}. {exp['date']} | {exp['category']} | {exp['amount']} | {exp['note']}")



def remove_expense(expenses):
    view_expenses_with_index(expenses)   # show list first
    
    index = int(input("\nEnter index of expense to delete: "))
    
    if 0 <= index < len(expenses):
        expenses.pop(index)
        print("Expense deleted successfully!")
    else:
        print("Invalid index.")


def view_by_category(expenses):
    category = input("Enter category to filter: ").strip()

    print(f"\nExpenses in category: {category}")
    print("---------------------------------------")

    found = False

    for i, exp in enumerate(expenses):
        if exp["category"].lower() == category.lower():
            print(f"{i}. {exp['date']} | {exp['category']} | {exp['amount']} | {exp['note']}")
            found = True

    if not found:
        print("No expenses found for this category.")



def view_by_date_range(expenses):
    start = input("Enter start date (YYYY-MM-DD): ").strip()
    end = input("Enter end date (YYYY-MM-DD): ").strip()

    # convert to datetime.date objects
    start_date = datetime.strptime(start, "%Y-%m-%d").date()
    end_date = datetime.strptime(end, "%Y-%m-%d").date()

    print(f"\nExpenses from {start} to {end}")
    print("---------------------------------------")

    found = False

    for i, exp in enumerate(expenses):
        exp_date = datetime.strptime(exp["date"], "%Y-%m-%d").date()

        if start_date <= exp_date <= end_date:
            print(f"{i}. {exp['date']} | {exp['category']} | {exp['amount']} | {exp['note']}")
            found = True

    if not found:
        print("No expenses found in this date range.")


def get_category_stats(expenses):
    totals = {}
    counts = {}

    for exp in expenses:
        cat = exp["category"]
        amt = float(exp["amount"])

        # total spent per category
        totals[cat] = totals.get(cat, 0) + amt

        # number of expenses per category
        counts[cat] = counts.get(cat, 0) + 1
    return totals, counts

def get_monthly_totals(expenses):
    monthly = {}

    for exp in expenses:
        amt = float(exp["amount"])
        dt = datetime.strptime(exp["date"], "%Y-%m-%d")
        key = dt.strftime("%Y-%m")  

        monthly[key] = monthly.get(key, 0) + amt
    return monthly

def show_statistics(expenses):
    if not expenses:
        print("No expenses to show statistics for.Its Empty!")
        return

    # total & average
    total = 0
    for exp in expenses:
        total += float(exp["amount"])

    avg = total / len(expenses)

    # category stats
    category_totals, category_counts = get_category_stats(expenses)

    # highest spending category
    highest_cat = max(category_totals, key=category_totals.get)
    highest_amount = category_totals[highest_cat]

    # monthly totals
    monthly_totals = get_monthly_totals(expenses)

    print("*********** STATISTICS ***********")
    print(f"Total amount spent: {total}")
    print(f"Average spending per expense: {avg:.2f}")

    print("\nAmount & count per category:")
    for cat in category_totals:
        print(f"  {cat}: {category_totals[cat]} (entries: {category_counts[cat]})")

    print(f"Highest spending category is : {highest_cat} ({highest_amount})")

    print("Monthly totals (YYYY-MM):")
    for month, amt in monthly_totals.items():
        print(f"  {month}: {amt}")

    print("****************************************\n")



def plot_category_bar_chart(expenses):
    if not expenses:
        print("No expenses to plot.")
        return

    category_totals, _ = get_category_stats(expenses)

    categories = list(category_totals.keys())
    totals = list(category_totals.values())

    plt.figure()
    plt.bar(categories, totals)
    plt.xlabel("Category")
    plt.ylabel("Total Spent")
    plt.title("Spending per Category")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def Main():
    expenses = load_expenses()

    while True:
        print("\n**************** EXPENSE TRACKER *************")
        print("Welcome to my program.This is the Menu and here are your Options:")

        print("1. Add expense")
        print("2. View expenses")
        print("3. Delete expense")
        print("4. View by category")
        print("5. View by date range")
        print("6. Show statistics")
        print("7. Plot category bar chart")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expenses(expenses)
            save_expenses(expenses)

        elif choice == "2":
            view_expenses_with_index(expenses)

        elif choice == "3":
            remove_expense(expenses)
            save_expenses(expenses)

        elif choice == "4":
            view_by_category(expenses)

        elif choice == "5":
            view_by_date_range(expenses)

        elif choice == "6":
            show_statistics(expenses)

        elif choice == "7":
            plot_category_bar_chart(expenses)

        elif choice == "8":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

Main()

