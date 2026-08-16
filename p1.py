# root@LiveKit-Server:Python_Projects# cat expense_tracker.py
"""
Expense Tracker
---------------
A simple command-line application to track personal expenses.

Features:
- Add an expense (date, category, amount, description)
- View all expenses
- View total spending
- View spending grouped by category
- Delete an expense
- All data is saved to a CSV file (expenses.csv), so it persists between runs

This project is designed for Python beginners and demonstrates:
- Functions
- File I/O (reading/writing CSV files)
- Lists and dictionaries
- Basic error handling (try/except)
- A simple menu-driven program loop
"""

import csv
import os
from datetime import datetime

# Name of the file where expenses are stored
FILENAME = "expenses.csv"

# Column headers for our CSV file
FIELDNAMES = ["id", "date", "category", "amount", "description"]


def initialize_file():
    """Create the CSV file with headers if it doesn't already exist."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


def load_expenses():
    """Read all expenses from the CSV file and return them as a list of dictionaries."""
    expenses = []
    with open(FILENAME, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert amount back to a float since CSV stores everything as text
            row["amount"] = float(row["amount"])
            row["id"] = int(row["id"])
            expenses.append(row)
    return expenses


def save_all_expenses(expenses):
    """Overwrite the CSV file with the given list of expenses."""
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(expenses)


def get_next_id(expenses):
    """Figure out the next unique ID to use for a new expense."""
    if not expenses:
        return 1
    return max(expense["id"] for expense in expenses) + 1


def add_expense():
    """Prompt the user for expense details and save it to the CSV file."""
    print("\n--- Add New Expense ---")

    # Ask for date, but default to today if the user just presses Enter
    date_input = input("Date (YYYY-MM-DD) [press Enter for today]: ").strip()
    if date_input == "":
        date = datetime.now().strftime("%Y-%m-%d")
    else:
        try:
            # Validate the date format
            datetime.strptime(date_input, "%Y-%m-%d")
            date = date_input
        except ValueError:
            print("Invalid date format. Using today's date instead.")
            date = datetime.now().strftime("%Y-%m-%d")

    category = input("Category (e.g., Food, Travel, Bills): ").strip().title()
    if category == "":
        category = "Uncategorized"

    # Keep asking until the user enters a valid number for amount
    while True:
        amount_input = input("Amount: ").strip()
        try:
            amount = float(amount_input)
            if amount <= 0:
                print("Amount must be greater than 0. Try again.")
                continue
            break
        except ValueError:
            print("That's not a valid number. Please enter a numeric amount.")

    description = input("Description (optional): ").strip()

    expenses = load_expenses()
    new_expense = {
        "id": get_next_id(expenses),
        "date": date,
        "category": category,
        "amount": amount,
        "description": description,
    }
    expenses.append(new_expense)
    save_all_expenses(expenses)

    print(f"\n✅ Expense added: {category} - ${amount:.2f} on {date}")


def view_expenses():
    """Display all recorded expenses in a readable table format."""
    expenses = load_expenses()

    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    print(f"{'ID':<5}{'Date':<12}{'Category':<15}{'Amount':<10}{'Description'}")
    print("-" * 60)
    for expense in expenses:
        print(
            f"{expense['id']:<5}{expense['date']:<12}{expense['category']:<15}"
            f"${expense['amount']:<9.2f}{expense['description']}"
        )


def view_total():
    """Calculate and display the total amount spent across all expenses."""
    expenses = load_expenses()

    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    total = sum(expense["amount"] for expense in expenses)
    print(f"\n💰 Total spending: ${total:.2f}")


def view_by_category():
    """Group expenses by category and show the subtotal for each."""
    expenses = load_expenses()

    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    # Build a dictionary to hold the running total per category
    totals_by_category = {}
    for expense in expenses:
        category = expense["category"]
        totals_by_category[category] = totals_by_category.get(category, 0) + expense["amount"]

    print("\n--- Spending by Category ---")
    for category, total in sorted(totals_by_category.items(), key=lambda x: -x[1]):
        print(f"{category:<15}${total:.2f}")


def delete_expense():
    """Delete an expense by its ID."""
    view_expenses()
    expenses = load_expenses()

    if not expenses:
        return

    try:
        expense_id = int(input("\nEnter the ID of the expense to delete: ").strip())
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    updated_expenses = [e for e in expenses if e["id"] != expense_id]

    if len(updated_expenses) == len(expenses):
        print(f"No expense found with ID {expense_id}.")
        return

    save_all_expenses(updated_expenses)
    print(f"🗑️  Expense with ID {expense_id} deleted.")


def show_menu():
    """Display the main menu options."""
    print("\n" + "=" * 40)
    print("           EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View total spending")
    print("4. View spending by category")
    print("5. Delete an expense")
    print("6. Exit")


def main():
    """Main program loop."""
    initialize_file()

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_total()
        elif choice == "4":
            view_by_category()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            print("\nGoodbye! 👋")
            break
        else:
            print("\nInvalid option. Please choose a number between 1 and 6.")


if __name__ == "__main__":
    main()