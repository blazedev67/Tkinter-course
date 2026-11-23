from tkinter import *

# entry widget = textbox that accepts a single line of user input
 
def submit():
    username =  entry.get() # get the current value within our entry box returns string
    print("Hello "+ username)
    

def delete():
    entry.delete(0,END) #from index 0 to end

def backspace():
    entry.delete(len(entry.get())-1,END)

window = Tk()

entry = Entry(window,
              font=('Arial', 50),
              fg='#00ff00',
              bg='black')

# To display texts with the follwing character ideal for passwords
#entry.config(show="*")

# To insert a default text at index 0
#entry.insert(0,'Spongebob')

# Intserting default text for entry box
# entry.insert(0,'Spongebob')

entry.pack(side=LEFT)

submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()
