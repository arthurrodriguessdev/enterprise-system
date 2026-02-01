
#  Enterprise System — Sistema de Compras de produtos

## Descrição do Projeto

**Enterprise System** é um sistema simples desenvolvido em Python puro, com foco em Programação Orientada a Objetos (POO). O projeto simula um sistema real de vendas de produtos, incluindo cadastro de funcionários, controle de estoque, processamento de vendas, geração de relatórios e regras de negócio bem definidas. O objetivo principal do projeto é revisar conceitos de POO já aprendidos, organização de código e testes unitários.

## Funcionalidades Principais do Sistema
- Cadastro e gerenciamento de produtos
- Controle de estoque
- Registro de vendas
- Associação de vendas a vendedores
- Cálculo de comissões
- Cálculo de salário de gerentes com regras de desconto
- Geração de comprovante de compra (.txt)
- Geração de relatório de vendas (.txt)
- Validações de regras de negócio
- Testes unitários para garantir integridade do sistema

## Tecnologias Utilizadas
### Back-End
- Python

### Interface
- Console (Terminal)

### Testes
- unittest

### Versionamento
- Git / GitHub

## Arquitetura do Sistema
- Programação Orientada a Objetos (POO)
- Encapsulamento
- Herança e polimorfismo
- Separação de responsabilidades por módulos
- Código organizado para fácil manutenção
- Testes unitários utilizando unittest

## Instruções de Uso
1. Clone o repositório:
```bash
https://github.com/arthurrodriguessdev/enterprise-system.git

2. Acesse o diretório do projeto:
cd enterprise-system

3. Execute o sistema:
python3 -m sistema_empresarial.main
```
Após a execução, um menu será exibido no terminal permitindo realizar compras e gerar relatórios.

## Executando Testes
- Para rodar todos os testes unitários do projeto:
```bash
python3 -m unittest discover
```

## Geração de Arquivos
O sistema gera automaticamente os seguintes arquivos:
- **comprovante_compra.txt**: comprovante da compra realizada
- **relatorio_vendas.txt**: relatório de todas as vendas realizadas

Os arquivos são salvos localmente no diretório "arquivos" dentro do projeto.

## Licença
- Uso comercial não permitido
- Código disponível apenas para visualização

Todos os direitos reservados ao autor.
---

## Autor
**Arthur Rodrigues**
Desenvolvedor Full Stack

LinkeIn: www.linkedin.com/in/arthur-rodriguesx