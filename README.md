# Personal Finance Tracker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)  
[![GitHub Stars](https://img.shields.io/github/stars/yourusername/repo?style=social)](https://github.com/NevigChanuka/Personal-Financial-Tracker)  


## Description

A Python-based application to manage financial transactions effectively. Features include:

1. Add single/bulk transactions
2. View transactions via GUI or CLI
3. Update/delete transactions
4. Display summary reports

## Prerequisites

- Python 3.x installed
- Files: `Personal Financial Tracker.py`, `GUI.py`, `transactions.json`

### Installing Python

1. Download Python from **[python.org](https://www.python.org/)**.
2. Run the installer and ensure Python is added to PATH.

## How to Run

1. Download the project files.
2. Place all files in the same folder.
3. Run: 
```cmd
python "Personal Financial Tracker.py"
```
## Main Menu Options

1. Add Transaction: Enter expense type, amount, and date (`YYYY-MM-DD`).
2. Add Bulk Transactions: Import from a text file (`format: Expense,Amount,Date`).
3. View Transactions (GUI): Displays data in a searchable/sortable table.
4. View Transactions (CLI): Displays data in the command line.
5. Update Transaction: Modify amount or date by row number.
6. Delete Transaction: Remove a transaction by row number.
7. Transactions Summary: Shows total transactions, expense types, and total amount.
8. Exit: Close the program.

### Bulk Transaction Text File Format

```
Groceries,1000,2024-04-10  
Shopping,5000,2024-04-12  
```
_Ensure commas separate fields and each transaction is on a new line._

## GUI Features

- __Search__: Enter keywords in the search bar.
- __Sort__: Click column headers (Category/Amount/Date).
- __Table View__: Displays all transactions from `transactions.json`.

### Design Choices

- __Tkinter__: Standard Python GUI toolkit.
- __JSON Storage__: Lightweight and easy to manipulate.

## License
MIT © Nevig Chanuka
