materia = input("Informe o nome da matéria: ")
quantidade_notas = int(input("Informe a quantidade de notas desejada: "))
total = 0

for i in range(0,quantidade_notas):
    nota = float(input(f"Informe a nota {i+1}: "))  
    total = nota + total

media = total/quantidade_notas
print(f"A média de {materia} é", media)

if media > 6:
    print("Aprovado!")
elif media >= 5 and media < 6:
    print("Recuperação")
else:
    print("Reprovado!")


