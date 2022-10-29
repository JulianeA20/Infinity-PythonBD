from functools import lru_cache
from operator import indexOf


ListaDeNomes = []

for i in range(0, 5):
    nomes = input("Insira um nome: ")
    ListaDeNomes.append(nomes)
    
for i in range(0,len(ListaDeNomes)):
    if i == len(ListaDeNomes) -1:
        print(ListaDeNomes[i],end=".")
    else:
        print(ListaDeNomes[i],end=", ")

parametro = input("Informe o parâmetro (pop) ou (remove): ")

i=0
while i==0:
    if parametro == 'pop':
        item = int(input("Informe o número que deseja remover: "))
        ListaDeNomes.pop(item)
        print(ListaDeNomes)
    elif parametro == 'remove':
        item = int(input("Informe o nome que deseja remover: "))
        ListaDeNomes.remove(item)
        print(ListaDeNomes)
    else:
        print("Parâmetro inválido!")




