import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter import *

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, NOTASDESAIDA, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def Options(*args,tkvar,self):

        if tkvar == 'NOTAS DE SAIDA':
            self.controller.show_frame('NOTASDESAIDA')

        if tkvar == 'NOTAS DE ENTRADA':
            self.controller.show_frame('NOTASDEENTRADA')

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Selecione o tipo de etiqueta", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        tkvar = tk.StringVar()

        #Options
        choices = {'NOTAS DE SAIDA','NOTAS DE ENTRADA'}

        popupMenu = tk.OptionMenu(self,tkvar,*choices)
        tkvar.set('NOTAS DE SAIDA')
        popupMenu.pack()

        button1 = tk.Button(self, text="Selecionar", width=10,command=self.Options(tkvar=tkvar.get(),self=self))
        button2 = tk.Button(self, text="Sair",command=self.quit,width=10)

        button1.pack()
        button2.pack()

        def quit(self):
            self.root.destroy


class NOTASDESAIDA(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()