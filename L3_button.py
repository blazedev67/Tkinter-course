from tkinter import *

# button = you click it, then it does stuff

count = 0

def click():
    global count
    count += 1
    print(count)

window = Tk()

photo = PhotoImage(file='./photos/like.png')

button = Button(window,
                text='Click me boi!',
                command=click,
                font=('Comis Sans', 30),
                fg='#00ff00',
                bg='black',
                activeforeground='#00ff00',
                activebackground='black',
                state=ACTIVE,
                image=photo,
                compound='bottom')
button.pack()

window.mainloop()