import tkinter as tk

class AccountInfoPage(tk.Frame):
    def __init__(self, parent, controller, job_id=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.job_id = job_id

        #print(controller)
        # Add widgets to display account information
        # ...