# radio button = similar to checkbox , but you can only select one from a group 


from tkinter import * 

# lets create a list of available food items
food = ['pizza','tea','coffee','shawarma']

def order():
    if(x.get()==0):
        print("You ordered a pizza!")
    elif(x.get()==1):
        print('You ordered a tea!')
    elif(x.get()==2):
        print('You ordered a coffee!')
    elif(x.get()==3):
         print('You ordered a shawarma!')
    else:
        print('huh?')

window = Tk()

# Lets create images for the food items

pizzaImage = PhotoImage(file='./photos/pizza.png')
shawarmaImage = PhotoImage(file='./photos/shawarma.png')
coffeeImage = PhotoImage(file='./photos/coffee.png')
teaImage = PhotoImage(file='./photos/tea.png')

foodImages = [pizzaImage,teaImage,coffeeImage,shawarmaImage]


x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], # adds text to radio buttons
                              variable=x, #groups radiobuttons together if they share the same variable
                              value=index, #assigns each radiobuttons a different value
                              padx=25,
                              font=('Impact',50),
                              image=foodImages[index], # adds images to radiobuttons
                              compound='left',  # adds image and text (left-side)
                              indicatoron=0, # eliminate circle indicators
                              width= 400, #sets width of radiobuttons
                              fg='black',
                              command=order #this will set command of radiobutton to function
                              ) 
     
    radiobutton.pack(anchor=W) # W means west

window.mainloop()