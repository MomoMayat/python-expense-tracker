# Personal Expense Tracker

This is a Python tool I built after my first semester of Computer Science to help track daily spending.
It saves data to a file so you don't lose your information when you close the program.

## What it does
- **Saves Expenses:** Stores everything in a `expenses.csv` file.
- **Prevents Errors:** If you type a letter instead of a number for the price, the program won't crash.
- **Search:** You can search for specific categories (like "Food" or "Rent").
- **Totals:** It automatically calculates how much you've spent in total.

## My Learning Goals
I built this to practice:
1. **Working with Files:** Learning how to read and write CSV files.
2. **Loops and Logic:** Using `while` loops for the menu and `if` statements for filtering.
3. **Testing:** I wrote a separate script (`test_tracker.py`) to make sure the "Add Expense" feature works correctly every time.

## How to use it
1. Download the files.
2. Run `python tracker.py` in your terminal.
3. Follow the menu options to add, view, calculate, or filter expenses!

## How to run tests
I included a test file to verify the code:
`python test_tracker.py`