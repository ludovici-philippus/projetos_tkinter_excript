from tkinter import *

janela = Tk()

lb = Label(janela, text="Horizontal", bg="green")
lb2 = Label(janela, text="", bg="blue")
lb3 = Label(janela, text="", bg="blue")

lb.pack(side=TOP, fill=X)
lb2.pack(side=LEFT, fill=Y)
lb3.pack(side=RIGHT, fill=Y)


janela.geometry("300x300+200+200")
janela.mainloop()