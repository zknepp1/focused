import tkinter as tk
from tkinter import messagebox
from main_page import StartPage
from jobs_ui import JobsPage
from pricesheets_ui import PricesheetsPage
from orders import OrdersPage
from account_info import AccountInfoPage
import sqlite3

from sql_queries import create_database



class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # CREATES THE DATABASE
        #self.create_database()

        self.title("My Application")  # Set the window title
        self.geometry("1200x1000")  # Set the size of the main application window

        # Create a menu bar
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        # Add menu items
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, JobsPage, PricesheetsPage, OrdersPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            frame.grid(row=0, column=0, sticky="nsew")
            frame.grid_rowconfigure(0, weight=1)
            frame.grid_columnconfigure(0, weight=1)
            self.frames[page_name] = frame

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def show_account_info_page(self, job_id):
        if "AccountInfoPage" not in self.frames:
            self.frames["AccountInfoPage"] = AccountInfoPage(parent=self.container, controller=self, job_id=job_id)
            self.frames["AccountInfoPage"].grid(row=0, column=0, sticky="nsew")

        self.frames["AccountInfoPage"].job_id = job_id  # Update job_id each time
        self.frames["AccountInfoPage"].update_info()  # Assuming you have this method to update info based on job_id
        self.show_frame("AccountInfoPage")


    def create_database(self):
        conn = None
        try:
            conn = sqlite3.connect('example.db')
            cursor = conn.cursor()

            for command in create_database:
                try:
                    cursor.execute(command)
                except sqlite3.Error as e:
                    # Show error for the specific command
                    tk.messagebox.showerror("Database Command Error", f"Error in SQL command: {command}\nError message: {str(e)}")
                    continue  # Skip to the next command

            conn.commit()  # Commit the transaction after all commands are attempted
        except sqlite3.Error as e:
            tk.messagebox.showerror("Database Connection Error", str(e))
            return False  # Return False on database connection error
        finally:
            if conn:
                conn.close()
        return True



app = SampleApp()
app.mainloop()


