from datetime import datetime
from produto import Produto

class Venda:
    def __init__(self, Produto, Vendedor, quantidade_produto, valor_pago, valor_total):
        self.verificar_venda(Produto, quantidade_produto, valor_pago, valor_total)

        self.produto_vendido = Produto
        self.vendido_por = Vendedor
        self.quantidade_vendas = 0
        self.total_vendido = 0
        self.quantidade_produto = quantidade_produto
        self.data_hora = datetime.now()
        self.valor_pago = valor_pago
        self.valor_total = valor_total
        self.registrar_venda()
    
    def verificar_venda(self, produto, quantidade_produto, valor_pago, valor_total):
        produto.verificar_estoque(quantidade_produto)
        produto.descontar_estoque(quantidade_produto)
        produto.verificar_valor_pago(valor_pago, valor_total)

    def registrar_venda(self):
        self.quantidade_vendas += 1
        self.total_vendido += self.produto_vendido.preco
        return True
    
    def __str__(self):
        return f'Produto vendido: {self.produto_vendido} ({self.produto_vendido.preco})'


    

