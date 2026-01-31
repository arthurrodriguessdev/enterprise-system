from abc import ABC, abstractmethod
from sistema_empresarial.core.pessoa import Pessoa
from sistema_empresarial.utils.sequencias import gerar_sequencia


class Funcionario(Pessoa, ABC):
    def __init__(self, nome, idade, altura, salario_base, departamento):
        self._validar_salario_base(salario_base)

        self._matricula = gerar_sequencia()
        self._salario_base = salario_base
        self._departamento = departamento
        self._avaliacoes = []

        super().__init__(nome, idade, altura)

    @abstractmethod
    def calcular_salario(self):
        pass

    @property
    def matricula(self):
        return self._matricula
    
    @property
    def salario_base(self):
        return self._salario_base
    
    @salario_base.setter
    def salario_base(self, novo_salario_base):
        self._validar_salario_base(novo_salario_base)
        self._salario_base = novo_salario_base
    
    @property
    def departamento(self):
        return self._departamento
    
    @property
    def avaliacoes(self):
        return list(self._avaliacoes)
    
    def _validar_salario_base(self, salario):
        if not salario or not isinstance(salario, (float, int)):
            raise ValueError('Valor de salário inválido.')
        
        if salario <= 0:
            raise ValueError('O salário não pode ser negativo ou igual a zero.')
    
    def receber_avaliacoes(self, *args):
        if not args:
            raise ValueError('Avaliações inválidas.')
        
        for avaliacao in args:
            self._avaliacoes.append(avaliacao)

        return True
    
    def __str__(self):
        return f'{self.nome} ({self.departamento})'