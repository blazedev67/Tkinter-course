from tkinter import *

window = Tk()
window.geometry("500x500")

canvas = Canvas(window, height=500, width=500, bg='white')

canvas.pack()

# canvas.create_line(0, 0, 500, 500, fill='blue', width=5)
# canvas.create_line(0, 500, 500, 0, fill='red', width=5)
#when lines overlap the most recent one will be on top 
# canvas.create_rectangle(50,50,100,200,fill='pink')
# points = [250,0,500,500,0,500]
# canvas.create_polygon(points, fill='yellow',outline="black",width=6)
# canvas.create_arc(0,0,500,500,style=PIESLICE,start=270,extent=180)
canvas.create_arc(0,0,500,500,fill="red",extent=180,width=8)
canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=8)
canvas.create_oval(190,190,310,310,fill='white',width=10)


window.mainloop()