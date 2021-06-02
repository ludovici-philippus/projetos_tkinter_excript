from tkinter import *

janela = Tk()

def somar():
    if str(e_primeiro.get()).isnumeric() and str(e_segundo.get()).isnumeric():
        resultado = float(float(e_primeiro.get()) + float(e_segundo.get()))
        lb_resultado["text"] = resultado
    else:
        lb_resultado["text"] = "Não é um número!"

e_primeiro = Entry(janela)
e_primeiro.place(x=100, y=100)

e_segundo = Entry(janela)
e_segundo.place(x=100, y=125)

bt_somar = Button(janela, width=20, text="Somar", command=somar)
bt_somar.place(x=100, y=175)

lb_resultado = Label(janela, text="Resultado")
lb_resultado.place(x=100, y=225)



janela.geometry("300x300+300+300")
janela.mainloop()