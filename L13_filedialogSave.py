from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(
                                    initialdir='/Users/abdurrahman/ Desktop/Tkinter_Course',
                                    defaultextension='.txt',
                                    filetypes=[
                                        ('Text file','.txt'),
                                        ('HTML file','.html'),
                                        ('All files','.*'),

                                    ])
    if file is None:
        return
    fileText = str(text.get(1.0,END))
    # fileText = input("Enter some Text here:")  # use this for to enter text from console
    file.write(fileText)
    file.close()


window = Tk()

button = Button(text='save',command=saveFile)
button.pack()

text = Text(window)
text.pack()

window.mainloop()
