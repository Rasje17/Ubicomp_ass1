import tkinter as tk

class NonParentPickupScreen(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller=controller