import tkinter as tk


class NonParentPickupScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        self.name_label = tk.Label(
            self,
            text="Name of non-parent"
        )
        self.name_label.grid(row=0, column=0, pady=10)

        self.name_entry = tk.Entry(
            self
        )
        self.name_entry.grid(row=0, column=1, columnspan=5, pady=10)

        self.employee_id_label = tk.Label(
            self,
            text="Employee ID"
        )

        self.employee_id_label.grid(row=1, column=0, pady=10)

        self.keyfab_inp = tk.Entry(
            self
        )
        self.keyfab_inp.grid(row=1, column=1, pady=10)

        self.authorize_btn = tk.Button(
            self,
            text="Employee Authorize",
            command = self.authorize
        )
        self.authorize_btn.grid(row=2, column=0, pady=50, padx=10)

        self.back_to_main_btn = tk.Button(
            self,
            text="Back to main screen",
            command = lambda : controller.show_frame("Mainscreen")
        )

        self.back_to_main_btn.grid(row=2, column=1, pady=50, padx=100)

    def authorize(self):
        found_Employee = None
        for employee in self.controller.employees:
            if employee.key_fob == self.keyfab_inp.get():
                found_Employee = employee
        
        if found_Employee:
            self.keyfab_inp.select_clear()
            self.controller.frames["CildrenInOutScreen"].initiate_transistion(self.name_entry.get())
            self.controller.show_frame("CildrenInOutScreen")
        else:
            print("unkonw keyfob:" + self.keyfab_inp.get())
            self.keyfab_inp.select_clear()

