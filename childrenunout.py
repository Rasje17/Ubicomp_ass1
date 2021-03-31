import tkinter as tk
from cild_parent import Parent
from child import Child

class CildrenInOutScreen(tk.Frame):
    def __init__(self, parent, controller):
        #setting up gui:
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
        
        #self.populate_listbox()
        
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

        #logic things
        self.pickup_person = None
        self.parentpikup = False
        self.child_list = []

    def initiate_transistion(self, parent):
        self.pickup_person = parent
        if(isinstance(self.pickup_person, Parent)):
            self.parentpikup = True
        else:
            self.parentpikup = False
        self.populate_listbox()

    def populate_listbox(self):
        #populate own childlist
        print(self.parentpikup)
        if(self.parentpikup):
            for i in self.pickup_person.children:
                for j in self.controller.daycare.children:
                    if (i == j.child_id):
                        self.child_list.append(j)
        else:
            for child in self.controller.daycare.children:
                self.child_list.append(child)


        for i in self.child_list:
            self.child_listbox.insert(tk.END, i.name)

    def check_in(self):
        for child in self.getselectedchildren():
            self.controller.daycare.check_in(child)
            print("present children:")
            print(str(self.controller.daycare.present_children))
            self.return_to_main()
        

    def check_out(self):
        for child in self.getselectedchildren():
            self.controller.daycare.check_out(child)
            print("present children:")
            print(str(self.controller.daycare.present_children))
            self.return_to_main()

    def return_to_main(self):
        self.pickup_person = None
        self.parentpikup = False
        self.child_list = []
        self.child_listbox.delete(0,tk.END)
        self.controller.show_frame("Mainscreen")

    def getselectedchildren(self):
        retlist=[]
        for i in self.child_listbox.curselection():
            retlist.append(self.child_list[i])
        return retlist 