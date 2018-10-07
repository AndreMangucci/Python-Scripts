from tkinter import *
import random

def callback():
    print(random.randrange(1,21))
import random

def callback():
    print(random.randrange(1,21))

class Application(Frame):
    

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(b1,B2):
        b1.myButton = Button(self, text='b1',command=callback)
        b1.myButton.grid()
        b1.place(relx = 0.5,rely = 0.5,anchor=CENTER)

        b2.myButton = Button(self, text='b2',command=callback)
        b2.myButton.grid()
        b2.place(relx = 0.5,rely = 0.3,anchor=CENTER)
        
        mainloop()

        
root = Tk()

root.title('First GUI app')
root.geometry('300x200')

app = Application(root)
root.mainloop()

