from Medico import Medico
from Auxiliar import Auxiliar
from Cirurgiao import Cirurgiao

medico = Medico("9336", "Daniel", 55, 4000)

auxiliar = Auxiliar("28273", "Vitor", 60, 2500, "auxiliar")

cirurgiao = Cirurgiao("28363", "Antonio", 50, 7000, "cirurgiao")

print(medico.VerificarAposentadoria())