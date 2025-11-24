<h3> Project Statement<>
🔍 Problem Statement

Managing daily expenses is often difficult for students and individuals who do not use full-scale finance apps. Tracking spending manually becomes messy, and users lack a simple way to analyze where their money goes.
There is a need for a lightweight, offline, and easy-to-use tool that helps users record expenses, view trends, and analyze spending patterns without requiring advanced accounting knowledge.

🎯 Scope of the Project

This project focuses on building a local, command-line expense tracker that stores all data permanently in a CSV file. The system provides essential expense-management features including adding, viewing, filtering, deleting, analyzing, and visualizing expenses.

The scope includes:

Data entry and secure local storage

Filtering and organizing expenses

Generating summaries and statistics

Visualizing category-wise spending

Ensuring fully offline usage without dependencies on online services

The project does not aim to be a full financial planner, multi-user system, or cloud-based service.

👥 Target Users

This project is designed for:

Students who want to track daily spending (food, travel, shopping, etc.)

Individuals seeking a simple, offline financial tracker

Beginners in Python who want to learn file handling, data processing, and visualization

Users who prefer privacy, since all data is stored locally

People who want insights into their monthly and category-wise expenses without complex apps

⭐ High-Level Features

Add Expenses
Input date, category, amount, and notes with input validation.

View All Expenses
Display expenses with index numbers for easy management.

Delete Expenses
Remove entries using their index.

Filter Options

View by category

View by date range

Statistics Module

Total spending

Average spending

Spending per category

Number of transactions per category

Highest spending category

Monthly spending summary

Data Visualization
Category-wise bar chart using Matplotlib.

Persistent Storage
All data saved in data/expenses.csv and auto-created if missing.
