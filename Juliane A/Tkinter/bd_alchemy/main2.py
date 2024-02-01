from tkinter import *
from tkinter.ttk import Treeview
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from carro import Carro

engine=sqlalchemy.create_engine('mysql+pymysql://u221579840_inf_warehouse:Inf_warehouse123@sql775.main-hosting.eu/u221579840_inf_warehouse')
sm = sessionmaker(bind=engine)
session = sm()

root = Tk()
root.geometry("400x400")
root.title("Cadastro de Carros")

treeView = Treeview(root,columns=("colMarca", "colModelo", "colCor", "colPlaca"), show="headings")

treeView.column('colMarca',width=60)
treeView.heading('colMarca', text='Marca')

treeView.column('colModelo',width=60)
treeView.heading('colModelo', text='Modelo')

treeView.column('colCor',width=60)
treeView.heading('colCor', text='Cor')

treeView.column('colPlaca',width=85)
treeView.heading('colPlaca', text='Placa')

treeView.grid(row=6,column=0, columnspan=3)

dados = session.query(Carro).all()

for carro in dados:
    treeView.insert("","end",values=[carro.marca,carro.modelo,carro.cor,carro.placa])

root.mainloop()