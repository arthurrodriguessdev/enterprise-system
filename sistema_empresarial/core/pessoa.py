class Pessoa():
    def __init__(self, nome, idade, altura):
        self._validar_nome(nome)
        self._validar_idade(idade)
        self._validar_altura(altura)

        self._nome = nome
        self._idade = idade
        self._altura = altura
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    
    @property
    def altura(self):
        return self._altura
    
    def _validar_nome(self, nome):
        if not nome or not isinstance(nome, str):
            raise ValueError('O nome informado está inválido.')
    
    def _validar_idade(self, idade):
        if not isinstance(idade, int):
            raise ValueError('O formato da idade está inválido.')
        
        if not idade or not 0 < idade <= 100:
            raise ValueError('A idade informada está inválida.')

    def _validar_altura(self, altura):
        if not isinstance(altura, (float, int)):
            raise ValueError('O formato da altura está inválido.')
        
        if not altura or altura <= 0:
            raise ValueError('A altura informada está inválida.')
    
    @nome.setter
    def nome(self, novo_nome):
        self._validar_nome(novo_nome)
        self._nome = novo_nome
    
    @idade.setter
    def idade(self, nova_idade):
        self._validar_idade(nova_idade)
        self._idade = nova_idade
    
    @altura.setter
    def altura(self, nova_altura):
        self._validar_altura(nova_altura)
        self._altura = nova_altura
    
    def __str__(self):
        return f'Nome: {self._nome} | Idade: {self._idade}'