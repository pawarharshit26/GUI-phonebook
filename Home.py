import tkinter
from tkinter import *
from tkinter import messagebox


def new():
   root.destroy()
   import add_new_entry_interface

def num():
    root.destroy()
    import find_contact_interface

def A():
   root.destroy()
   import all_contact_interface

root = tkinter.Tk()
root.title("PhoneBook")
root.geometry("720x480")
root['bg'] = 'white'


main_lable = Label(root,text = 'Contacts',font = ('aerial',36),bg = 'white' , fg = 'red')
main_lable.place(x = 250,y = 80)


all_contact = Button(root,text = 'All Contact',font = ('aerial',20),bg = 'white',fg = 'blue',command = A)
all_contact.place(x = 150,y = 180)

New_entry = Button(root,text = 'Add New Entries',font = ('aerial',20),bg = 'white',fg = 'blue',command = new)
New_entry.place(x = 330,y = 180)

fc = Button(root,text = 'Find contact',font = ('aerial',20),bg = 'white',fg = 'blue',command = num)
fc.place(x = 250,y = 250)

root.mainloop()
