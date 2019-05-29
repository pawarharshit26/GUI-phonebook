import tkinter
from tkinter import *
from tkinter import messagebox

def home():
    root.destroy()
    import Home


root = tkinter.Tk()
root.title("ALl Contact")
root.geometry("1080x720")
root['bg'] = 'white'


All = Label(root,text = "All Contact",font = ("aerial",36),bg = "white",fg = "red")
All.place(x = 440,y = 50)

h = Button(root,text = 'Home',font = ('aerial',16),bg = 'white',fg = 'blue',command = home)
h.place(x = 100,y = 70)


s = open("storage.txt","r")
d = {}
for line in s:
    l = line.split()
    x,y = l[0],l[1]
    d[x] = y

q = sorted(d)
j = 0
for i in q:
    string = i + "  =  " + d[i]
    contact = Label(root,text = string,font = ("aerial",12),bg = 'white',fg = "dark blue")
    contact.place(x = 100,y = 140 + 20*j)
    j +=1


s.close()

root.mainloop()
