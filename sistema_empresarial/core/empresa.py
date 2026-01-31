class Empresa:
    def __init__(self):
        self.total_vendas = 0
        self.total_valor = 0
        self.nome = 'Tecnologias Python'
    
    def registrar_venda(self, valor_total, valor_pago, produto, quantidade_solicitada, venda):
        venda.verificar_venda(produto, quantidade_solicitada, valor_pago, valor_total)
        self.total_vendas += 1
        self.total_valor += valor_total
    
    @property
    def valor_media_vendas(self):
        try:
            return self.total_valor / self.total_vendas
        
        except:
            raise ZeroDivisionError('Vendas ainda não foram feitas.')