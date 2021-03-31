import tkinter as tk
from nonparentpickup import NonParentPickupScreen
from loginscreen import Loginscreen
from mainscreen import Mainscreen
from childrenunout import CildrenInOutScreen
from child import Child
from cild_parent import Parent
from employee import Employee
from daycare import Daycare

class GUI:
    def __init__(self, parent):
        container = tk.Frame(parent)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #init of dummy object in system
        self.children= []
        
        
        self.parents = []
        
        self.employees = []

        self.populate()


        self.daycare = Daycare(self.children,[], self.employees, self.parents)
        

        self.frames = {}
        for F in (Mainscreen, Loginscreen, NonParentPickupScreen, CildrenInOutScreen):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nesw")

        self.show_frame("Mainscreen")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def populate(self):
        #children
        child1 = Child("Hans Jensen", "c1", ["p1", "p2"], [])
        child2 = Child("Line Jensen", "c2", ["p1", "p2"], [])
        child3 = Child("William den 3", "c3", ["p3"], [])

        self.children.extend([child1, child2, child3])

        #parents
        parent1 = Parent("Carl Jensen", "p1", ["c1", "c2"], "001")
        parent2 = Parent("Signe Jensen", "p2", ["c1", "c2"], "002")
        parent3 = Parent("Elisbeth den 1", "p3", ["c3"], "003")

        self.parents.extend([parent1, parent2, parent3])

        emply1 = Employee("Henrik Hansen", "e1", "101")
        self.employees.append(emply1)




if __name__ == "__main__":
    # Mockup of entities in system (childs,parents,emploiess daycare)
    # Create a new window
    root = tk.Tk()
    root.title("In/Out system")
    app =GUI(root)
    root.mainloop()