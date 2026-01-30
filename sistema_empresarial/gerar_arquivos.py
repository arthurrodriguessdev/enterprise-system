from datetime import datetime

def gerar_comprovante_compra(produto, quantidade, valor_total_compra, data_hora_compra):
    try:
        # Montando arquivo de comprovante
        decorador_comprovante = '--------------------------------------------------------\n'
        conteudo = [
            decorador_comprovante,
            'COMPROVANTE DE COMPRA\n',
            decorador_comprovante,
            f'Produto: {produto.nome}\n',
            f'Quantidade: {quantidade}\n',
            f'Valor total da compra: R${valor_total_compra}\n',
            f'\nData e hora: {datetime.strftime(data_hora_compra, '%d/%m/%Y - %H:%M:%S')}\n',
            decorador_comprovante,
            'Agradecemos pela preferência!'
        ]

        with open('comprovante.txt', 'w') as arquivo_comprovante:
            arquivo_comprovante.writelines(conteudo)
            arquivo_comprovante.close()

    except Exception as error:
        raise SystemError('Erro ao gerar comprovante: {}', format(error))