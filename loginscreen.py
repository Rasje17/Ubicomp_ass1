import tkinter as tk
class Loginscreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller=controller

        self.instructiion_label = tk.Label(
            self,
            text = "enter username and password below to log in"
        )
        self.instructiion_label.grid(row=0, column=0, columnspan=5, sticky="nesw")

        self.username_lbl =tk.Label(
            self,
            text="username"
        )
        self.username_lbl.grid(row=1, column=0)

        self.username_entry=tk.Entry(
            self
        )
        self.username_entry.grid(row=1, column=2)
        
        self.pw_label=tk.Label(
            self,
            text="password"
        )
        self.pw_label.grid(row=2,column=0)

        self.pw_entry=tk.Entry(
            self
        )
        self.pw_entry.grid(row=2,column=2)

        self.login_btn = tk.Button(
            self,
            text= "Login",
            command = self.login
        )
        self. login_btn.grid(row=3, column=1)

        self.mainscreen_btn = tk.Button(
            self,
            text ="return to main screen",
            command = lambda : controller.show_frame("Mainscreen")
        )
        self.mainscreen_btn.grid(row=3, column=3)
    
    
    def login(self):
        #implement login feature somehow
        #send to controller.show_frame("CildrenInOutScreen")
        self.controller.show_frame("CildrenInOutScreen")