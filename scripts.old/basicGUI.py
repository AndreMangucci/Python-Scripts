import tkinter as tk
import time

root = tk.Tk()
root.geometry("200x200")
root.config(background="black")

def chcolor() :
    root.config(background="orange")
def chcolor2():
    root.config(background="red")
def chcolor3():
    root.config(background="#ff3399")
def chcolor4():
    root.config(background="blue")
def chcolor5():
    root.config(background="purple")
def chcolor6():
    root.config(background="#999999")
def chcolor7():
    root.config(background="orange")
    time.sleep(1)
    root.config(background="red")
    time.sleep(1)
    root.config(background="#ff3399")
    time.sleep(1)
    root.config(background="blue")
    time.sleep(1)
    root.config(background="purple")    
    time.sleep(1)
    root.config(background="#999999")
    time.sleep(1)

b1 = tk.Button(root,text = 'Laranja',fg ='orange',width = 12,command=chcolor)
b1.grid()

b2= tk.Button(root,text = 'Vermelho',fg ='red',width = 12,command=chcolor2)
b2.grid()

b3 = tk.Button(root,text = 'Rosa',fg ='#ff3399',width = 12,command=chcolor3)
b3.grid()

b4 = tk.Button(root,text = 'Azul',fg ='blue',width = 12,command=chcolor4)
b4.grid()

b5 = tk.Button(root,text = 'Roxo',fg ='purple',width = 12,command=chcolor5)
b5.grid()

b6 = tk.Button(root,text = 'Cinza',fg ='gray',width = 12,command=chcolor6)
b6.grid()

b7 = tk.Button(root,text = 'RAFA',fg ='yellow',width = 12,command=chcolor7)
b7.grid()

root.mainloop()


