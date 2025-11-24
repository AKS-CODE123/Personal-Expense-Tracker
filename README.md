# Personal-Expense-Tracker
This is a project by me that aims to solve an issue faced by many, tracking where your money goes. With the help of this project one can now track where their expenses are going and thus allows them to save money.
Expense Tracker (Python)

A command-line application designed to help users record, view, filter, analyze, and visualize their daily expenses.
Data is stored permanently in a CSV file, allowing the application to function as a lightweight personal finance tool.

<h1>Purpose:</h1>

The purpose of this project is to provide a simple, local, and efficient expense-management system that allows users to:

   &#8226; Maintain a record of daily transactions

   &#8226; Analyze money spent across categories

   &#8226; View spending patterns over different dates

   &#8226; Visualize category-wise spending

   &#8226; Manage expenses without requiring any external applications

The program runs directly in the terminal and is easy to use for beginners as well as intermediate Python learners.

<h1>Features:</h1>

&#10148;Record Expenses

   &#8226;   Add new expenses with date, category, amount, and a note

   &#8226;   Validated date and amount inputs

&#10148;View & Manage Expenses

   &#8226;View all expenses with index numbers

   &#8226;Delete expenses by index

   &#8226;Filter expenses by category

   &#8226;Filter expenses by a date range

&#10148;Statistics
 
   &#8226;Total spending

   &#8226;Average spending

   &#8226;Spending per category

   &#8226;Number of entries per category

   &#8226;Highest spending category

   &#8226;Monthly spending summary

&#10148;Visualization

   &#8226;Category-wise bar chart generated using Matplotlib

&#10148;File Handling

  &#8226;Expenses stored permanently in data/expenses.csv
 
  &#8226;CSV automatically created if missing

TECH STACK:

|Component	       | Technology               |
|------------------|--------------------------|
|Backend	       | Python 3                 |
|File Storage	   | CSV (DictReader/Writer)  |
|Visualization	   | Matplotlib               |
|Libraries Used	   | csv, datetime, os        |

&#10022;PROJECT SRTUCTURE:

    /data
          └── expenses.csv
     Expense_Tracker.py
     README.md


The data/ folder stores the CSV file used for permanent data storage.

How to Run Locally
1. Install dependencies:

        pip install matplotlib

2. Run the application:

        python expense_tracker.py

3. Use the interactive menu

  The application provides options such as:

     1. Add expense
     2. View expenses
     3. Delete expense
     4. View by category
     5. View by date range
     6. Show statistics
     7. Plot category bar chart 
     8. Exit


Enter the number corresponding to the desired operation.

&#10022;Sample CSV Output : 

   |date        |  category  | amount  |  note |
   |------------|------------|---------|-------|
   |2025-01-10  | Food       |220      |Lunch  |
   |2025-01-12  | Shopping   |1500     |Clothes|
   |2025-02-01  | Travel     |999      |cab    |

MADE BY:


|Name   	   |Enrollment No. |
|--------------|---------------|
|AKSHAT SINGH  |25BCE10857     |

&#10022;The program runs entirely on the command line.

&#10022;No external database is required.

&#10022;CSV file is fully compatible with Excel and Google Sheets.

&#10022;This project is suitable for academic submission or portfolio use.
