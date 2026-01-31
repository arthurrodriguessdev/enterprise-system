import random
from core.produto import Produto
from core.vendas import Venda
from core.vendedor import Vendedor
from sistema_empresarial.utils.gerar_arquivos import gerar_comprovante_compra


PRODUTOS = (
    Produto('Televisão', 2500, 20),
    Produto('Monitor', 1840, 15),
    Produto('Mouse Gamer', 89.90, 10),
    Produto('Impressora', 559.90, 5),
    Produto('Notebook', 3450, 10)
)

VENDEDORES = (
    Vendedor("João Silva", 28, 1.75, 3200.00, "Vendas"), 
    Vendedor("Maria Oliveira", 35, 1.62, 4800.00, "Vendas"), 
    Vendedor("Carlos Souza", 22, 1.80, 2200.00, "Vendas")
)

def selecionar_vendedor(vendedores):
    return random.choice(vendedores)

def get_produto(codigo_produto):
    if not codigo_produto or not isinstance(codigo_produto, str):
        raise ValueError('Código inválido ou não informado.')
    
    try:
        for produto in PRODUTOS:
            if produto.codigo == codigo_produto:
                produto_escolhido = produto
                break

        return produto_escolhido
    
    except Exception:
        raise ValueError('O produto não foi encontrado.')

def comprar_produto(empresa):
    if PRODUTOS is None:
        raise ValueError('Erro ao adicionar produtos')
    
    print('\n')
    for produto in PRODUTOS:
        print(produto)
    
    try:
        codigo_produto_comprar = str(input('\nInsira o código do produto desejado: '))
        produto = get_produto(codigo_produto_comprar)
        quantidade_produto_comprar = int(input('Informe a quantidade desejada: '))
        vendedor = selecionar_vendedor(VENDEDORES)

        valor_total = produto.preco * quantidade_produto_comprar

        print('\nValor total da compra: R$', valor_total)

        valor_pago = float(input('Com quantos reais irá pagar? '))
        venda = Venda(produto, vendedor, quantidade_produto_comprar, valor_pago, valor_total)

    except Exception:
        raise ValueError('Código inválido e/ou produto não encontrado.')
    
    empresa.registrar_venda(valor_total, venda)
    vendedor.calcular_comissao(produto, quantidade_produto_comprar)
    gerar_comprovante_compra(produto, quantidade_produto_comprar, valor_total, venda.data_hora, vendedor)
    
    print('\nCompra realizada com sucesso. Já geramos o seu comprovante, acesse no diretório de arquivos!')
    return True