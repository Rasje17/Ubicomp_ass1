import tkinter as tk
from nonparentpickup import NonParentPickupScreen
from loginscreen import Loginscreen
from mainscreen import Mainscreen
from childrenunout import CildrenInOutScreen
class GUI:
    def __init__(self, parent):
        container = tk.Frame(parent)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Mainscreen, Loginscreen, NonParentPickupScreen, CildrenInOutScreen):
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




if __name__ == "__main__":
    # Mockup of entities in system (childs,parents,emploiess daycare)
    # Create a new window
    root = tk.Tk()
    root.title("In/Out system")
    app =GUI(root)
    root.mainloop()