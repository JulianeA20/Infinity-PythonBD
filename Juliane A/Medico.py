from pydoc import cram


class Medico:
    def __init__(self, crm, nome, idade, salario):
        self.crm = crm
        self.nome = nome
        self._idade = idade
        self.salario = salario

    @property
    def Idade(self):
        return self._idade

    @Idade.setter
    def 

    def VerificarAposentadoria(self):
            if self._idade >= 55:
               return True
            else:
                return None
                
                


'''self._salario -= (80/100)* self._salario
aposentadoria = self._salario
return f"Sua aposentadoria será de R$ {aposentadoria}"'''