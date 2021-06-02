from tkinter import *

janela = Tk()

lb1 = Label(janela, text="RIGHT", bg="white")
lb2 = Label(janela, text="LEFT", bg="red")
lb3 = Label(janela, text="TOP", bg="blue")
lb4 = Label(janela, text="BOTTOM", bg="yellow")

lb1.pack(side=RIGHT)
lb2.pack(side=LEFT)
lb3.pack(side=TOP)
lb4.pack(side=BOTTOM)

janela.geometry("300x300+200+200")
janela.mainloop()