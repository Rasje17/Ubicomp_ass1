import tkinter as tk
class Mainscreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.mainscreen = self
        #self.mainscreen.pack()
        self.parent = parent
        self.controller=controller

        self.instruction_lbl = tk.Label(
            master= self,
            text = "Scan key fab",
            width = 75,
            height = 5
        )
        self.instruction_lbl.grid(row = 0, column = 0, columnspan = 5, sticky = "nesw")

        self.inputID_lbl = tk.Label(
            master = self,
            text = "partent id",
            width=10
        )
        self.inputID_lbl.grid(row = 1, column = 0,sticky = "nesw")

        self.keyfab_inp = tk.Entry(
            master= self,
            width=10
        )
        self.keyfab_inp.grid(row=1, column=1, sticky = "nesw")

        self.keyfab_btn = tk.Button(
            master=self,
            text="Key Fab",
            command =self.keyfab_login
        )
        self.keyfab_btn.grid(row=1, column=3, sticky = "nesw")

        self.no_keyfab_lbl= tk.Label(
            master=self,
            text= "if you have no key fab please pres apropriate button below",
            height = 5
        )
        self.no_keyfab_lbl.grid(row=2, column=0, columnspan = 5, sticky="nesw")
        
        self.login_btn = tk.Button(
            master= self,
            text= "Parent login",
            command = self.parent_login
        )
        self.login_btn.grid(row=3, column=1)

        self.not_parant_btn = tk.Button(
            master=self,
            text="Not Parent",
            command= self.not_parent_action
        )
        self.not_parant_btn.grid(row=3, column=3)

    def keyfab_login(self):
        foundparent = None
        for parent in self.controller.parents:
            if parent.key_fob == self.keyfab_inp.get():
                foundparent = parent
        
        if foundparent:
            self.keyfab_inp.select_clear()
            self.controller.frames["CildrenInOutScreen"].initiate_transistion(foundparent)
            self.controller.show_frame("CildrenInOutScreen")
        else:
            print("unkonw keyfob:" + self.keyfab_inp.get())
            self.keyfab_inp.select_clear()

    
        #login with the id written in self.keyfab_inp.get()

    def parent_login(self):
        self.controller.show_frame("Loginscreen")

    def not_parent_action(self):
        self.controller.show_frame("NonParentPickupScreen")