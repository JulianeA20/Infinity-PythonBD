cancela = False

temperatura = float(input("Informe a temperatura: "))

cancela = temperatura <= 37 and temperatura >= 36

if cancela == True:
     print("Acesso liberado")
else:
    print("Acesso restrito, temperatura anormal")
    