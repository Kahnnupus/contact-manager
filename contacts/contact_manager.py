contatos = []

def adicionar():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    cadastro = {"nome": nome, "telefone": telefone}
    contatos.append(cadastro)
    return True

def listar():
    if len(contatos) > 0:
         for contato in contatos:
             print("Nome:", contato["nome"], "\t| Telefone:", contato["telefone"])
    else:
        print('Não existe contatos cadastrados!')

def remover(telefone):
    if len(contatos) > 0:
         for contato in contatos:
             if contato["telefone"] == telefone:
                 contatos.remove(contato)
                 print('Removido com sucesso!')             
    else:
        print('Não existe contatos cadastrados!')