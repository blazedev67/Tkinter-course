from tkinter import *

def create_window():
    #Toplevel() = new window 'on top' of other windows, linked to a 'bottom' window
    #Tk() = new independent window
    new_window = Tk()
    old_window.destroy() #close out old window

old_window = Tk()

Button(old_window,text='create new window',command=create_window).pack()
old_window.mainloop()