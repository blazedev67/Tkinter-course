from tkinter import *
from tkinter import filedialog

def openFile():
    filePath = filedialog.askopenfilename(initialdir='/Users/abdurrahman/Desktop/Tkinter_Course',
    title='Open file boii',
    filetypes= (('text files','*.txt'),
    ('all files', '*.*'))) 
    file = open(filePath,'r')
    print(file.read())
    file.close()


window = Tk()

button = Button(text='Open',command=openFile)
button.pack()
window.mainloop()