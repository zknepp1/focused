import tkinter as tk
from tkinter import ttk
import sqlite3
from sql_queries import select_price_sheets



class PricesheetsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Price Sheets")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Back to Start",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        data = self.get_data()

        # Create a treeview widget
        treeview = ttk.Treeview(self, columns=("PriceSheetID", "ItemDescription", "Price", "SizeOrFormat", "Discount"), show="headings")

        # Define the column headings
        treeview.heading("PriceSheetID", text="Price Sheet ID")
        treeview.heading("ItemDescription", text="Description")
        treeview.heading("Price", text="Price")
        treeview.heading("SizeOrFormat", text="Size or Format")
        treeview.heading("Discount", text="Discount")

        # Populate the treeview with sample data
        for job in data:
            treeview.insert('', tk.END, values=job)

        # Arrange the treeview in the main window
        treeview.pack(expand=True, fill='both')


    # Database setup
    def get_data(self):
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()
        cursor.execute(select_price_sheets)

        # Fetch all rows from the query result
        data = cursor.fetchall()
        conn.close()

        return data






'''
data = get_data()

# Create the main window
root = tk.Tk()
root.title("Price Sheets")

# Create a treeview widget
treeview = ttk.Treeview(root, columns=("PriceSheetID", "ItemDescription", "Price", "SizeOrFormat", "Discount"), show="headings")



# Define the column headings
treeview.heading("PriceSheetID", text="Price Sheet ID")
treeview.heading("ItemDescription", text="Description")
treeview.heading("Price", text="Price")
treeview.heading("SizeOrFormat", text="Size or Format")
treeview.heading("Discount", text="Discount")

# Populate the treeview with sample data
for job in data:
    treeview.insert('', tk.END, values=job)

# Arrange the treeview in the main window
treeview.pack(expand=True, fill='both')

# Start the application
root.mainloop()


'''