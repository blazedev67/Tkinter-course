from tkinter import *
from tkinter import colorchooser #submodule

def click():
    color = colorchooser.askcolor()
   
  
    window.config(bg=color[1]) #change bg color

window = Tk()
window.geometry("420x420")

button = Button(text='click me',command=click)
button.pack()

window.mainloop()
