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
# Create a function to build a database:
def create_db(self):

    # Create a connection to a new database called "phonebook" by using SQLite's built-in connect() method:
    connection = sqlite3.connect('phonebook.db')

    # If creating that connection was successful/error-free...
    with connection:

        # ...then use the cursor of our connection class object...
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



# **************** INSERT EXAMPLE TEXT INTO DATABASE TABLE ********************
# Create a function that
def first_run(self):

    # Connect to the "phonebook" database by using SQLite's built-in "connect()" method:
    connection = sqlite3.connect('phonebook.db')

    # If creating that connection was successful...
    with connection:
        # ...then access the cursor object and assign it to the "cur" variable...
        cur = connection.cursor()
        # ...and use that variable to execute the "count_records" function: 
        cur, count = count_records(cur)

        # If there isn't any data in the database (ie. zero rows in this only table)...
        if count < 1:
            # ...then create a 4 indices long tuple of first row example data into the table, to prevent errors:
            cur.execute("""INSERT INTO table_phonebook (column_firstName, column_lastName, column_fullName, column_phone, column_email) VALUES (?,?,?,?,?)""", ('ExampleFirstName','LastName','ExampleFirstName LastName','555-555-5555','john_doe@example.com'))
            # ...and save these changes to the database:
            connection.commit()
    # Close the database:
    connection.close()


# **************** COUNT NUMBER OF ROWS CURRENTLY IN THE DATABASE TABLE ********************
def count_records(cur):
    # Create an empty count variable:
    count = ""

    # Use SQLite's built-in "execute()" to count all the rows in the table:
    cur.execute("""SELECT COUNT(*) FROM table_phonebook""")

    # Extract the very first indexed value from that (ie. the value of the ID integer primary key) and set it as the value of the "count" variable:
    count = cur.fetchone()[0]

    # Return the cursor and the number of rows:
    return cur, count
  


# **************** LOOK-UP INFORMATION ********************
# Create a function to handle if a user selects a name inside the list box:
def onSelect(self,event):
    # The event is the self.listBox widget found in the GUI file

    # Save inside of a "varList" variable whatever is triggering the event (that being a user clicking on the listBox widget)
    varList = event.widget

    # Each name/row inside of the list box has its own index.  Find the index of which one the user selected, and save it in a variable named "select":
    select = varList.curselection()[0]

    # Find the text inside of that index (i.e. the text inside of "select") of the "varList" variable.  Save that text inside a variable named "value":
    value = varList.get(select)

    # Connect to the "phonebook" database by using SQLite's built-in "connect()" method:
    connection = sqlite3.connect('phonebook.db')

    # If creating that connection was successful...
    with connection:
        # ...then access the cursor object and assign it to a "cursor" variable...
        cursor = connection.cursor()
        # ...and use that "cursor" variable to select the firstName, lastName, phone, and email columns from the phonebook table where the full name is the text in the "value" variable: 
        cursor.execute("""SELECT column_firstName, column_lastName, column_phone, column_email FROM table_phonebook WHERE column_fullName = (?)""", [value])

        # The above returns a tuple.  So we need to slice it into 4 parts using data[]. The text box fields on the left hand side of the form window also need to be cleared first and then each iteration can be inserted into the corresponding text box so that the user can see the info they resquested:
        varBody = cursor.fetchall()
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])


