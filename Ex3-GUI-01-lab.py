#Jose Andres Zamora

import tkinter
from tkinter import *

page = tkinter.Tk()#make page
page.geometry("300x300")#set the size to 300x300

page.configure(bg='#732828')#Cool hex color I found
page.title("Hello World!")#Made the title the usual

words = StringVar()#make a string
output = Label(page, textvariable = words, font = ("Courier", 16, "italic"), bg = '#eeeeee', fg = '#181818')#set details
words.set("These are words")#change string
output.pack()#pack

output2 = Label(page, textvariable = words, font = ("Helvetica", 24), bg = '#181818', fg = '#eeeeee')#set new details
words.set("And you are you")#change string
output2.pack()#pack

page.mainloop()#keeps page running I think
