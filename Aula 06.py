from tkinter import *

janela = Tk()

def muda_texto():
    print("bt_click")
    lb["text"] = "Funcionou!"

bt = Button(janela, width=20, text="Clica", command=muda_texto)
bt.place(x=100, y=100)

lb = Label(janela, text="Teste")
lb.place(x=100, y=150)



janela.geometry("300x300+200+200")
janela.mainloop()