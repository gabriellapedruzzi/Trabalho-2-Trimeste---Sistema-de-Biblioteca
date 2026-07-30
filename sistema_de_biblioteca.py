livros = [
    ["Uma janela sombria", "Rachel Gillig", "978-65-85348-55-3", 1 ],
    ["Mistborn", "Brandon Sanderson", "978-65-81339-18-0", 1]
]

usuarios = {
    "gabi@gmail.com": "05062010",
    "ademar@gmail.com": "ademar123"
}

def cadastrar_livros():
    while True:
        escolha = input("você deseja cadastrar um livro novo(s/n): ")

        if escolha == "s":
            titulo = input("Insira o titulo do livro: ")
            autor = input("Insira o nome do autor do livro: ")
            codigo = input("Insira o codigo ISBN do livro: ")
            quantidade = input("Insira a quantidade de livros")
            
            novo_livro = [titulo, autor, codigo, quantidade]
            livros.append(novo_livro)
            print(novo_livro)
            print(livros)
        elif escolha == "n":
            break
        else:
            print("Insira s ou n")


def cadastrar_usuarios(usuarios):
    while True:
        alternativa = input("Você deseja cadastrar um novo usuario(s/n): ")
        if alternativa == "s":
            email = input("Insira seu email: ")
            senha = input("insira sea senha: ")

            usuarios[email] = senha
            print(usuarios)
        elif alternativa == "n":
            break
        else:
            print("insira s ou n")

def mostrar_usuarios(usuarios):
    for usuario in usuarios:
        email = usuario
        senha = usuarios[usuario]
        print(f"email: {email} \t senha: {senha}")

def emprestimo_devolução():
    pass

def consultar_livros(livros):
    for livro in range(len(livros)):
        print(f"Titulo: {livros[livro][0]} \t autor(a): {livros[livro][1]} \t Codigo ISBN: {livros[livro][2]} \t Quantidade: {livros[livro][3]}")

def relatorio():
    pass

while True:
    print("""
        1 - Cadastrar um livro
        2 - Cadastrar um Usuario
        3 - Emprestimo ou devolução de um livro
        4 - Consultar livros disponiveis
        5 - consultar usuarios cadastrados
        6 - Relatorio de emprstimo
        0 - Fechar sistema
    """)

    opcao = input("Insira uma opção: ")

    if opcao == "1":
        cadastrar_livros()
    elif opcao == "2":
        cadastrar_usuarios(usuarios)
    elif opcao == "3":
        emprestimo_devolução()
    elif opcao == "4":
        consultar_livros(livros)
    elif opcao == "5":
        mostrar_usuarios(usuarios)
    elif opcao == "6":
        relatorio()
    elif opcao == "0":
        break
    else:
        print("insira uma das opções")