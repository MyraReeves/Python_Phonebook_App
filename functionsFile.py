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

    # Since the database is currently empty, pass this "create_db" function into the "first_run" function (see Lines 93 to 112):
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
        # ...and use that variable to execute the "count_records" function (see Lines 116 to 127): 
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




# **************** ADD NEW INFORMATION INPUTTED BY USER ********************
# Create a function to add new inputted information from the user into the stored list when the "Add" button is pressed:
def addToList(self):
    var_fname = self.text_firstName.get()
    var_lname = self.text_lastName.get()

    # Correct for user error Part 1 -- Remove any potential blank spaces before and/or after the user's entries:
    var_fname = var_fname.strip()
    var_lname = var_lname.strip()
    # Alternatively, those two separate steps could be combined into only one step:
    var_phone = self.text_phone.get().strip()
    var_email = self.text_email.get().strip()
    
    # Correct for user error Part 2 -- Ensure that the first character in each word of the entered name is capitalized:
    var_fname = var_fname.title()
    var_lname = var_lname.title()

    # Correct for user error Part 3 -- Ensure that proper email address format was used:
    if not "@" or not "." in var_email:
        print("ERROR: Incorrect email format entered!")

    # Create a "var_fullname" variable to hold the combination of the entered first and last names: 
    var_fullname = ("{} {}".format(var_fname, var_lname))
    # Allow devs to confirm via the console that the names combined successfully:
    print("var_fullname: {}".format(var_fullname))

    # Correct for user error Part 4 -- Ensure the user didn't leave any fields blank:
    # If the length (ie. number of characters) of EVERY variable is at least 1 character long....
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and(len(var_email) > 0):
        # ...connect to the database:
        connection = sqlite3.connect('phonebook.db')
        # If the connection is good...
        with connection:
            # ...then access the cursor object...
            cursor = connection.cursor()
            # ...and check the database for the existance of the inputted fullname:
            cursor.execute("""SELECT COUNT(column_fullName) FROM table_phonebook WHERE column_fullName = '{}'""".format(var_fullname))
            count = cursor.fetchone()[0]
            checkName = count

            # If the full name does NOT already exist in the database (ie. the count is zero), then proceed with adding the information:
            if checkName == 0:
                # Check for errors. Allow devs to see in the console that this function is working correctly:
                print("checkName: {}".format(checkName))
                # Insert the entered information into the database's table:
                cursor.execute("""INSERT INTO table_phonebook (column_firstName, column_lastName, column_fullName, column_phone, column_email) VALUES (?,?,?,?,?)""",(var_fname, var_lname, var_fullname, var_phone, var_email))
                # Update the listBox widget by inserting the newly inputted full name:
                self.listBox.insert(END, var_fullname)
                # ...and use the onClear() function [see Lines 304 to 308] to clear all of the text boxes to prepare for future user actions:
                onClear(self)


            #  If the full name already exists in the database, then disregard the add request, alert the user, and clear the text:
            else:
                messagebox.showerror("ERROR: Duplicate Name!","'{}' already exists in the database! Please alter the new name if you are adding a new person's information.".format(var_fullname))
                onClear(self)

        # Save the above changes to the database:
        connection.commit()

        # Close the database:
        connection.close()


    else:
        messagebox.showerror("ERROR: Missing input", "Please ensure that there is data in ALL four fields.")
        



# **************** ALLOW USER TO DELETE ENTRIES ********************
# Create a function to delete an entry from the list, upon request from the user via the GUI button:
def onDelete(self):
    # Use the built-in "get" function to access the "curselection" function which will in turn find the index of which full name the user clicked on inside the list box:
    var_select = self.listBox.get(self.listBox.curselection())

    # Connect to the database:
    connection = sqlite3.connect('phonebook.db')

    # If that connection was successful...
    with connection:
        # ...then access the cursor object...
        cur = connection.cursor()
        # ...and count how many rows are in the table, because if the database becomes empty that will create errors:
        cur.execute("""SELECT COUNT(*) FROM table_phonebook""")
        count = cur.fetchone()[0]

        # If there are at least two records left in the database...
        if count > 1:
            # Then use the built-in ask pop-up (which contains choice between OK button or Cancel button) function to receive confirmation that the user wishes to delete the record they selected:
            confirm = messagebox.askokcancel("*** DELETE CONFIRMATION ***", "All information associated with, ({}) \nwill be permanently deleted from the database. \n\nProceed with this deletion?".format(var_select))

            # If the user confirms they want to delete that record:
            if confirm:
                # Connect to the database, and with the connection access the cursor object:
                connection = sqlite3.connectionect('phonebook.db')
                with connection:
                    cursor = connection.cursor()
                    # ...then use the SQL command to delete the requested record from the table:
                    cursor.execute("""DELETE FROM table_phonebook WHERE column_fullName = '{}'""".format(var_select))
                # Once the requested rows have been deleted from the table, call the "clearOnDeleted" function [See lines 290 to 300] to clear all the textboxes from the screen and to remove the name from the list box:
                clearOnDeleted(self)

                # Save these changes to the database:
                connection.commit()

        # However, if there is only 1 record left in the database, then let the user know that it isn't currently possible to delete:
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first to enable deletion of ({}).".format(var_select,var_select))

    # Close the database:
    connection.close()




