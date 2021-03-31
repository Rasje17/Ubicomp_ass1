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
        self.info_lbl.grid(row=0, column=0, sticky="nsew")

        self.child_list_frame = tk.Frame(self)
        

        self.scrollbar = tk.Scrollbar(self.child_list_frame, orient=tk.VERTICAL)
        
        self.child_listbox = tk.Listbox(self.child_list_frame, yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.child_listbox.pack()


        self.child_list_frame.grid(row=1, column=1, columnspan=3, sticky="nsew")