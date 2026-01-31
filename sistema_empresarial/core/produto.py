from sistema_empresarial.utils.sequencias import gerar_sequencia


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
    
    def verificar_estoque(self, quantidade_solicitada):
        if self._quantidade < quantidade_solicitada:
            raise ValueError(f'Infelizmente nosso estoque de {self.nome} não tem a quantidade solicitada')
    
    def descontar_estoque(self, quantidade_descontar):
        if self._quantidade < quantidade_descontar:
            raise ValueError('Não há essa quantidade para descontar do estoque')
        
        self._quantidade -= quantidade_descontar
    
    def verificar_valor_pago(self, valor_pago, valor_total_compra):
        if not valor_pago or not isinstance(valor_pago, float):
            raise ValueError('Valor pago inválido.')
        
        if valor_pago < valor_total_compra:
            raise ValueError('Valor insuficiente.')

    def __str__(self):
        return f'{self._nome} | Código: {self._codigo} | Quantidade: {self.quantidade}'
