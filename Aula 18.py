from tkinter import *

janela = Tk()

lb1 = Label(janela, text="ESPAÇO", width="20", height="3", bg="blue")
lb_horizontal = Label(janela, text="HORIZONTAL", width="10", bg="yellow")
lb_vertical = Label(janela, text="VERTICAL", bg="green")

lb1.grid(row=0, column=0)
lb_horizontal.grid(row=1, column=0, sticky=E)
lb_vertical.grid(row=0, column=1, sticky=N)

janela.geometry("300x300+200+200")
janela.mainloop()