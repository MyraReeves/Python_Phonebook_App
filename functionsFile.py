# Import the operating system module to enable use of os-dependent functionality:
import os

# Import the Tkinter module:
import tkinter as tk

# Import ALL of its widgets:
from tkinter import *

# Import Tkinter's messagebox:
from tkinter import messagebox

# Import SQLite in order to create a database:
import sqlite3

# Import the other 2 module scripts created for this phonebook app:
import main
import GUI



# **************** CENTER WINDOW ********************
# Create a function to center the form window in the middle of the screen. To do so, width and height are necessary parameters; they will be set to 500 and 300, respectively, in the main file:
def center_window(self, w, h):

    # Use the built-in Tkinter methods "winfo_screenwidth()" & "winfo_screenheight()" to get the user's screen width and height.  Assign them to variables:
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()

    # Calculate x and y coordinates to center the form window app on the user's screen. Again, in the main file, w will be defined as 500 and h will be defined as 300.
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))

    # Use the built-in Tkinter method "geometry()" to set the width & height dimensions of the form (width * height) and the x & y coordinates of where to place it on the screen so that it will be centered.  
    centerGeometry = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeometry




# **************** CONFIRM QUIT ********************
# Create a function to confirm a user wants to close the app if that user clicks on the windows upper-right 'X':
def ask_quit(self):
    # Use Messagebox class's built-in "askokcancel()" method to create a pop-up with two button choices -- "OK" or "Cancel". The first parameter of this method will be the name of the pop-up window; the second parameter is the message inside the pop-up box.
    if messagebox.askokcancel("Quit", "Exit application?"):

        # If the user clicks on OK, then close the app:
        self.master.destroy()

        # ...and using the operating system's built-in "exit()" method fully delete any parts of memory that had been used by this app: 
        os._exit(0)



# **************** CREATE DATABASE ********************
# Create a function that builds a database
def create_db(self):

    # Create a connection to a new database called "phonebook" by using SQLite's built-in connect() method
    connection = sqlite3.connect('phonebook.db')

    # If creating that connection was successful/error-free...
    with connection:

        # ...use the cursor of our connection class object...
        cur = connection.cursor()

        # ...to create a table and its column names with their data types:
        cur.execute("CREATE TABLE if not exists table_phonebook ( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            column_firstName TEXT, \
            column_lastName TEXT, \
            column_fullName TEXT, \
            column_phone TEXT, \
            column_email TEXT \
            );")
        
        # Use the commit() method to save the above changes:
        connection.commit()

    # Close the database:
    connection.close()

    # Since the database is currently empty, pass this "create_db" function into the "first_run" function below:
    first_run(self)


