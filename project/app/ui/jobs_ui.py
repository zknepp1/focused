import tkinter as tk
from tkinter import ttk
import sqlite3
from sql_queries import select_jobs


# Database setup
def get_data():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute(select_jobs)

    # Fetch all rows from the query result
    data = cursor.fetchall()

    conn.close()

    return data




data = get_data()

# Create the main window
root = tk.Tk()
root.title("Jobs List")

# Create a treeview widget
treeview = ttk.Treeview(root, columns=("JobID", "SchoolName", "pictureDate", "schoolLocation", "schoolContactNumber", "schoolEmail", "schoolAddress"), show="headings")

# Define the column headings
treeview.heading("JobID", text="Job ID")
treeview.heading("SchoolName", text="School Name")
treeview.heading("pictureDate", text="Picture Date")
treeview.heading("schoolLocation", text="School Location")
treeview.heading("schoolContactNumber", text="Contact Number")
treeview.heading("schoolEmail", text="Email")
treeview.heading("schoolAddress", text="Address")

# Populate the treeview with sample data
for job in data:
    treeview.insert('', tk.END, values=job)

# Arrange the treeview in the main window
treeview.pack(expand=True, fill='both')

# Start the application
root.mainloop()