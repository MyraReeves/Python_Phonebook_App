# Import the Tkinter module:
import tkinter as tk

# Import ALL of its widgets:
from tkinter import *

# Import Tkinter's messagebox:
from tkinter import messagebox

# TO-DO:  Import the other modules created for this phonebook app:


# Create a class that creates a form window on the screen and have it inherit from the built-in Tkinter Frame class object:
class ParentWindow(Frame):

    # Initialize it:
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Access the "master" object from the parent by specifying self:
        self.master = master

        # Make the window a set size that can't be resized by the user by setting the minimum and maximum window size to be the same dimensisions. 500px high and 300px wide:
        self.master.minsize(500, 300)
        self.master.maxsize(500, 300)
        # This could have also been done by using:     self.master.resizable(width=False, height=False)

        # TO-DO: Access the function.py file and use its "center window" function.  Pass in "self" and the height/width dimensions of the window:

        # Set a title for this form window that is being created on the screen:
        self.master.title("Demo Tkinter Phonebook")

        # Load the imported GUI widgets from the GUI module: