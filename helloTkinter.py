from tkinter import *
window = Tk()
window.geometry("420x420") # Width and height of the window

icon = PhotoImage(file='./photos/logo.png') #Tkinker uses Photo Image format 
window.iconphoto(True,icon)         

window.title("Abdur Rahman first GUI programs")

window.config(background='#dbbc5c') # Changes background color of our window 
window.mainloop()