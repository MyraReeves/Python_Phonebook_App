# Import the Tkinter module:
import tkinter as tk

# Import ALL of its widgets:
from tkinter import *

# Import Tkinter's messagebox:
from tkinter import messagebox

# Import the other 2 module scripts created for this phonebook app:
import main

# Create a function to define the widgets (labels, buttons, text boxes, scrollbars, etc.) inside the window on the screen.  Pass in itself to access the class objects:
def load_gui(self):

    # **************** LABELS *****************************
    # Create a "First Name" label object by instantiating/calling Tkinter's "Label" class, naming it, placing it on the primary window form (the master level of the class), and defining what the value of its text attribute should be: 
    self.label_firstName = tk.Label(self.master, text = 'First Name: ')

    # Place it onto the form window using the grid geometry manager. Give it a padding of 27px to the left and 10px on top, and make sure it goes into the upper(north) leftmost (west) of the window:
    self.label_firstName.grid(row=0, column=0, padx=(27,0), pady=(10,0), sticky=N+W)

    # Repeat the same again to create label objects of "Last Name", "Phone Number", "Email", and "Users".  Remember to skip rows to allow for the text boxes to fit between these labels:
    self.label_lastName = tk.Label(self.master, text = 'Last Name: ')
    self.label_lastName.grid(row=2, column=0, padx=(27,0), pady=(10,0), sticky=N+W)

    self.label_phone = tk.Label(self.master, text = 'Phone Number: ')
    self.label_phone.grid(row=4, column=0, padx=(27,0), pady=(10,0), sticky=N+W)

    self.label_email = tk.Label(self.master, text = 'Email Address: ')
    self.label_email.grid(row=6, column=0, padx=(27,0), pady=(10,0), sticky=N+W)

    self.label_users = tk.Label(self.master, text = 'Users: ')
    # The "Users" area will be in the first row, to the right of the first name area:
    self.label_user.grid(row=0, column=2, padx=(0,0), pady=(10,0), sticky=N+W)


    # **************** TEXT BOXES *****************************




# If an attempt is made to accidentally run this GUI file as its own stand-alone module, make certain nothing occurs: 
if __name__ == "__main__":
    pass
