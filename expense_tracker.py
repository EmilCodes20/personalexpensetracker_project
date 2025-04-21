# expense_tracker.py
import sqlite3
from datetime import datetime

DB_NAME = 'expenses.db'

def add_expense(date, category, amount, description):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO expenses (date, category, amount, description)
        VALUES (?, ?, ?, ?)
    ''', (date, category, amount, description))
    conn.commit()
    conn.close()

def view_expenses():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT * FROM expenses ORDER BY date DESC')
    rows = c.fetchall()
    conn.close()
    for row in rows:
        print(row)

# Lav Update formel og Delete formel
def update_expense(expense_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

# Example usage
if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            date = input("Date (YYYY-MM-DD): ") or datetime.now().strftime('%Y-%m-%d')
            category = input("Category: ")
            amount = float(input("Amount: "))
            description = input("Description: ")
            add_expense(date, category, amount, description)
        elif choice == "2":
            view_expenses()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
