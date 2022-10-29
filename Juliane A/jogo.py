import random
numero_sorteado = random.randrange(1,10)
print(numero_sorteado)

while True:
    numero = int(input("Informe o número: "))
    if numero ==  numero_sorteado:
        print("Acertou! O número sorteado é", numero_sorteado)
        break
    else:
        if numero > numero_sorteado:
            print("Tente um número menor")
        else:
            print("Tente um número maior")
        
print("Fim do programa.")
