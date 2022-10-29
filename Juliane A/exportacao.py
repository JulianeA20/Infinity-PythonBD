valor_tonelada = int(input("Informe o valor por tonelada: "))
quantidade = 0
while True:
    mes = input("Informe o mês (Ou digite 'sair' para sair): ")
    if mes == "sair":
        break
    else:
        quantidade = float(input(f"Informe o valor para o mês de {mes}: "))
        quantidade = quantidade + quantidade

print(f"O total faturado foi {quantidade * valor_tonelada}")
print("Fim.")