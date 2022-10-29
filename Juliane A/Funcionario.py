class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def salarioLiquido(self, itens_descontos):
        liquido = self._salario
        for desconto in itens_descontos:
            liquido -= desconto
        return liquido