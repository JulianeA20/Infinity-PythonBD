pacientes = int(input("Informe o numero de pacientes: "))
pacientes_graves = 0
assintomaticos = 0
pacientes_leves = 0
for i in range(0,pacientes):
    estado = input(f"Insira estado do paciente {i+1}: ")
    if estado == "grave":
        pacientes_graves += 1
    elif estado == "assintomatico":
        assintomaticos += 1
    elif estado =="leve":
        pacientes_leves +=1
    else:
        print("Valor digitado inválido")
        estado = input(f"Insira estado do paciente {i+1}: ")


    print(f"O total de pacientes graves é {'total_graves = pacientes_graves / 100'}%")
    print(f"O total de pacientes assintomaticos é {'total_assintomaticos = assintomaticos / 100'}%")
    print(f"O total de pacientes com sintomas leves é {'total_leves = pacientes_leves / 100'}%")