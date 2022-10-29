eleitores_total = int(input("Informe o número total de eleitores:"))

votos_brancos = int(input("Informe o número de votos brancos:"))

votos_nulos = int(input("Informe o número de votos nulos:"))

votos_validos =int(input("Informe o número total de votos brancos: "))

percent_votos_brancos = votos_brancos / eleitores_total
percent_votos_nulos = votos_nulos / eleitores_total
percent_votos_validos = votos_validos / eleitores_total 

print("percentual de votos brancos é:", int(percent_votos_brancos * 100), '%')
print("O percentual de votos nulos é:", int(percent_votos_nulos * 100, '%'))
print("O percentual de votos validos é:", int(percent_votos_validos * 100, '%'))



