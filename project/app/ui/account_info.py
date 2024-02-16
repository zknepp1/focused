import tkinter as tk
import sqlite3
from sql_queries import select_jobs

class AccountInfoPage(tk.Frame):
    def __init__(self, parent, controller, job_id=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.job_id = job_id

        # Example data (you will replace this with actual data retrieval logic)
        self.job_data = self.get_data(job_id)

        # Display job information
        tk.Label(self, text="Job ID:").grid(row=0, column=0, sticky="w")
        self.job_id_entry = tk.Entry(self)
        self.job_id_entry.grid(row=0, column=1)
        self.job_id_entry.insert(0, self.job_data.get("JobID", ""))
        self.job_id_entry.configure(state="readonly")

        tk.Label(self, text="School Name:").grid(row=1, column=0, sticky="w")
        self.school_name_entry = tk.Entry(self)
        self.school_name_entry.grid(row=1, column=1)
        self.school_name_entry.insert(0, self.job_data.get("SchoolName", ""))
        self.school_name_entry.configure(state="readonly")

        # ... Repeat for other pieces of data ...



        # Database setup
    def get_data(self):
        try:
            conn = sqlite3.connect('example.db')
            cursor = conn.cursor()
            cursor.execute(select_jobs)
            data = cursor.fetchall()
            print(data)
        except sqlite3.Error as e:
            tk.messagebox.showerror("Database Error", str(e))
            data = []
        finally:
            conn.close()
        return data


