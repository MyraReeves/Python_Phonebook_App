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

        # Set the background color of the window to a very light blue shade:
        self.master.configure(bg="#e7feff")

        # TO-DO: Create a prototcol to catch Window OS's built-in event button "WM_DELETE_WINDOW" so that when that is clicked the program will access the function.py file and use its "ask_quit" function (passing in "self") to ask for confirmation before closing the window. This will occur if the user clicks the "X" in the upper right corner of the window:

        # arg = self.master

        # Load the imported GUI widget from the GUI module file, passing in "self":



# When this main application module runs...
if __name__ == "__main__":
    # Create a window from Tkinter and assign it to a variable named "root":
    root = tk.Tk()

    # Use the above ParentWindow class app to pass that "root" variable into:
    App = ParentWindow(root)

    # And create a main loop for it to run so that the window stays persistently open until manually closed by the user:
    root.mainloop()