# Budget Tracker (Console Based Application)

## Description
- A console-based budget tracker using python that helps you manage your finances by keeping track of incomes and expenses. 
- This application stores your transactions in a local file (transactions.txt) and provides a simple command-line interface (CLI) for all operations.

-------

## Features
- Add transactions — Track both incomes and expenses, assign categories, and add optional notes.
- List all transactions — See your complete ledger in a neat table.
- Filter transactions — By type (income or expense) and by category.
- View summary — Display your total income, expenses, and current balance.
- Persistent storage — All data is automatically saved and loaded from transactions.txt.

--------

## Requirements
- Python 3


------

## How to Run
1. Clone or Download the Project
2. Save the file budget_tracker.py in a folder on your computer.
3. Launch the Program

Open your terminal, navigate to the folder containing budget_tracker.py, then run:
```
python budget_tracker.py
or
py budget_tracker.py
```
(Use python3 instead of python on some systems, or py on Windows if the previous doesn't work.)

4.Follow the Menu
You'll see a menu like:
```
----- Budget Tracker Menu -----
1. Add a Transaction
2. List All Transactions
3. Filter Transactions
4. View Summary
5. Save and Exit
------------------------------
Select an option (1-5):
```

-------

## How to Use the Features

- Pick an option by entering its number, then follow prompts.
- When you’re done, choose "Save and Exit" to store your data in transactions.txt.
- On your next run, the program will auto-load your transactions that you saved previously.

  
## Note
- The transactions file (transactions.txt) will be created in the same folder as the Python script after you save your first transaction.
- If you want to start fresh, simply delete the transactions.txt file.
