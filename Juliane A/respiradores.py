qtd_respiradores = int(input("Informe a quantidade de respiradores: "))
taxa_ocupacao = float(input("Informe a taxa de ocupação (em %): "))
qtd_respiradores_nova = qtd_respiradores

if qtd_respiradores < 50 and taxa_ocupacao > 60:
    qtd_respiradores += 5

if qtd_respiradores != qtd_respiradores_nova:
    print("Novos respiradores adicionados")
else:
    print("Respiradores suficientes")

print("A quantidade de respiradores é:", qtd_respiradores_nova)

