import tkinter
from tkinter import *
from tkinter import messagebox


def save():
    p = messagebox.askyesno(title = 'question',message = 'check name and number')
    if p == True:
        string = name.get() + "    " + mob_no.get()
        #print(string)

        add = open("storage.txt",'a')

        s = string
        add.write('\n')
        add.write(s)

        add.close()

        root.destroy()
        import Home

def back():
    root.destroy()
    import Home


root = tkinter.Tk()
root.title("Add new Entry")
root.geometry("702x480")
root['bg'] = 'white'

Add_entry = Label(root,text = "Add new Entry",font = ("aerial",30),bg = 'white',fg = "red")
Add_entry.place(x = 200,y = 80)


name_lable = Label(root,text = "Name",font = ("aerial",16),bg = 'white',fg = "red")
name_lable.place(x = 200,y = 190)

name = Entry(root,width = 26)
name.place(x=320,y=200)


mobile_no = Label(root,text = "Mobile No",font = ("aerial",16),bg = 'white',fg = "red")
mobile_no.place(x = 200,y = 250)

mob_no = Entry(root,width = 26)
mob_no.place(x=320,y=250)


submit= Button(root,text = 'submit',font = ("aerial",16),bg = 'white',fg = "blue",command = save)
submit.place(x=230,y = 300)

home= Button(root,text = 'Home',font = ("aerial",16),bg = 'white',fg = "blue",command = back)
home.place(x=350,y = 300)

root.mainloop()
