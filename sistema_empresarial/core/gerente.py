from sistema_empresarial.core.funcionario import Funcionario


class Gerente(Funcionario):
    def __init__(self, nome, idade, altura, salario_base, departamento, bonus_fixo):
        self._validar_bonus_fixo(bonus_fixo, salario_base)
        self._bonus_fixo = bonus_fixo

        super().__init__(nome, idade, altura, salario_base, departamento)
    
    # Calcula o salário total baseado na procentagem sobre o bônus
    def calcular_salario(self):
        salario = self._salario_base

        if salario > 10000:
            return self.calcular_salario_com_desconto(25)
        
        elif salario > 7000:
            return self.calcular_salario_com_desconto(15)
        
        elif salario > 5000:
            return self.calcular_salario_com_desconto(10)
        
        return self._salario_base + self._bonus_fixo
    
    def calcular_salario_com_desconto(self, procentagem_desconto):
        desconto = (self._bonus_fixo * procentagem_desconto) / 100
        return (self._salario_base + self._bonus_fixo) - desconto
    
    # Exibe o salário total do gerente (salário base + bônus)
    @property
    def salario_total(self):
        return self.calcular_salario()
    
    @property
    def bonus_fixo(self):
        return self._bonus_fixo
    
    def _validar_bonus_fixo(self, bonus_fixo, salario_base):
        if bonus_fixo > salario_base:
            raise ValueError('O bônus não pode ser maior que o salário.')