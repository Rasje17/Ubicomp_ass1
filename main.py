import tkinter as tk

class GUI:
    def __init__(self, parent):
        self.mainscreen = tk.Frame(parent)
        self.mainscreen.pack()
        self.parent = parent

        self.instruction_lbl = tk.Label(
            master= self.mainscreen,
            text = "Scan key fab",
            width = 75,
            height = 5
        )
        self.instruction_lbl.grid(row = 0, column = 0, columnspan = 5, sticky = "nesw")

        self.inputID_lbl = tk.Label(
            master = self.mainscreen,
            text = "partent id",
            width=10
        )
        self.inputID_lbl.grid(row = 1, column = 0,sticky = "nesw")

        self.keyfab_inp = tk.Entry(
            master= self.mainscreen,
            width=10
        )
        self.keyfab_inp.grid(row=1, column=1, sticky = "nesw")

        self.keyfab_btn = tk.Button(
            master=self.mainscreen,
            text="Key Fab",
            command =self.keyfab_login
        )
        self.keyfab_btn.grid(row=1, column=3, sticky = "nesw")

        self.no_keyfab_lbl= tk.Label(
            master=self.mainscreen,
            text= "if you have no key fab please pres apropriate button below",
            height = 5
        )
        self.no_keyfab_lbl.grid(row=2, column=0, columnspan = 5, sticky="nesw")
        
        self.login_btn = tk.Button(
            master= self.mainscreen,
            text= "Parent login",
            command = self.parent_login
        )
        self.login_btn.grid(row=3, column=1)

        self.not_parant_btn = tk.Button(
            master=self.mainscreen,
            text="Not Parent",
            command= self.not_parent_action
        )
        self.not_parant_btn.grid(row=3, column=3)

    def keyfab_login(self):
        print(self.keyfab_inp.get())
        #login with the id written in self.keyfab_inp.get()

    def parent_login(self):
        pass

    def not_parent_action(self):
        pass


if __name__ == "__main__":
    # Mockup of entities in system (childs,parents,emploiess daycare)
    # Create a new window
    root = tk.Tk()
    root.title("In/Out system")
    app =GUI(root)
    root.mainloop()