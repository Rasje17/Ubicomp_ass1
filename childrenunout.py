import tkinter as tk

class CildrenInOutScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller=controller

        self.info_lbl = tk.Label(
            self,
            text = "Select the children below and the clic the in or out button"
        )
        self.info_lbl.grid(row=0, column=0,columnspan=5, sticky="nsew")


        #setting up listbox frame with scrolling
        self.child_list_frame = tk.Frame(self)      

        self.scrollbar = tk.Scrollbar(self.child_list_frame, orient=tk.VERTICAL)
        
        self.child_listbox = tk.Listbox(
            self.child_list_frame, 
            yscrollcommand=self.scrollbar.set,
            selectmode = tk.MULTIPLE
            )
        
        self.populate_listbox()
        
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.child_listbox.pack()

        self.child_list_frame.grid(row=1, column=1, columnspan=3, sticky="nsew")

        #setting up buttons

        self.in_btn = tk.Button(
            self,
            text= "IN",
            command = self.check_in
        )
        self.in_btn.grid(row=2, column=0, sticky="nsew")

        self.out_btn = tk.Button(
            self,
            text="OUT",
            command= self.check_out
        )
        self.out_btn.grid(row=2, column=3, sticky="nsew")

        self.return_btn = tk.Button(
            self,
            text="Return to mainscreen",
            command= self.return_to_main
        )
        self.return_btn.grid(row=2, column=5, sticky="nsew")

    def populate_listbox(self):
        for i in range (100):
            self.child_listbox.insert(tk.END, "child nr" + str(i))

    def check_in(self):
        pass

    def check_out(self):
        pass

    def return_to_main(self):
        #clear user login
        self.controller.show_frame("Mainscreen")