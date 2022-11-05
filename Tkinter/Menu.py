from tkinter import *
from tkinter import messagebox

def abrirTelaUsuarios():
    messagebox.showinfo(title="Sucesso",message="Abrindo tela de Usuarios...") 
    
def abrirTelaCarros():
    messagebox.showinfo(title="Sucesso",message="Abrindo tela de Carros...")    
    
def abrirRelatorioVendas():
    messagebox.showinfo(title="Sucesso",message="Abrindo tela de Relatório...")    
    
root = Tk()
root.title("Menus")

menuBar = Menu(root)
root.config(menu=menuBar)

cadastroMenu = Menu(menuBar)

menuBar.add_cascade(
    label="Cadastro",
    menu=cadastroMenu
)

relatorioMenu = Menu(menuBar)

menuBar.add_cascade(
    label="Relatórios",
    menu=relatorioMenu
)

cadastroMenu.add_command(
    label="Usuários",
    command=abrirTelaUsuarios
)

cadastroMenu.add_command(
    label="Carros",
    command=abrirTelaCarros
)

relatorioMenu.add_command(
    label="Relatório de vendas",
    command=abrirRelatorioVendas
)


root.mainloop()
