from Medico import Medico
class Cirurgiao(Medico):
    def __init__(self, crm, nome, idade, salario, funcao):
        super().__init__(crm, nome, idade, salario)
        self._funcao = funcao


    def VerificarIdade(self):
            if self._idade <= 50:
                    self._salario -= (80/100)* self._salario
                    aposentadoria = self._salario
                    return f"Sua aposentadoria será de R$ {aposentadoria} "
            else:
                return None
        