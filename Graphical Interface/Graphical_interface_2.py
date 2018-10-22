# Multi-frame tkinter application v2.3
import tkinter as tk


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # Create a Tkinter variable
        tkvar = tk.StringVar()

        # Dictionary with options
        choices = {'NOTAS FISCAIS DE SAIDA', 'NOTAS FISCAIS DE ENTRADA'}
        tkvar.set('NOTAS FISCAIS DE SAIDA')  # set the default option

        tk.Label(self, text="Selecione o tipo de etiqueta : ").pack(side="top", fill="x", pady=10, padx=10)
        tk.OptionMenu(self, tkvar, *choices).pack(padx=10)

        self.mybutton = tk.Button(self, text="Selecionar", command=lambda: master.switch_frame(PageOne))

        # on change dropdown value
        def change_dropdown(*args):
            print(tkvar.get())

            if tkvar.get() == 'NOTAS FISCAIS DE SAIDA':
                self.mybutton.destroy()
                self.mybutton = tk.Button(self, text="Selecionar", command=lambda: master.switch_frame(PageOne))
                self.mybutton.pack(side="top", fill="x", pady=10, padx=10)

            if tkvar.get() == 'NOTAS FISCAIS DE ENTRADA':
                self.mybutton.destroy()
                self.mybutton = tk.Button(self, text="Selecionar", command=lambda: master.switch_frame(PageTwo))
                self.mybutton.pack(side="top", fill="x", pady=10, padx=10)

        # link function to change dropdown
        tkvar.trace('w', change_dropdown)


class PageOne(tk.Frame):

    def print_item_values(*args):
        a = item_1.get()
        print(a)

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Notas fiscais de saida").pack(side="top", fill="x", pady=10)

        item_1 = tk.IntVar()

        tipo = "NOTAS FISCAIS DE SAÍDA"

        item_1 = tk.Spinbox(master, from_=0, to=1000000).pack(pady=10, padx=10)

        tk.Button(self, text="Imprimir", command = self.print_item_values).pack()

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Notas fiscais de entrada").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page", command=lambda: master.switch_frame(StartPage)).pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()