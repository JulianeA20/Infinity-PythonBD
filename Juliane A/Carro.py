

class Carro:
    def __init__(self, marca, modelo, ano, velocidade, pista, sistema = False, ligado = False):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._velocidade = velocidade
        self._velocidade_maxima = 120
        self._sistema = sistema
        self._ligado = ligado
        self._pista = pista

    def Verificar_Ligado(self):
        if self._ligado == False:
            return "---Ligue o carro---"
        if self._ligado == True:
            return ":::Carro ligado, acelere:::"


    def Verificar_Marcha(self):
        if self._velocidade <= 19:
            return "1° Marcha"
        elif self._velocidade >= 20 and self._velocidade <= 29:
            return "2° Marcha"
        elif self._velocidade >= 30 and self._velocidade <= 39:
            return "3° Marcha"
        elif self._velocidade >= 40 and self._velocidade <= 49:
            return "4° Marcha"
        elif self._velocidade >= 60 and self._velocidade <= 120:
            return "5° Marcha"
        else:
            return "Velocidade acima do permitido! Insira uma velocidade válida"

    def Verificar_Pista(self):
        
        if self._pista == "-" and self._velocidade >= 25:
            return "Ladeira abaixo, diminua a velocidade!"
        else:
            return "Ladeira! Desça!"
        
        if self._pista == "+" and self._velocidade >= 19:
            return "Ladeira acima, diminua a velocidade!"
        else:
            return "Ladeira! Pode subir!"
        
            if self._pista == "<":
                return "Seta para esquerda! Vire a esquerda!"
            elif self._pista == ">":
                return "Seta para direita! Vire a direita!"
            elif self._pista == "^":
                return "Siga em Frente!"
            else:
                return "Informe uma orientação válida!"




    
        


