from tkinter import *

janela = Tk()

def bt_onclick():
    print(ed.get())
    lb["text"] = ed.get()

ed = Entry(janela)
ed.place(x=100, y=100)


bt = Button(janela, width=20, text="Ok", command=bt_onclick)
bt.place(x=100, y=150)

lb = Label(janela, text="Label")
lb.place(x=100, y=200)


janela.geometry("300x300+300+300")
janela.mainloop()