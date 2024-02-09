import tkinter as tk
from tkinter import ttk
import sqlite3
from sql_queries import select_jobs
from tkinter import messagebox
import tkinter.font as tkFont



class JobsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#E1BEE7")
        self.controller = controller
        
        # Use bold font for the page title
        title_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
        label = tk.Label(self, text="Jobs Page", font=title_font, bg="#E1BEE7", fg="#6A1B9A")
        label.grid(row=0, column=0, columnspan=2, pady=10)

        # Organize the layout into frames
        top_frame = tk.Frame(self, bg="#E1BEE7")
        top_frame.grid(row=1, column=0, sticky="ew")
        table_frame = tk.Frame(self, bg="#E1BEE7")
        table_frame.grid(row=2, column=0, sticky="nsew")
        button_frame = tk.Frame(self, bg="#E1BEE7")
        button_frame.grid(row=3, column=0, sticky="ew")

        # Configuring row and column weights for responsiveness
        self.grid_rowconfigure(2, weight=1)  # Make the table frame expandable
        self.grid_columnconfigure(0, weight=1)

        # Search bar in top frame using grid
        search_label = tk.Label(top_frame, text="Search:", bg="#E1BEE7", fg="#6A1B9A")
        search_label.grid(row=0, column=0, padx=5, pady=(0, 5))
        self.search_entry = tk.Entry(top_frame)
        self.search_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=(0, 5))
        button_style = {"bg": "#9C27B0", "fg": "white", "activebackground": "#6A1B9A", "activeforeground": "white"}
        search_button = tk.Button(top_frame, text="Search", command=self.search_jobs, **button_style)
        search_button = tk.Button(top_frame, text="Search", command=self.search_jobs)
        search_button.grid(row=0, column=2, padx=5, pady=(0, 5))
        top_frame.columnconfigure(1, weight=1)


        data = self.get_data()

        # Customizing the treeview
        style = ttk.Style(self)
        style.configure("Treeview", background="#E1BEE7", fieldbackground="#E1BEE7", foreground="#6A1B9A")
        style.configure("Treeview.Heading", background="#9C27B0", foreground="white")



        # Create a treeview widget
        treeview = ttk.Treeview(self, columns=("JobID", "SchoolName", "pictureDate", "schoolLocation", "schoolContactNumber", "schoolEmail", "schoolAddress"), show="headings")

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

        # In the __init__ method, bind the double-click event
        treeview.bind("<Double-1>", self.on_job_select)


        # Arrange the treeview in the table_frame using grid
        treeview.grid(row=0, column=0, sticky='nsew')
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
        self.treeview = treeview

        # Buttons in button frame using grid
        back_button = tk.Button(button_frame, text="Back to Start", command=lambda: controller.show_frame("StartPage"), **button_style)
        back_button.grid(row=0, column=0, padx=10, pady=10)
        edit_button = tk.Button(button_frame, text="Edit Selected Job", command=self.edit_job, **button_style)
        edit_button.grid(row=0, column=1, padx=10, pady=10)
        refresh_button = tk.Button(button_frame, text="Refresh", command=self.refresh_data, **button_style)
        refresh_button.grid(row=0, column=2, padx=10, pady=10)

    def on_job_select(self, event):
        selected_item = self.treeview.selection()
        if selected_item:
            job_id = self.treeview.item(selected_item)['values'][0]
            # Assuming you have a method in your controller to show the AccountInfoPage
            self.controller.show_account_info_page(job_id)

    # Database setup
    def get_data(self):
        try:
            conn = sqlite3.connect('example.db')
            cursor = conn.cursor()
            cursor.execute(select_jobs)
            data = cursor.fetchall()
        except sqlite3.Error as e:
            tk.messagebox.showerror("Database Error", str(e))
            data = []
        finally:
            conn.close()
        return data
    
    def search_jobs(self, event=None):
        search_query = self.search_entry.get()


    def edit_job(self):
        selected_item = self.treeview.selection()
        if selected_item:
            # Assuming the first column in your TreeView is the job's ID
            job_id = self.treeview.item(selected_item)['values'][0]
            EditJobDialog(self, job_id)

    def refresh_data(self):
        self.treeview.delete(*self.treeview.get_children())
        data = self.get_data()
        for job in data:
            self.treeview.insert('', tk.END, values=job)




class EditJobDialog(tk.Toplevel):
    def __init__(self, parent, job_id):
        tk.Toplevel.__init__(self, parent)
        
        self.job_id = job_id
        self.title("Edit Job")

        # Retrieve current job data from database
        self.current_data = self.get_current_data(job_id)

        # Create entry widgets for each field
        self.school_name_entry = tk.Entry(self)
        self.picture_date_entry = tk.Entry(self)
        self.picture_date_entry.insert(1, self.current_data[2])
        self.school_name_entry.insert(0, self.current_data[1])
        self.picture_date_entry.pack()
        self.school_name_entry.pack()

        # ... Create similar entry widgets for other fields ...

        save_button = tk.Button(self, text="Save Changes", command=self.save_changes)
        save_button.pack()

    def get_current_data(self, job_id):
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM jobs WHERE JobID = ?", (job_id,))
        data = cursor.fetchone()
        conn.close()
        return data  # Assuming data is a dictionary

    def save_changes(self):
        updated_school_name = self.school_name_entry.get().strip()
        updated_picture_date = self.picture_date_entry.get()

        # Update the database
        try:
            conn = sqlite3.connect('example.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE jobs SET SchoolName = ?, PictureDate = ? WHERE JobID = ?", (updated_school_name, updated_picture_date, self.job_id))
            conn.commit()
        except sqlite3.Error as e:
            tk.messagebox.showerror("Database Error", str(e))
        finally:
            conn.close()

        # Refresh the data in the main JobsPage
        self.master.get_data()
        self.destroy()


