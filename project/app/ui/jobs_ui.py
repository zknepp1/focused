import tkinter as tk
from tkinter import ttk
import sqlite3
from sql_queries import select_jobs, select_all_jobs_school
from tkinter import messagebox
import tkinter.font as tkFont
from tkinter import filedialog
import pandas as pd

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
        self.row_count = len(data)

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

        # Add a job button
        add_job_button = tk.Button(button_frame, text="Add New Job", command=self.open_add_job_dialog, **button_style)
        add_job_button.grid(row=0, column=3, padx=10, pady=10)

        # Import jobs from excel or csv
        import_job_button = tk.Button(button_frame, text="Import Jobs From File", command=self.open_import_jobs_dialog, **button_style)
        import_job_button.grid(row=0, column=4, padx=10, pady=10)

        # Add a delete button
        delete_button = tk.Button(button_frame, text="Delete Job", command=self.delete_selected_job, **button_style)
        delete_button.grid(row=0, column=5, padx=10, pady=10)


    def delete_selected_job(self):
        selected_job_id = self.get_selected_job_id()
        if selected_job_id is not None:
            if self.delete_job_from_database(selected_job_id):  # Check if deletion was successful
                messagebox.showinfo("Success", f"Job {selected_job_id} has been deleted.")
                self.update_jobs_list()
            else:
                messagebox.showerror("Error", "Failed to delete the job.")
        else:
            messagebox.showwarning("Selection Error", "Please select a job to delete.")


    def get_selected_job_id(self):
        # Get the item that is currently selected in the treeview
        selection = self.treeview.selection()
        
        if selection:  # If there is a selection
            # Get the first (and ideally, only) item in the selection
            item = selection[0]
            # Retrieve the job ID from the values of the selected item
            selected_job_id = self.treeview.item(item, 'values')[0]
            return selected_job_id
        else:  # If nothing is selected
            messagebox.showwarning("Selection Error", "No job selected.")
            return None


    def delete_job_from_database(self, selected_job_id):
        try:
            conn = sqlite3.connect('example.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Jobs WHERE JobID = ?;", (selected_job_id,))
            conn.commit()  # Commit the transaction
        except sqlite3.Error as e:
            tk.messagebox.showerror("Database Error", str(e))
            return False  # Return False on error
        finally:
            conn.close()
        return True


    def update_jobs_list(self):
        # Clear the current content of the treeview
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        
        # Fetch the updated list of jobs from the database
        new_data = self.get_data()
        
        # Re-populate the treeview with the new data
        for job in new_data:
            self.treeview.insert('', 'end', values=job)


    def on_job_select(self, event):
        selected_item = self.treeview.selection()
        if selected_item:
            job_id = self.treeview.item(selected_item)['values'][0]
            school_name = self.treeview.item(selected_item)['values'][1]
            #print(self.treeview.item(selected_item)['values'])
            # Create a new Toplevel window
            detail_window = tk.Toplevel(self)
            detail_window.title("Job Details")
            
            # Fetch the job's data from the database
            job_data = self.get_job_data(school_name)

            # Display the job's data in labels or any other widgets
            for i, (key, value) in enumerate(job_data.items()):
                label = tk.Label(detail_window, text=f"{key}: {value}")
                label.grid(row=i, column=0, sticky="w")


    def get_job_data(self, school_name):
        try:
            conn = sqlite3.connect('example.db')
            cursor = conn.cursor()
            cursor.execute(select_all_jobs_school, (school_name,))
            data = cursor.fetchone()
            print(data)
            # Convert the data to a dictionary or any other format that's easy to display
            data_dict = {"School Name": data[0], "School Location": data[1], "School Contact Number": data[2], "School Address": data[3], "Number of Jobs": data[4]} # and so on for other fields
            return data_dict
        except sqlite3.Error as e:
            tk.messagebox.showerror("Database Error", str(e))
            return {}
        finally:
            conn.close()


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

    def add_job_to_database(self, school_name, picture_date, school_location, school_contact_number, school_email, school_address):
        try:
            conn = sqlite3.connect('example.db')
            cursor = conn.cursor()
            #adding 1 to the row count
            self.row_count = self.row_count + 1
            cursor.execute("INSERT INTO jobs (JobID, SchoolName, PictureDate, SchoolLocation, SchoolContactNumber, SchoolEmail, SchoolAddress) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (self.row_count, school_name, picture_date, school_location, school_contact_number, school_email, school_address))
            conn.commit()
        except sqlite3.Error as e:
            tk.messagebox.showerror("Database Error", str(e))
        finally:
            conn.close()

    def open_import_jobs_dialog(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
        if filename:
            self.import_jobs_from_file(filename)


    def import_jobs_from_file(self, filename):
        # Read the file using pandas
        if filename.endswith('.csv'):
            df = pd.read_csv(filename)
        else:
            df = pd.read_excel(filename)
        
        # Connect to the SQLite database
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()

        # Iterate over DataFrame and insert data
        for _, row in df.iterrows():
            picture_date_str = row['PictureDate'].strftime('%Y-%m-%d %H:%M:%S') if pd.notnull(row['PictureDate']) else None
            self.row_count = self.row_count + 1
            cursor.execute("INSERT INTO jobs (JobID, SchoolName, PictureDate, SchoolLocation, SchoolContactNumber, SchoolEmail, SchoolAddress) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (self.row_count, row['SchoolName'], picture_date_str, row['SchoolLocation'], row['SchoolContactNumber'], row['SchoolEmail'], row['SchoolAddress']))
        
        conn.commit()
        conn.close()

        # Refresh the data display
        self.refresh_data()


    def open_add_job_dialog(self):
        AddJobDialog(self)



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



class AddJobDialog(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Add New Job")

        # Labels and entry widgets for each field
        tk.Label(self, text="School Name").pack()  # Label for school name
        self.school_name_entry = tk.Entry(self)
        self.school_name_entry.pack()

        tk.Label(self, text="Picture Date").pack()  # Label for picture date
        self.picture_date_entry = tk.Entry(self)
        self.picture_date_entry.pack()

        tk.Label(self, text="School Location").pack()  # Label for school location
        self.school_location_entry = tk.Entry(self)
        self.school_location_entry.pack()

        tk.Label(self, text="School Contact Number").pack()  # Label for contact number
        self.school_contact_number_entry = tk.Entry(self)
        self.school_contact_number_entry.pack()

        tk.Label(self, text="School Email").pack()  # Label for email
        self.school_email_entry = tk.Entry(self)
        self.school_email_entry.pack()

        tk.Label(self, text="School Address").pack()  # Label for address
        self.school_address_entry = tk.Entry(self)
        self.school_address_entry.pack()

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


