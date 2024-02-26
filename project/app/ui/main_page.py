import tkinter as tk
import tkinter.font as tkFont
import sqlite3

from sql_queries import delete_database, create_database

class StartPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.configure(bg="#E1BEE7")  # Light purple background

        welcome_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
        button_font = tkFont.Font(family="Helvetica", size=12)
        
        # Welcome label
        label = tk.Label(self, text="Welcome to the Application", font=welcome_font, bg="#E1BEE7", fg="#6A1B9A")
        label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        # Button style
        button_style = {"bg": "#9C27B0", "fg": "white", "font": button_font, "activebackground": "#6A1B9A", "activeforeground": "white"}

        # Buttons
        button1 = tk.Button(self, text="Jobs", command=lambda: controller.show_frame("JobsPage"), **button_style)
        button1.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        button2 = tk.Button(self, text="Price Sheets", command=lambda: controller.show_frame("PricesheetsPage"), **button_style)
        button2.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        button3 = tk.Button(self, text="Orders", command=lambda: controller.show_frame("OrdersPage"), **button_style)
        button3.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        # Configure grid rows and columns
        self.grid_columnconfigure(0, weight=1)
        for i in range(4):
            self.grid_rowconfigure(i, weight=1)



    def delete_database(self):
        try:
            conn = sqlite3.connect('example.db')
            cursor = conn.cursor()
            for i in delete_database:
                cursor.execute(i)
                conn.commit()  # Commit the transaction
        except sqlite3.Error as e:
            tk.messagebox.showerror("Database Error", str(e))
            return False  # Return False on error
        finally:
            conn.close()
        return True

            