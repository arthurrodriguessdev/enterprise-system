from datetime import datetime
from pathlib import Path

# Criando caminho para armazenamento dos arquivos
BASE_DIR = Path(__file__).resolve().parent.parent
ARQUIVOS_DIR = BASE_DIR / 'arquivos'
ARQUIVOS_DIR.mkdir(exist_ok=True)

DECORADOR_ARQUIVOS = '--------------------------------------------------------\n'


def gerar_comprovante_compra(produto, quantidade, valor_total_compra, data_hora_compra, vendido_por):
    try:
        # Montando arquivo de comprovante
        conteudo = [
            DECORADOR_ARQUIVOS,
            'COMPROVANTE DE COMPRA\n',
            DECORADOR_ARQUIVOS,
            f'Produto: {produto.nome}\n',
            f'Quantidade: {quantidade}\n',
            f'Vendedor: {vendido_por}\n',
            f'Valor total da compra: R${valor_total_compra:.2f}\n',
            f'\nData e hora: {datetime.strftime(data_hora_compra, "%d/%m/%Y - %H:%M:%S")}\n',
            DECORADOR_ARQUIVOS,
            'Agradecemos pela preferência!'
        ]
        
        caminho_arquivo = ARQUIVOS_DIR / 'comprovante_compra.txt'
        montar_txt(conteudo, caminho_arquivo)

    except Exception as error:
        raise SystemError(f'Erro ao gerar comprovante: {error}')

def gerar_relatorio(empresa):
    if empresa.total_vendas == 0:
        raise SystemError('Nenhuma venda foi realizada até o momento.')
    
    try:
        # Montando arquivo de relatório da empresa
        conteudo = [
            DECORADOR_ARQUIVOS,
            'RELATÓRIO DE VENDAS\n',
            DECORADOR_ARQUIVOS,
            f'Empresa: {empresa.nome}\n',
            f'Total de vendas: {empresa.total_vendas}\n',
            f'Valor total vendido: R${empresa.total_valor:.2f}\n',
            f'Média por vendas: R${empresa.valor_media_vendas:.2f}\n',
            DECORADOR_ARQUIVOS
        ]

        caminho_arquivo = ARQUIVOS_DIR / 'relatorio_vendas.txt'
        montar_txt(conteudo, caminho_arquivo)

    except Exception as error:
        raise SystemError(f'Erro ao gerar relatório: {error}')
    
    print('Relatório gerado com sucesso.')

def montar_txt(conteudo, caminho):
    try:
        with open(caminho, 'w', encoding='utf-8') as arquivo:
            arquivo.writelines(conteudo)

    except Exception as error:
        raise SystemError(f'Erro ao gerar arquivo:{error}')