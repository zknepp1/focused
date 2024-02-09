import tkinter as tk
from tkinter import messagebox
from main_page import StartPage
from jobs_ui import JobsPage
from pricesheets_ui import PricesheetsPage
from orders import OrdersPage
from account_info import AccountInfoPage

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("My Application")  # Set the window title
        self.geometry("800x600")  # Set the size of the main application window

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

app = SampleApp()
app.mainloop()




