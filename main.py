import tkinter as tk

class GUI:
    def __init__(self, parent):
        container = tk.Frame(parent)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Mainscreen, Loginscreen):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Mainscreen")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

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
        print(self.keyfab_inp.get())
        #login with the id written in self.keyfab_inp.get()

    def parent_login(self):
        self.controller.show_frame("Loginscreen")

    def not_parent_action(self):
        pass

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


if __name__ == "__main__":
    # Mockup of entities in system (childs,parents,emploiess daycare)
    # Create a new window
    root = tk.Tk()
    root.title("In/Out system")
    app =GUI(root)
    root.mainloop()