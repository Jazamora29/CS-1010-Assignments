#Jose Andres Zamora
import tkinter
from tkinter import *

main = tkinter.Tk()#declare window and the size of it
main.geometry("300x300")

main.configure(bg='#732828')#set background color to something I like

words = StringVar()#make a string var, then make a label with that string var, set string var, and lastly pack the label
out = Label(textvariable = words)
words.set("Hello, type words and push button")
out.pack()

user = Entry(bd = 5)#set up an entry with a small border then pack it
user.pack()

def buttonPress():#method for button
    var = user.get()#retreives info from entry
    if(var.lower() == "red"):#if red is inputed, not case sensitive, then change background to red
        main.configure(bg = 'red')
    elif(var.lower() == "blue"):#same as above but for blue
        main.configure(bg = 'blue')
    elif(var == ""):#if nothing we use code above to reset to default
        main.configure(bg='#732828')
        out.configure(textvariable = "Hello, type words and push button")
        out.pack()
    else:#lastly, if none of the above conditions are met we just change the label
        words.set(var)
        out.pack()

bub = Button(text = "Enter", command = buttonPress)#sets up button with method and text
bub.pack()#pack button

main.mainloop()