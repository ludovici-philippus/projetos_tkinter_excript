from tkinter import *

janela = Tk()

lb1 = Label(janela, text="Label 1", bg="green")
lb2 = Label(janela, text="Label 2", bg="blue")
lb3 = Label(janela, text="Label 3", bg="red")
lb4 = Label(janela, text="Label 4", bg="yellow")

lb1.pack()
lb2.pack()
lb3.pack()
lb4.pack(side=BOTTOM)



janela.geometry("400x300+200+200")
janela.mainloop()