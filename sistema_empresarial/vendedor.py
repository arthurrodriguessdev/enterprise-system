from funcionario import Funcionario


class Vendedor(Funcionario):
    def __init__(self, nome, idade, altura, salario_base, departamento):
        self._comissao = 0

        return super().__init__(nome, idade, altura, salario_base, departamento)
    
    @property
    def comissao(self):
        return self._comissao
    
    def calcular_comissao(self, Produto):
        self._comissao += (Produto.preco * 20) / 100

    def calcular_salario(self):
        return self._salario_base + self._comissao
    
    def __str__(self):
        return super().__str__()