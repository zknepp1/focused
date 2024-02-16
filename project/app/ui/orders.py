import tkinter as tk
from tkinter import ttk
import sqlite3
from sql_queries import select_orders



class OrdersPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Orders Page")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Back to Start", command=lambda: controller.show_frame("StartPage"))
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

    def open_add_order_dialog(self):
        AddOrderDialog(self)

    # Database setup
    def get_data(self):
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()
        cursor.execute(select_orders)

        # Fetch all rows from the query result
        data = cursor.fetchall()
        conn.close()

        return data



# Orders (OrderID, CustomerID, JobID, PriceSheetID, items, DatePlaced, TotalAmount, Status)
class AddOrderDialog(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Add New Job")

        # Labels and entry widgets for each field
        tk.Label(self, text="Order Id").pack()  # Label for school name
        self.order_id = tk.Entry(self)
        self.order_id.pack()

        tk.Label(self, text="Customer ID").pack()  # Label for picture date
        self.customer_id = tk.Entry(self)
        self.customer_id.pack()

        tk.Label(self, text="Job ID").pack()  # Label for school location
        self.job_id = tk.Entry(self)
        self.job_id.pack()

        tk.Label(self, text="Price Sheet ID").pack()  # Label for contact number
        self.price_sheet_id = tk.Entry(self)
        self.price_sheet_id.pack()

        tk.Label(self, text="How many items").pack()  # Label for email
        self.items = tk.Entry(self)
        self.items.pack()

        tk.Label(self, text="Date Placed").pack()  # Label for address
        self.date_placed = tk.Entry(self)
        self.date_placed.pack()

        # Add button to submit the form
        add_button = tk.Button(self, text="Add Job", command=self.add_job)
        add_button.pack()

    def add_job(self):
        school_name = self.school_name_entry.get().strip()
        picture_date = self.picture_date_entry.get().strip()  # Ensure this is in the correct TIMESTAMP format
        school_location = self.school_location_entry.get().strip()
        school_contact_number = self.school_contact_number_entry.get().strip()
        school_email = self.school_email_entry.get().strip()
        school_address = self.school_address_entry.get().strip()

        self.master.add_job_to_database(school_name, picture_date, school_location, school_contact_number, school_email, school_address)
        self.destroy()









