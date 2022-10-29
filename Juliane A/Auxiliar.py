from Medico import Medico
class Auxiliar(Medico):
    def __init__(self, crm, nome, idade, salario, cargo):
        super().__init__(crm, nome, idade, salario)
        self._cargo = cargo


    def VerificarIdade(self):
            if self._idade <= 60:
                    self._salario -= (80/100)* self._salario
                    aposentadoria = self._salario
                    return f"Sua aposentadoria será de R$ {aposentadoria}"
            else:
                return None