from utils import gerar_sequencia


class Produto:
    def __init__(self, nome, preco, quantidade):
        self._validar_preco(preco)
        self._validar_quantidade(quantidade)

        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade
        self._codigo = gerar_sequencia()
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return self._preco
    
    @property
    def quantidade(self):
        return self._quantidade
    
    @property
    def codigo(self):
        return self._codigo
    
    def _validar_preco(self, preco):
        if not preco or not isinstance(preco, (int, float)) or preco <= 0:
            raise ValueError('Preço inválido.')
    
    def _validar_quantidade(self, quantidade):
        if not quantidade or quantidade <= 0 or not isinstance(quantidade, int):
            raise ValueError('Quantidade inválida.')
    
    def verificar_estoque(Produto, quantidade_solicitada):
        if Produto._quantidade < quantidade_solicitada:
            raise ValueError(f'Infelizmente nosso estoque de {Produto.nome} não tenha a quantidade solicitada')
    
    def descontar_estoque(Produto, quantidade_descontar):
        if Produto.quantidade < quantidade_descontar:
            raise ValueError('Não há essa quantidade para descontar do estoque')
        
        Produto.quantidade -= quantidade_descontar

    def __str__(self):
        return f'{self._nome} | Código: {self._codigo} | Quantidade: {self.quantidade}'