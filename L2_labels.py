from tkinter import *

#label = an area widget that holds text and/or an image within a window

# To create a winow 
window = Tk()

photo = PhotoImage(file='./photos/coder.png')

label = Label(window,
              text='Hello Dunya', 
              font=('Arial',40,'bold'),
              fg='blue',  #fg means foreground (text color)
              bg='lightblue',
              relief=RAISED, # Lets change how our label border looks
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom') 
            
label.pack() #This will display the text on the window by default top center





# To keep the window active so it doesn't close
window.mainloop()