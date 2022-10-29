class Venda:
    def __init__(self, descricao, marca, peso, importado = False):
        self._descricao = descricao
        self._marca = marca 
        self._peso = peso
        self._importado = importado

    def Vender(self, items):
        self._items = items
        if self._promocao != None:
            


    def AdicionarPromocao(self, promocao):
        self._promocao = promocao