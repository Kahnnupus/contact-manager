contatos = []

def input_nome():
    while True:
        nome = input("\nDigite o nome do contato: ")
        if nome.strip() == "":
            print("\nO campo nome é obrigatório. \nPor favor, tente novamente!")
        elif not nome.replace(" ", "").isalpha():
            print("\nO nome deve conter apenas letras. \nPor favor, tente novamente!")
        else:
            return nome.upper()

def input_telefone(exibir):
    while True:
        telefone = input(f"{exibir}")
        if telefone.strip() == "":
            print("\n O campo telefone é obrigatório. \nPor favor, tente novamente!")
        elif len(telefone) != 11 and telefone.isdigit():
            print(
                "\nO campo telefone deve conter exatamente 11 dígitos números. \nPor favor, tente novamente!")
        elif not telefone.isdigit():
            print(
                "\nO campo telefone não pode conter letras. \nPor favor, tente novamente!")
        elif telefone and len(telefone) == 11 and telefone.isdigit():
            telefone = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:11]}"
            return telefone
        else:
            print("\nO campo telefone não foi preenchido corretamente. \nPor favor, tente novamente!")

def verificar_cadastro(telefone):
    possui_cadastro = False
    for contato in contatos:
        if telefone == contato["telefone"]:
            possui_cadastro = True
    return possui_cadastro

def adicionar():
    telefone = input_telefone("\nDigite o telefone do contato: ")
    verificar_cadastro_existente = verificar_cadastro(telefone)
    if verificar_cadastro_existente:
        return False
    nome = input_nome()
    cadastro = {"nome": nome, "telefone": telefone}
    contatos.append(cadastro)
    return True

def listar():
    if len(contatos) > 0:
        todos_contatos = "\nContatos:\n"
        for contato in contatos:
            todos_contatos += f" Nome: {contato["nome"]} \t| Telefone: {contato["telefone"]}\n"
    else:
        todos_contatos = "\nNão há contatos cadastrados!\n"
    return todos_contatos

def remover(telefone):
    excluido = False
    for contato in contatos:
        if contato["telefone"] == telefone:
            contatos.remove(contato)
            excluido = True
    return excluido