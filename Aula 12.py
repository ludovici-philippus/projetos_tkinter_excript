from tkinter import *

janela = Tk()
lb1 = Label(janela, text="Side 1", bg="white")
lb2 = Label(janela, text="Side 2", bg="green")
lb3 = Label(janela, text="Anchor 1", bg="red")
lb4 = Label(janela, text="Anchor 2", bg="yellow")

lb1.pack(side=LEFT)
lb2.pack(side=LEFT)
lb3.pack(anchor=NW)
lb4.pack(side=BOTTOM, anchor=SW)



janela.geometry("400x300+200+200")
janela.mainloop()