from tkinter import *
from tkinter import messagebox # imports messagebox library

def click():
   
    # messagebox.showinfo(title='This is an info messagebox',message='You are a person')
    # messagebox.showwarning(title='WARNING!',message='You have a virus')
    # messagebox.showerror(title='ERROR!',message='something went wrong :(')
    #if messagebox.askokcancel(title='ask ok cancel!',message='Do you want to do the thing?'):
        #print('You did a thing!')
    #else:
        #print('You canceld a thing!') 


    #if messagebox.askretrycancel(title='ask ok cancel!',message='Do you want to retry the thing?'):
     #   print('You retried a thing!')
    #else:
     #   print('You canceld a thing!') 

    #if messagebox.askyesno(title='ask yer or no',message='Do you like cake?'):
    #    print('I also like cake :)')
    #else:
    #    print('why do you not like a cake? :(')

    #answer = messagebox.askquestion(title='ask question',message='Do you like shawarma?')
    #if(answer == 'yes'):
    #    print('I also like shawarma')
    #else:
    #    print('why do you not like shawarma')

    answer1 = messagebox.askyesnocancel(title='Yes no cancel', message='Do you like to code?',icon='error')
        
    if(answer1 ==True):
        print('You like to code')
    elif(answer1==False):
      print('Then why are you watching a video on coding?')
    else:
      print('You have dodged the question')
   
   
   
window = Tk()

button = Button(window, command=click,text='click me!')
button.pack()

window.mainloop()