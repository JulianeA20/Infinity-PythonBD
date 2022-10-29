  
def ObterSaudacao(horario = 12):
    if horario < 0:
        return "Horário informado foi menor que zero", False 
    if horario > 24:
        return "Horário informado foi maior que 24", False

    if horario <= 12:
        return "Bom dia!", True
    elif horario > 12 and horario <= 18:
        return "Boa tarde!", True
    else:
        return "Boa noite!", True
    

hora = float(input("Informe a hora: "))
saudacao, erro = ObterSaudacao((hora))

if erro == False:
    print("Erro! Hora inválida!")
else: 
    print(saudacao)

