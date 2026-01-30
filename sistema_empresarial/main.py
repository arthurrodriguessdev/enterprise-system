from vendas import Venda
from produto import Produto
from services import comprar_produto


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
                comprar_produto()
                break

            case 2:
                ...
                break
            
            case 3:
                print('\nEncerrando programa')
                return False
    
if __name__ == "__main__":
    main()