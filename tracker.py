import csv
import os


# 1. Add an Expense(Amount + Category)
# This is the write(output) function
# Example: add_expense(20.50, "Food")
def add_expense(amount, category):
    file_exists = os.path.isfile('expenses.csv')

    with open('expenses.csv', mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        if not file_exists or os.path.getsize('expenses.csv') == 0:
            writer.writerow(['Amount', 'Category'])

        writer.writerow([amount, category])

    print(f'Successfully added ${amount:.2f} under {category}!')
    # .2f is to display currency correctly with two decimal places
    # (e.g. $20.50 instead of $20.5)


# 2. View All Expenses
# This is the read(input) function
def view_expenses():
    if not os.path.isfile('expenses.csv') or os.path.getsize('expenses.csv') == 0:
        print('\nNo expenses found!')
        return

    print("\n-----Your Expenses-----")

    with open('expenses.csv', mode='r') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
        # Each row is a list (e.g. [20.5, "Food"])
            if row == ['Amount', 'Category']:
                print(f"\n{row[0]:<10} | {row[1]}")
            # prints the header 'Amount' without $ in front
            # :<10 is to add padding so that the amount column stays uniform
            else:
                print(f"\n${float(row[0]):<9.2f} | {row[1]}")
    print("\n-----------------------")


# 3. Calculate Total Spending
def total_expenses():
    if not os.path.isfile('expenses.csv') or os.path.getsize('expenses.csv') == 0:
        print('\nNo expenses found!')
        return

    total = 0

    with open('expenses.csv', mode='r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        # next function skips the header of the csv

        for row in reader:
            total += float(row[0])

        print(f"\nTotal Expenses: ${total:.2f}")


# 4. Filter by Category
def filter_by_category():
    if not os.path.isfile('expenses.csv') or os.path.getsize('expenses.csv') == 0:
        print('\nNo expenses found!')
        return

    search_term = input("Which category do you want to search for?: ").strip()

    print(f"\n--- Expenses for '{search_term}' ---")

    with open('expenses.csv', mode='r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        # next function skips the header of the csv

        found = False
        for row in reader:
            if row[1].lower() == search_term.lower():
                print(f"\n${float(row[0]):<9.2f} | {row[1]}")
                found = True

        if not found:
            print(f"\nNo expenses found in that category.")

    print("\n--------------------------")

# Main Menu
# This is the main loop
while True:
    print ("\n\033[1mPersonal Expense Tracker\033[0m")
    # used ANSI codes for bold text
    print ("\n1. Add Expense")
    print ("2. View All Expenses")
    print ("3. Total Expenses")
    print ("4. Search Expenses by Category")
    print ("5. Exit")

    choice = input("\nSelect an option(type either 1, 2, 3, 4, or 5): ").strip()

    if choice == '1':
        try:
            amt = float(input("Enter Amount: "))
            cat = input("Enter Category: ").strip()
            add_expense(amt, cat)
        except ValueError:
            print("\nError: Please enter a number for the amount (e.g., 20.50).")

    elif choice == '2':
        view_expenses()

    elif choice == '3':
        total_expenses()

    elif choice == '4':
        filter_by_category()

    elif choice == '5':
        print("\nThank you for using the Personal Expense Tracker!")
        break

    else:
        print ("\nInvalid choice, please try again.")