class Item:
    def __init__(self, produto, preco, data_validade):
        self._produto = produto
        self._preco = preco
        self._data_validade = data_validade

def ColocarEmPromoção(self, desconto):
    self._precoComDesconto= self._preco * (desconto/100)
    