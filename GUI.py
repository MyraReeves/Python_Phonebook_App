# Import the Tkinter module:
import tkinter as tk

# Import ALL of its widgets:
from tkinter import *

# Import Tkinter's messagebox:
from tkinter import messagebox

# Import the other 2 module scripts created for this phonebook app:
import main
import functionsFile



# Create a function to define the widgets (labels, buttons, text boxes, scrollbars, etc.) inside the window on the screen.  Pass in itself to access the class objects:
def load_gui(self):

    # **************** LABELS *****************************
    # Create a "First Name" label object by instantiating/calling Tkinter's "Label" class, naming it, placing it on the primary window form (the master level of the class), and defining what the value of its text attribute should be: 
    self.label_firstName = tk.Label(self.master, text = 'First Name: ', bg="#e7feff")

    # Place it onto the form window using the grid geometry manager. Give it a padding of 27px to the left and 10px on top, and make sure it goes into the upper(north) leftmost (west) of the cell:
    self.label_firstName.grid(row=0, column=0, padx=(27,0), pady=(10,0), sticky=N+W)

    # Repeat the same again to create label objects of "Last Name", "Phone Number", "Email", and "Users".  Remember to skip rows to allow for the text boxes to fit between these labels:
    self.label_lastName = tk.Label(self.master, text = 'Last Name: ', bg="#e7feff")
    self.label_lastName.grid(row=2, column=0, padx=(27,0), pady=(10,0), sticky=N+W)

    self.label_phone = tk.Label(self.master, text = 'Phone Number: ', bg="#e7feff")
    self.label_phone.grid(row=4, column=0, padx=(27,0), pady=(10,0), sticky=N+W)

    self.label_email = tk.Label(self.master, text = 'Email Address: ', bg="#e7feff")
    self.label_email.grid(row=6, column=0, padx=(27,0), pady=(10,0), sticky=N+W)

    self.label_users = tk.Label(self.master, text = 'Choose An Existing Entry Here: ', bg="#e7feff")
    # The "Users" area will be in the first row, to the right of the first name area:
    self.label_users.grid(row=0, column=2, padx=(0,0), pady=(10,0), sticky=N+W)


    # **************** EMPTY TEXT BOXES *****************************
    self.text_firstName = tk.Entry(self.master, text='')
    # These empty text boxes should span the width of 2 columns to allow for long entries:
    self.text_firstName.grid(row=1, column=0, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)

    self.text_lastName = tk.Entry(self.master, text='')
    self.text_lastName.grid(row=3, column=0, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)

    self.text_phone = tk.Entry(self.master, text='')
    self.text_phone.grid(row=5, column=0, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)

    self.text_email = tk.Entry(self.master, text='')
    self.text_email.grid(row=7, column=0, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)


    # **************** USERS LIST BOX & SCROLLBAR *****************************
    self.scrollbar = Scrollbar(self.master, orient=VERTICAL)
    self.scrollbar.grid(row=1, rowspan=7, column=5, padx=(0,0), pady=(0,0), sticky=N+E+S)

    self.listBox = Listbox(self.master, exportselection=0, yscrollcommand=self.scrollbar.set)
    self.listBox.grid(row=1, rowspan=7, column=2, columnspan=3, padx=(0,0), pady=(0,0), sticky=N+E+W+S)

    # Create event listener for if a user chooses a name from the list. If they do, then call the "onSelect" function from functionFile
    self.listBox.bind('<<ListboxSelect>>', lambda event: functionsFile.onSelect(self, event))
    self.scrollbar.config(command=self.listBox.yview)


    # **************** BUTTONS *****************************
    self.button_add = tk.Button(self.master, width=12, height=2, text='Add', fg="darkgreen", bg="lightgreen", command=lambda: functionsFile.addToList(self))
    self.button_add.grid(row=8, column=0, padx=(25,0), pady=(45,10), sticky=W)

    self.button_update = tk.Button(self.master, width=12, height=2, text='Update', fg="darkblue", bg="lightblue", command=lambda: functionsFile.onUpdate(self))
    self.button_update.grid(row=8, column=1, padx=(15,0), pady=(45,10), sticky=W)

    self.button_delete = tk.Button(self.master, width=12, height=2, text='Delete', fg="darkred", bg="pink", command=lambda: functionsFile.onDelete(self))
    self.button_delete.grid(row=8, column=2, padx=(15,0), pady=(45,10), sticky=W)

    self.button_close = tk.Button(self.master, width=8, height=1, text='EXIT', font=("Courier", 11), fg="darkred", bg="papayawhip", command=lambda: functionsFile.ask_quit(self))
    self.button_close.grid(row=8, column=4, padx=(15,0), pady=(45,10), sticky=E)




    # Create the database:
    functionsFile.create_db(self)

    # Populate the listbox of names in the database:
    functionsFile.onRefresh(self)



# **************** If an attempt is made to accidentally run this GUI file as its own stand-alone module, make certain nothing occurs: 
if __name__ == "__main__":
    pass
