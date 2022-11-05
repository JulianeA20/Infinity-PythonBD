from tkinter import *
from tkinter.ttk import Treeview
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from aluno import Aluno

engine=sqlalchemy.create_engine('mysql+pymysql://u221579840_inf_warehouse:Inf_warehouse123@sql775.main-hosting.eu/u221579840_inf_warehouse')
sm = sessionmaker(bind=engine)
session = sm()

root = Tk()
root.geometry("400x400")
root.title("Cdastro de Alunos")

treeView = Treeview(root,columns=("colId","colNome"),show="headings")

treeView.column('colId',width=60)
treeView.heading('colId', text='ID')

treeView.column('colNome',width=100)
treeView.heading('colNome',text='Nome')

treeView.grid(row=0,column=0)

dados = session.query(Aluno).all()

for aluno in dados:
    treeView.insert("","end",values=[aluno.id,aluno.nome])

root.mainloop()