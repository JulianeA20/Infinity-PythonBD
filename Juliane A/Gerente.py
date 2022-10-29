from Funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qt_gerenciados):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qt_gerenciados = qt_gerenciados

    def Descricao(self):
        return self._nome + " gerencia " + str(self._qt_gerenciados) + " pessoas"