import random as rnd
print(rnd.randint(1,20))
import tkinter as tk
master=tk.Tk()
def d20():
    print(rnd.randint(1,20))
but=tk.Button(master,command=d20)
but.grid()
