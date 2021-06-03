from tkinter import *

janela = Tk()

lb1 = Label(janela, text="Label 1")
lb1.grid(row=3, column=1)


janela.geometry("300x300+200+200")
janela.mainloop()