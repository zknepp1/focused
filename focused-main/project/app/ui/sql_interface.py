import tkinter as tk
from tkinter import scrolledtext, messagebox
import sqlite3

from sql_queries import create_database, test_data, select_photographers
from sql_queries import select_customers, select_jobs, select_students_grades
from sql_queries import select_students_parents, select_orders_by_customer, select_price_sheets
from sql_queries import select_barcodes_students, select_orders_revenue, select_all_jobs_school


# Database setup
def create_db():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    for i in create_database:
        try:
            cursor.execute(i)
        except Exception as e:
            print('An error occured: ', e)

    for i in test_data:
        try:
            cursor.execute(i)
        except Exception as e:
            print('An error occured: ', e)
            
    conn.commit()
    conn.close()

# Function to execute query from the user input
def execute_query():
    query = query_input.get("1.0", tk.END).strip()
    if query:
        try:
            conn = sqlite3.connect('example.db')
            cursor = conn.cursor()
            cursor.execute(query)
            if query.lower().startswith("select"):
                results = cursor.fetchall()
                result_text.delete('1.0', tk.END)
                for row in results:
                    result_text.insert(tk.END, str(row) + '\n')
            else:
                conn.commit()
                result_text.delete('1.0', tk.END)
                result_text.insert(tk.END, "Query executed successfully.")
            cursor.close()
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            conn.close()
    else:
        messagebox.showwarning("Warning", "Please enter a SQL query.")

# Tkinter UI setup
app = tk.Tk()
app.title("Database Query Executor")

# Query Input
query_input = scrolledtext.ScrolledText(app, height=8)
query_input.pack(pady=10)

# Execute Button
execute_button = tk.Button(app, text="Execute Query", command=execute_query)
execute_button.pack(pady=5)

# Query Result Display
result_text = scrolledtext.ScrolledText(app, height=8)
result_text.pack(pady=10)

# Initialize Database
create_db()

# Start the application
app.mainloop()