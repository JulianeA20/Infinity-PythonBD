def ValidarOperacao(op):
        while op not in ("+-*/"):
            op = input("Insira uma operação válida: ")
        return op

def CalculoNumerico(n1,n2,op):

    if op == "+":
        soma = n1 + n2
        return soma
    if op == "-":
        sub = n1 - n2
        return sub
    if op == "*":
        multiplicacao = n1 * n2
        return multiplicacao
    if op == "/":
        divisao = n1 /n2
        return divisao


num_1 = float(input("Informe um número: "))
num_2 = float(input("Informe outro número: "))
operacao = str(input("Escolha a operacao (+), (-), (*) ou (/): "))
operacao = ValidarOperacao(operacao)

resultado = CalculoNumerico(num_1,num_2, operacao)
print(f"O valor de {num_1} {operacao} {num_2} = {resultado}")
