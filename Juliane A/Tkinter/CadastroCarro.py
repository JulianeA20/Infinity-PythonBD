from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import mysql.connector

def getConnection():
    connection = mysql.connector.connect(user='u221579840_inf_warehouse', 
                                     password='Inf_warehouse123',
                                     host='sql775.main-hosting.eu',
                                    database='u221579840_inf_warehouse')
    return connection

def buscarDados():

    treeView.delete(*treeView.get_children())

    conn = getConnection()

    cursor = conn.cursor()
    sql = (f"SELECT * FROM carro")
    cursor.execute(sql)

    for (marca,modelo,cor,placa) in cursor:
        treeView.insert("","end", values=[marca,modelo,cor,placa])

    conn.close()

    treeView.delete()

def cadastrar():
    conn = getConnection()
    cursor = conn.cursor()
    marca = entryMarca.get()
    modelo = entryModelo.get()
    cor = entryCor.get()
    placa = entryPlaca.get()
    
    if placa == "":
        messagebox.showerror(title="Erro", message="Placa deve ser informada")
        return
    
    sql  = (f"INSERT INTO carro VALUES('{marca}','{modelo}','{cor}','{placa}')")
    cursor.execute(sql)    
    conn.commit()
    conn.close()
    
    entryMarca.delete(0,END)
    entryModelo.delete(0,END)
    entryCor.delete(0,END)
    entryPlaca.delete(0,END)
    
    messagebox.showinfo(title="Sucesso",message="Cadastrado com Sucesso!")
    
    buscarDados()
    
def atualizar():
    conn = getConnection()
    cursor = conn.cursor()
    marca = entryMarca.get()
    modelo = entryModelo.get()
    cor = entryCor.get()
    placa = entryPlaca.get()
    
    if placa == "":
        messagebox.showerror(title="Erro", message="Placa deve ser informada")
        return
    
    sql = (f"UPDATE carro SET marca ='{marca}', modelo='{modelo}', cor='{cor}' WHERE placa='{placa}'")
    cursor.execute(sql)
    conn.commit()
    conn.close()
    
    messagebox.showinfo(title="Sucesso", message="Atualizado com sucesso")

    buscarDados()
    
def excluir():
    conn = getConnection()
    cursor = conn.cursor()
    placa = entryPlaca.get()
    
    if placa == "":
        messagebox.showerror(title="Erro", message="Placa deve ser informada")
        return
    
    sql = (f"DELETE FROM carro WHERE placa like '{placa}'")
    cursor.execute(sql)
    conn.commit()
    conn.close()
    
    messagebox.showinfo(title="Sucesso", message="Excluído com sucesso")

    buscarDados()
   
    
font1 = ('Georgia 10')

root = Tk()
root.geometry("400x400")
root.title("Cadastro de Carro")

lblMarca = Label(root, text="Marca", font=font1)
lblMarca.grid(row=0,column=0)
entryMarca = Entry(root)
entryMarca.grid(row=0,column=1)

lblModelo = Label(root, text="Modelo", font=font1)
lblModelo.grid(row=1,column=0)
entryModelo = Entry(root)
entryModelo.grid(row=1,column=1)

lblCor = Label(root, text="Cor", font=font1)
lblCor.grid(row=2,column=0)
entryCor = Entry(root)
entryCor.grid(row=2,column=1)

lblPlaca = Label(root, text="Placa", font=font1)
lblPlaca.grid(row=3,column=0)
entryPlaca = Entry(root)
entryPlaca.grid(row=3,column=1)

btnCadastrar = Button(root, text="Cadastrar", command=cadastrar)
btnCadastrar.grid(row=4,column=0)

btnAtualizar = Button(root,text="Atualizar", command=atualizar)
btnAtualizar.grid(row=4,column=1)

btnExcluir = Button(root,text="Excluir", command=excluir)
btnExcluir.grid(row=4,column=2)

btnBuscar = Button(root, text="Buscar", command=buscarDados)
btnBuscar.grid(row=4,column=3)

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

buscarDados()

root.mainloop()
