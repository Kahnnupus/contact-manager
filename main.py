from contacts.contact_manager import *


def menu():
    while True:
        opcao = input(
            "\n[Gerenciamento de Contatos]\n\nOpções:\n\n [1] Adicionar\n [2] Listar\n [3] Remover\n [4] Sair\n\nDigite a opção: ")
        if opcao.isdigit() and int(opcao) in range(1, 5):
            return int(opcao)

        else:
            print("\nOpção invalida, tente novamente!")
            input("\n\nPressione ENTER para retornar para o menu principal...")


def main():

    while True:
        opcao = menu()

        if opcao == 1:
            novo_contato = adicionar()
            if novo_contato:
                print("\nTelefone cadastrado com sucesso!")
            else:
                print("\nTelefone já possui cadastro!")
        elif opcao == 2:
            print(listar())
        elif opcao == 3:
            telefone = input_telefone("Digite o telefone que deseja remover: ")
            excluir = remover(telefone)
            if excluir:
                print(f"\nO telefone {telefone} foi excluído com sucesso!")
            else:
                print(f"\nO telefone {
                      telefone} não foi excluído, pois não existe na lista de contatos!")
        elif opcao == 4:
            print("\nSistema finalizado!\n")
            return False

        input("\n\nPressione ENTER para retornar para o menu principal...")


if __name__ == "__main__":
    main()
