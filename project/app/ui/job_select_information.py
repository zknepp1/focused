import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import pandas as pd

from sql_queries import select_students_from_job_id


"""CREATE TABLE `Students` (
   `StudentID` INTEGER PRIMARY KEY,
   `fname` VARCHAR(255),
   `lname` VARCHAR(255),
   `teacher` VARCHAR(255),
   `GradeOrClass` VARCHAR(255),
   `JobID` INTEGER,
   FOREIGN KEY (`JobID`) REFERENCES `Jobs` (`JobID`)
   );"""



class JobDetailWindow(tk.Toplevel):
    def __init__(self, parent, job_id, school_name):
        super().__init__(parent)
        self.job_id = job_id
        self.school_name = school_name
        self.student_info = self.get_student_data_by_job(job_id)

        # Display job information
        tk.Label(self, text=f"Job ID: {self.job_id}, School: {self.school_name}").pack()

        # Student detail labels and entry fields
        tk.Label(self, text="First Name:").pack()
        self.fname_entry = tk.Entry(self)
        self.fname_entry.pack()

        tk.Label(self, text="Last Name:").pack()
        self.lname_entry = tk.Entry(self)
        self.lname_entry.pack()

        tk.Label(self, text="Teacher:").pack()
        self.teacher_entry = tk.Entry(self)
        self.teacher_entry.pack()

        tk.Label(self, text="Grade/Class:").pack()
        self.grade_class_entry = tk.Entry(self)
        self.grade_class_entry.pack()

        tk.Label(self, text="Student ID:").pack()
        self.student_id = tk.Entry(self)
        self.student_id.pack()

        # Button to add student
        tk.Button(self, text="Add Student", command=self.add_student).pack()

        # Initialize the tree view
        self.setup_tree_view()



    def setup_tree_view(self):
        # Define columns
        columns = ('student_id', 'first_name', 'last_name', 'teacher', 'grade_class')

        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.heading('student_id', text='Student ID')
        self.tree.heading('first_name', text='First Name')
        self.tree.heading('last_name', text='Last Name')
        self.tree.heading('teacher', text='Teacher')
        self.tree.heading('grade_class', text='Grade/Class')

        # Arrange the tree view
        self.tree.pack(expand=True, fill='both')

        # Populate the tree view with data
        self.populate_tree_view()


    def populate_tree_view(self):
        # Clear existing data in the tree
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Fetch data from database
        students = self.get_student_data_by_job(self.job_id)

        # Insert data into tree view
        for student in students:
            self.tree.insert('', 'end', values=student)


    def get_student_data_by_job(self, job_id):
        try:
            conn = sqlite3.connect('example.db')
            cursor = conn.cursor()
            cursor.execute(select_students_from_job_id, (job_id,))
            data = cursor.fetchall()  # Retrieve all rows of data
            return data
        except sqlite3.Error as e:
            tk.messagebox.showerror("Database Error", str(e))
            return []
        finally:
            conn.close()






    def add_student(self):
        # Gather student details from the entry fields
        student_details = {
            'fname': self.fname_entry.get(),
            'lname': self.lname_entry.get(),
            'teacher': self.teacher_entry.get(),
            'GradeOrClass': self.grade_class_entry.get()
        }

        # Call the method to add student to the database
        self.add_student_to_job('example.db', student_details, self.job_id)


        
    def add_student_to_job(self, database_path, student_details, job_id):
        try:
            conn = sqlite3.connect(database_path)
            cursor = conn.cursor()
            insert_query = '''INSERT INTO Students(fname, lname, teacher, GradeOrClass, JobID)
                              VALUES(?,?,?,?,?)'''
            student_data = (student_details['fname'], student_details['lname'], 
                            student_details['teacher'], student_details['GradeOrClass'], job_id)
            cursor.execute(insert_query, student_data)
            conn.commit()
            print("Student added successfully.")
        except sqlite3.Error as e:
            tk.messagebox.showerror("Database Error", str(e))
        finally:
            conn.close()






