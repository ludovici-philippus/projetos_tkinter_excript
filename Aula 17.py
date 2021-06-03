from tkinter import *

janela = Tk()

login = StringVar()
senha = StringVar()


lb_login = Label(janela, text="Login: ")
lb_login.grid(row=1, column=1)

e_login = Entry(janela, textvariable=login)
e_login.grid(row=1, column=10)

lb_senha = Label(janela, text="Senha: ")
lb_senha.grid(row=10, column=1)

e_senha = Entry(janela, textvariable=senha)
e_senha.grid(row=10, column=10)

bt_continuar = Button(janela, width=10, text="Continuar")
bt_continuar.grid(row=20, column=10)


janela.geometry("200x100+200+200")
janela.mainloop()