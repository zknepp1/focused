import tkinter as tk
import sqlite3
from tkinter import messagebox

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



    def get_student_data_by_job(self, job_id):
        try:
            conn = sqlite3.connect('example.db')
            cursor = conn.cursor()
            cursor.execute(select_students_from_job_id, (job_id,))
            data = cursor.fetchone()
            # Convert the data to a dictionary or any other format that's easy to display
            #data_dict = {"School Name": data[0], "School Location": data[1], "School Contact Number": data[2], "School Address": data[3], "Number of Jobs": data[4]} # and so on for other fields
            return data
        except sqlite3.Error as e:
            tk.messagebox.showerror("Database Error", str(e))
            return {}
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


        
    def add_student_to_job(database_path, student_details, job_id):
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('example.db')
            cursor = conn.cursor()

            # SQL query to insert a new student
            insert_query = ''' INSERT INTO Students(fname, lname, teacher, GradeOrClass, JobID)
                            VALUES(?,?,?,?,?) '''
            student_data = (student_details['fname'], student_details['lname'], student_details['teacher'], student_details['GradeOrClass'], job_id)

            # Execute the query and commit the changes
            cursor.execute(insert_query, student_data)
            conn.commit()
            print("Student added successfully.")

        except sqlite3.Error as e:
            tk.messagebox.showerror("Database Error", str(e))
            return {}
        finally:
            conn.close()

"""CREATE TABLE `Students` (
   `StudentID` INTEGER PRIMARY KEY,
   `fname` VARCHAR(255),
   `lname` VARCHAR(255),
   `teacher` VARCHAR(255),
   `GradeOrClass` VARCHAR(255),
   `JobID` INTEGER,
   FOREIGN KEY (`JobID`) REFERENCES `Jobs` (`JobID`)
   );"""