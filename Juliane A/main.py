from Funcionario import Funcionario
from Gerente import Gerente

funcionario = Funcionario("Lucas","92801018821", 1500)

gerente = Gerente("Danilo", "98278619729", 2000, '1234', 20)
plano_saude = 300
inss = 200
i_r = 500
lista_descontos = [plano_saude, inss, i_r]
salario_liquido = gerente.salarioLiquido(lista_descontos)
print(salario_liquido)
