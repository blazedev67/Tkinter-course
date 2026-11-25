from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get())+ " degrees C")
window = Tk()

hotImage = PhotoImage(file='./photos/fire.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()


scale = Scale(window,from_=100,to=0,
              length=600,
              orient=VERTICAL, #orientation of scale
              font=('Consolas',20),
              tickinterval=10, #this adds numeric indicators for value
              showvalue=0, #hide current value
              resolution=5, #increment of slider
              troughcolor='#69eaff',
              fg='#FF1C00',
              bg='#111111')
scale.set((scale['from']-scale ['to'])/2+scale['to']) #set current value of slider with fancy formula
# scale.set(50)  unfancy way

scale.pack()

iceImage = PhotoImage(file='./photos/snow.png')
iceLabel = Label(image=iceImage)
iceLabel.pack()


button = Button(window, text='submit',command=submit)
button.pack()

window.mainloop()