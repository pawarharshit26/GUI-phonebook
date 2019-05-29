import tkinter
from tkinter import *
from tkinter import messagebox


def find():

    f = open("storage.txt",'r') 

    d = {}

    for line in f:              
        l= line.split()
        x = l[0]
        y = l[1]
        d[x] = y


    fi = name.get()             

    if fi in d:               
        string = fi  + '  =  '  + d[fi]
    else:
        string = "contact not found"

    f.close()
    
    contact = Label(root,text = string,font = ("aerial",16),bg = 'white',fg = "dark blue")
    contact.place(x = 200,y = 250)
    
def back():
    root.destroy()
    import Home


root = tkinter.Tk()
root.title("Find contact")
root.geometry("702x480")
root['bg'] = 'white'

fc = Label(root,text = "Find contact",font = ("aerial",30),bg = 'white',fg = "red")
fc.place(x = 200,y = 80)

name_lable = Label(root,text = "Name",font = ("aerial",16),bg = 'white',fg = "red")
name_lable.place(x = 200,y = 190)

name = Entry(root,width = 26)
name.place(x=320,y=200)

submit= Button(root,text = 'submit',font = ("aerial",16),bg = 'white',fg = "blue",command = find)
submit.place(x=230,y = 300)

Home= Button(root,text = 'Home',font = ("aerial",16),bg = 'white',fg = "blue",command = back)
Home.place(x=350,y = 300)

root.mainloop()
