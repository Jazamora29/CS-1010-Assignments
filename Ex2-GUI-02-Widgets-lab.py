#Jose Andres Zamora
import tkinter
from tkinter import *

main = tkinter.Tk()#declare window and set the size
main.geometry("300x300")

main.configure(bg = '#732828')#make background a color I like

var = StringVar()#create a string var to store the output of the radio boxes
r1 = Radiobutton(main, text = "cat", variable = var, value = "cat")#make a radio box for cat, dog, and so on. Also packs each one

r1.pack()

r2 = Radiobutton(main, text = "dog", variable = var, value = "dog")

r2.pack()

r3 = Radiobutton(main, text = "cow", variable = var, value = "cow")

r3.pack()

r4 = Radiobutton(main, text = "bird", variable = var, value = "bird")

r4.pack()

ra = Label(main)#creates a label below them to print, also packs this
ra.pack()

var1 = IntVar()#creates a variable for each check box
var2 = IntVar()
var3 = IntVar()
c1 = Checkbutton(main, text = "1", variable = var1, onvalue = 1, offvalue = 0)#makes a check box and sets on and off values. Also packs each one

c1.pack()

c2 = Checkbutton(main, text = "2", variable = var2, onvalue = 1, offvalue = 0)

c2.pack()

c3 = Checkbutton(main, text = "3", variable = var3, onvalue = 1, offvalue = 0)

c3.pack()

ch = Label(main)#makes a label to print output
ch.pack()

def buttonPress():
    if var.get() == "dog":#checks for each animal and adds a color to string, also for fun I changed the background
        selection = "Blue "
        main.configure(bg='blue')
    elif var.get() == "cat":
        selection = "Orange "
        main.configure(bg='orange')
    elif var.get() == "bird":
        selection = "Yellow "
        main.configure(bg='yellow')
    else:
        selection = "Black and White "
        main.configure(bg='white')
    selection += var.get()#adds the animal name to the string
    ra.config(text = selection)#I learned I can just do this rather than setting a StringVar and packing again
    
    if var1.get() == 1:#checks each check box and sets the string to yes or no depending on if it is checked
        str1 = "Yes"
    else:
        str1 = "No"
    
    if var2.get() == 1:
        str2 = "Yes"
    else:
        str2 = "No"
    
    if var3.get() == 1:
        str3 = "Yes"
    else:
        str3 = "No"
    ch.config(text = (str1 + " - " + str2 + " - " + str3))#prints to the checkbox label



bub = Button(text = "Button", command = buttonPress)#makes a button to use the button press comand
bub.pack()#packs button

main.mainloop()