import unittest
from sistema_empresarial.core.vendedor import Vendedor
from sistema_empresarial.core.produto import Produto


class TestVendedor(unittest.TestCase):
    def setUp(self):
        self.produto = (Produto('Notebook', 2500, 10), Produto('Mesa de PC', 1200, 10))
        self.vendedor = Vendedor('Arthur', 19, 1.82, 2000, 'Vendas')
        
    def test_calculo_comissao(self):
        self.assertEqual(self.vendedor.calcular_comissao(self.produto[0], 1), 125)
    
    def test_incremento_comissao(self):
        self.vendedor.calcular_comissao(self.produto[0], 2)
        self.vendedor.calcular_comissao(self.produto[1], 3)
        self.assertEqual(self.vendedor.comissao, 430)
    
    def test_calcular_salario_total(self):
        self.vendedor.calcular_comissao(self.produto[0], 2) # Comissão R$250
        self.assertEqual(self.vendedor.calcular_salario(), 2250)