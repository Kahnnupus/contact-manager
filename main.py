def menu():
    while True:
        opcao = input("\n[Gerenciamento de Contatos]\n\nOpções:\n\n [1] Adicionar\n [2] Listar\n [3] Remover\n [4] Sair\n\nDigite a opção: ")
        if opcao.isdigit() and int(opcao) in range(1,5):
            print("opcao", opcao)
            return int(opcao)
        
        else:
            print("\nOpção invalida, tente novamente!")
            input("\n\nPressione ENTER para retornar para o menu principal...")

def main():

    while True:
        opcao = menu()

        if opcao == 1:
            print("\n1 - adicionar")
            
        elif opcao == 2:
            print("\n2 - listar")
            
        elif opcao == 3:
            print("\n3 - remover")
            
        elif opcao == 4:
            print("\nSistema finalizado!")
            return False
        input("\n\nPressione ENTER para retornar para o menu principal...")


main()