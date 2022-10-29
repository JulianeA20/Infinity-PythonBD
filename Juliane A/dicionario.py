

alunos = []

for i in range(0,2):  
    aluno = {}
    aluno["nome"] = input("Informe um nome: ")
    aluno["telefone"] = input("Informe um telefone: ")
    while aluno["telefone"].isnumeric() == False:
        aluno["telefone"] = input("Informe um telefone: ")
    alunos.append(aluno)


print(alunos)            





