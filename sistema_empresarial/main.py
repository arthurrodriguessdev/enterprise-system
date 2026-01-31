from core.empresa import Empresa
from services.compras import comprar_produto
from utils.gerar_arquivos import gerar_relatorio

EMPRESA = Empresa()

def main():
    while True:
        print('\n1 - Comprar produto')
        print('2 - Gerar relatório de vendas')
        print('3 - Sair\n')

        try:
            opcao = int(input('Informe a opção desejada: '))
        except Exception:
            print('Digite um valor válido.')
            continue

        match(opcao):
            case 1:
                comprar_produto(EMPRESA)

            case 2:
                gerar_relatorio(EMPRESA)
            
            case 3:
                print('\nEncerrando programa')
                return False
    
if __name__ == "__main__":
    main()