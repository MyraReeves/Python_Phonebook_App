# Import the operating system module to enable use of os-dependent functionality:
import os

# Import the Tkinter module:
import tkinter as tk

# Import ALL of its widgets:
from tkinter import *

# Import Tkinter's messagebox:
from tkinter import messagebox


import sqlite3

# Import the other 2 module scripts created for this phonebook app:
import main
import GUI



# **************** CENTER WINDOW ********************
# Create a function to center the form window in the middle of the screen. To do so, width and height are needed:
def center_window(self, w, h):

    # Get the user's screen width and height, and assign them to variables:
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()

    # Calculate x and y coordinates to center the form window app on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeometry = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeometry




# **************** CONFIRM QUIT ********************
# Create a function to confirm a user wants to close the app if that user clicks on the windows upper-right 'X':
def ask_quit(self):
    if messagebox.askokcancel("Quit", "Exit application?"):

        # Close the app:
        self.master.destroy()
        os._exit(0)


