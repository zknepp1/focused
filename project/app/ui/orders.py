import tkinter as tk
from tkinter import ttk
import sqlite3
from sql_queries import select_orders










class OrdersPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Orders Page")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Back to Start",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        data = self.get_data()

        # Create a treeview widget
        treeview = ttk.Treeview(self, columns=("OrderID", "CustomerID", "JobID", "PriceSheetID", "items", "DatePlaced", "TotalAmount", "Status"), show="headings")

        # Define the column headings
        treeview.heading("OrderID", text="Order ID")
        treeview.heading("CustomerID", text="Customer ID")
        treeview.heading("JobID", text="Job ID")
        treeview.heading("PriceSheetID", text="Price Sheet ID")
        treeview.heading("items", text="Items")
        treeview.heading("DatePlaced", text="Date Placed")
        treeview.heading("TotalAmount", text="Total Amount")
        treeview.heading("Status", text="Status")


        # Populate the treeview with sample data
        for job in data:
            treeview.insert('', tk.END, values=job)

        # Arrange the treeview in the main window
        treeview.pack(expand=True, fill='both')



    # Database setup
    def get_data(self):
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()
        cursor.execute(select_orders)

        # Fetch all rows from the query result
        data = cursor.fetchall()
        conn.close()

        return data





#Orders (OrderID, CustomerID, JobID, PriceSheetID, items, DatePlaced, TotalAmount, Status)
'''
data = get_data()

# Create the main window
root = tk.Tk()
root.title("Orders")

# Create a treeview widget
treeview = ttk.Treeview(root, columns=('OrderID', 'CustomerID', 'JobID', 'PriceSheetID', 'items', 'DatePlaced', 'TotalAmount', 'Status'), show="headings")

# Define the column headings
treeview.heading("OrderID", text="Order ID")
treeview.heading("CustomerID", text="Customer ID")
treeview.heading("JobID", text="Job ID")
treeview.heading("PriceSheetID", text="Price Sheet ID")
treeview.heading("items", text="Items")
treeview.heading("DatePlaced", text="Date Order was placed")
treeview.heading("TotalAmount", text="Total Amount")
treeview.heading("Status", text="Status")

# Populate the treeview with sample data
for job in data:
    treeview.insert('', tk.END, values=job)

# Arrange the treeview in the main window
treeview.pack(expand=True, fill='both')

# Start the application
root.mainloop()
'''