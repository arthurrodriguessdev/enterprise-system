class Empresa:
    def __init__(self):
        self.total_vendas = 0
        self.total_valor = 0
        self.nome = 'Tecnologias Python'
    
    def registrar_venda(self, valor_venda):
        self.total_vendas += 1
        self.total_valor += valor_venda
    
    @property
    def valor_media_vendas(self):
        try:
            return self.total_valor / self.total_vendas
        
        except:
            raise ZeroDivisionError('Vendas ainda não foram feitas.')