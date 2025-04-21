
import sqlite3
import csv

DB_NAME = 'expenses.db'

def export_to_csv(filename='expenses.csv'):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT * FROM expenses')
    rows = c.fetchall()
    conn.close()

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Date', 'Category', 'Amount', 'Description'])
        writer.writerows(rows)
    print(f"Exported to {filename}")

def view_summary_by_category():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT category, SUM(amount) FROM expenses GROUP BY category')
    rows = c.fetchall()
    conn.close()
    
    print("\nSpending by Category:")
    for category, total in rows:
        print(f"{category}: ${total:.2f}")