# **************** CLEAR TEXT FROM SCREEN (two different functions needed) ********************

# Create a function for after record deletion to clear the text from the screen's text boxes AND delete the name from the list box: 
def clearOnDeleted(self):
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)

    try:
        index = self.listBox.curselection()[0]
        self.listBox.delete(index)
    except IndexError:
        pass


# Create a function (for use in other scenarios) that clears the text from only the screen's text boxes:
def onClear(self):
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    



# **************** REFRESH THE LIST BOX ********************
# Create a function to re-populate the listbox with names from the database
def onRefresh(self):
    # Delete the current contents of the list box:
    self.listBox.delete(0,END)

    # Connect to the database and access the cursor object
    connection = sqlite3.connect('phonebook.db')
    with connection:
        cursor = connection.cursor()

        # Count how many records are in the table.  As long as it is more than zero...
        cursor.execute("""SELECT COUNT(*) FROM table_phonebook""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
                # ...loop thru the table, selecting the contents of the "full name" cell from each row and inserting that text into the list box: 
                cursor.execute("""SELECT column_fullName FROM table_phonebook""")
                varList = cursor.fetchall()[i]
                for item in varList:
                    self.listBox.insert(0,str(item))
                    i = i + 1
 
    # Close the database:
    connection.close()




# **************** ALLOW ENTRIES TO BE EDITTED ********************
# Create a function that will allow a user to change an email address or phone number
def onUpdate(self):
    try:
        # Find the index of the full name the user selected within the list box:
        var_select = self.listBox.curselection()[0]
        # Get the text contained in that index.  Assign that full name to a "var_value" variable:
        var_value = self.listBox.get(var_select)

    except:
        messagebox.showinfo("Missing selection","No name was selected from the list box. \nCancelling the Update request.")
        return

    # Pull the new text the user wrote inside the phone and email text boxes.  Assign them to variables.  While doing so, also correct for potential user error by removing any leading or trailing white space: 
    var_phone = self.text_phone.get().strip()
    var_email = self.text_email.get().strip()

    # If the phone AND email text fields have characters in them (ie. a length greater than zero)...
    if (len(var_phone) > 0) and (len(var_email) > 0):
        # ...then connect to the database and access the cursor object...
        connection = sqlite3.connect('phonebook.db')
        with connection:
            cur = connection.cursor()

            # ...then count how many records of the newly inputted phone number or email already exist in the table, because if a record of it already exists, then there is no change and therefore no need to update the database.
            cur.execute("""SELECT COUNT(column_phone) FROM table_phonebook WHERE column_phone = '{}'""".format(var_phone))
            count_phone = cur.fetchone()[0]
            cur.execute("""SELECT COUNT(column_email) FROM table_phonebook WHERE column_email = '{}'""".format(var_email))
            count_email = cur.fetchone()[0]
            
            # If there is no count (zero record) of the proposed new phone number or email already in the database...
            if count_phone == 0 or count_email == 0:
                # ...then use a built-in ok/cancel pop-up to have the user confirm the proposed changes: 
                response = messagebox.askokcancel("CONFIRM UPDATE","The following changes ({}) and ({}) will be implemented for ({}). \n\nProceed?".format(var_phone, var_email, var_value))

                # If the user confirms their wish to update the text values inside those fields...
                if response:
                    # ...then connect to the database and access the cursor object...
                    connection = sqlite3.connectionect('phonebook.db')
                    with connection:
                        cursor = connection.cursor()
                        # ...and use the "update" SQL command to change the information inside of the phone and/or email cells of the selected row:
                        cursor.execute("""UPDATE table_phonebook SET phone = '{}', column_email = '{}' WHERE column_fullName = '{}'""".format(var_phone, var_email, var_value))

                        # Afterwards, clear all the text boxes on the screen:
                        onClear(self)

                        # And save the changes to the database:
                        connection.commit()

                # But if the user pressed the "cancel" button, then let them know that nothing was changed:
                else:
                    messagebox.showinfo("CANCEL CONFIRMED","No changes have been made to ({}).".format(var_value))


            # If there is already a record of the newly inputted phone number or email already existing in the table (ie. the count of them is 1 or greater), then there is no need to update the database. Inform the user that there is no change:
            else:
                messagebox.showinfo("NO CHANGE DETECTED","Both ({}) and ({}) \nalready exist in the database for this person's name. \n\nUpdate is not needed. Cancelling request.".format(var_phone, var_email))
            # Clear the text boxes:
            onClear(self)

        # Close the connection to the database:
        connection.close()


    # If the phone AND email text fields don't both have characters in them (ie. they don't both have a length greater than zero), then inform the user that they need to try their request again:
    else:
        messagebox.showerror("MISSING INFORMATION","Please select a name from the list. \nThen edit the phone or email information. \nNames can not be changed. \nTo change a name, please delete the existing record and start over.")
    # Clear the text boxes:
    onClear(self)






# **************** If an attempt is made to accidentally run this GUI file as its own stand-alone module, make certain nothing occurs: 
if __name__ == "__main__":
    pass

