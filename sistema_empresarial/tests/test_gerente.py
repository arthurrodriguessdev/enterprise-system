import unittest
from sistema_empresarial.core.gerente import Gerente


class TestGerente(unittest.TestCase):
    def setUp(self):
        self.gerentes = (
            Gerente('Arthur', 19, 1.80, 10500.0, 'Tecnologia', 1500.0),
            Gerente('Mariana', 32, 1.65, 8000.0, 'Financeiro', 1200.0),
            Gerente('Carlos', 40, 1.78, 6000.0, 'Operações', 900.0),
        )

    def test_calcular_salario(self):
        maior_dezmil = self.gerentes[0].calcular_salario()
        maior_setemil = self.gerentes[1].calcular_salario()
        maior_cincomil = self.gerentes[2].calcular_salario()

        self.assertEqual(maior_dezmil, 11625.0)
        self.assertEqual(maior_setemil, 9020.0)
        self.assertEqual(maior_cincomil, 6810.0)