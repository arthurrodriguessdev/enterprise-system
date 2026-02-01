import unittest
from sistema_empresarial.core.empresa import Empresa
from sistema_empresarial.core.vendas import Venda
from sistema_empresarial.core.produto import Produto
from sistema_empresarial.core.vendedor import Vendedor


class TestEmpresa(unittest.TestCase):
    def setUp(self):
        self.empresa = Empresa()
        self.produto = Produto('Notebook', 2500, 10)
        self.vendedor = Vendedor('Arthur', 19, 1.82, 2000, 'Vendas')
        self.venda = Venda(self.produto, self.vendedor, 2, 6000.0, 5000.0)

        self.empresa.registrar_venda(5000.0, 6000.0, self.produto, 2, self.venda)
        self.empresa.registrar_venda(7500.0, 9000.0, self.produto, 3, self.venda)
    
    def test_registrar_venda(self):
        self.assertEqual(self.empresa.total_valor, 12500.0) and self.assertEqual(self.empresa.total_vendas, 5)
    
    def test_valor_media_vendas(self):
        valor_media = self.empresa.valor_media_vendas
        self.assertEqual(valor_media, 6250.0)
    
    # Testando exception de divisão por zero
    def test_valor_media_vendas_sem_vendas(self):
        self.empresa.total_vendas = 0

        with self.assertRaises(ZeroDivisionError) as erro_divisao_zero:
            self.empresa.valor_media_vendas
            
        self.assertEqual(erro_divisao_zero.exception.args[0], 'Vendas ainda não foram feitas.')

