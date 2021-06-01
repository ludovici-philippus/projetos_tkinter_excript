#import tkinter as tk

"""janela = tk.Tk()
janela.title("Janela principal.")
janela["bg"] = "green"

janela.geometry("600x600+100+100")



janela.mainloop()"""

from tkinter import *

janela = Tk()

janela.title("Janela")

lb = Label(janela, text="Fala galera!")
lb.place(x=150, y=150) # Place = Gerenciador de layout.
# WxH+L+T
janela.geometry("300x300+200+200")

janela.mainloop()