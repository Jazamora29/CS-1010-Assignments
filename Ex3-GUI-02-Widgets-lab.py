#Jose Andres Zamora
import tkinter
from tkinter import *

main = tkinter.Tk()
main.geometry("300x300")

main.configure(bg = '#732828')

choices = Listbox(selectmode = 'SINGLE')
choices.insert(1, "Red")
choices.insert(2, "Orange")
choices.insert(3, "Yellow")
choices.insert(4, "Green")
choices.insert(5, "Blue")
choices.insert(6, "Purple")
choices.pack()

def buttonPress():
    if choices.curselection()[0] == 0:
        main.configure(bg = 'red')
        words.configure(text = "Red")
    elif choices.curselection()[0] == 1:
        main.configure(bg = 'orange')
        words.configure(text = "Orange")
    elif choices.curselection()[0] == 2:
        main.configure(bg = 'yellow')
        words.configure(text = "Yellow")
    elif choices.curselection()[0] == 3:
        main.configure(bg = 'green')
        words.configure(text = "Green")
    elif choices.curselection()[0] == 4:
        main.configure(bg = 'blue')
        words.configure(text = "Blue")
    else:
        main.configure(bg = 'purple')
        words.configure(text = "Purple")

bub = tkinter.Button(text = "Set Color", command = buttonPress)
bub.pack()

var = StringVar()
words = Label(main, text = var)
words.pack()

main.mainloop()