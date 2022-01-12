#Jose Andres Zamora

import tkinter
from tkinter import *
import random

page = tkinter.Tk()#make page
page.geometry("500x500")#set the size to 300x300

page.configure(bg='#732828')#Cool hex color I found
page.title("Hello World!")#Made the title the usual

words = StringVar()#make a string
word = StringVar()
output = Label(page, textvariable = words, font = ("Courier", 16), bg = '#eeeeee', fg = '#181818')#set details
words.set("This is a thing")#change string
output.pack()#pack

output2 = Label(page, textvariable = word, font = ("Helvetica", 24), bg = '#181818', fg = '#eeeeee')#set new details
word.set("Waiting...")#change string
output2.pack()#pack

def firstButtonPressed():
    words.set("Button 1 was pressed")
    output.pack()
def secondButtonPressed():
    words.set("Generating Random Number...")
    output.pack
    num = random.randint(0, 100)
    word.set(str(num))
    output3 = Label(page, textvariable = word, font = ("Helvetica", 24), bg = '#000080', fg = '#ffffff')
    output3.pack

beu = Button(page, text = "Press here", command = firstButtonPressed)
beu.place(x = 205,y = 75)
ueb = Button(page, text = "Random Number", height = 2, width = 15, command = secondButtonPressed)
ueb.place(x = 180,y = 100)

page.mainloop()#keeps page running I think
