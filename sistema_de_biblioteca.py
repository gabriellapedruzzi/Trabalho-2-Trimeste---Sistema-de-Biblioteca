livros = [
    {
        "titulo": "Uma janela sombria",
        "autor": "Rachel Gillig",
        "codigo": "978-65-85348-55-3",
        "quantidade": 3
    },
    {
        "titulo": "Mistborn",
        "autor": "Brandon Sanderson",
        "codigo": "978-65-81339-18-0",
        "quantidade": 5
    }
]

usuarios = {
    "gabi@gmail.com": "05062010",
    "ademar@gmail.com": "ademar123"
}

def cadastrar_livros():
    while True:
        escolha = input("você deseja cadastrar um livro novo(s/n): ").lower()

        if escolha == "s" or escolha == "sim":
            titulo = input("Insira o titulo do livro: ")
            autor = input("Insira o nome do autor do livro: ")
            codigo = input("Insira o codigo ISBN do livro: ")
            quantidade = int(input("Insira a quantidade de livros"))
            
            novo_livro = {
            "titulo": titulo,
            "autor": autor,
            "codigo": codigo,
            "quantidade": quantidade
            }
            livros.append(novo_livro)
            print(novo_livro)
            print(livros)
        elif escolha == "n" or escolha == "não" or escolha == "nao":
            break
        else:
            print("Insira s ou n")


def cadastrar_usuarios(usuarios):
    while True:
        alternativa = input("Você deseja cadastrar um novo usuario(s/n): ").lower()
        if alternativa == "s" or alternativa == "sim":
            email = input("Insira seu email: ")
            senha = input("insira sua senha: ")

            usuarios[email] = senha
            print(usuarios)
        elif alternativa == "n" or alternativa == "não" or alternativa == "nao":
            break
        else:
            print("insira s ou n")

def mostrar_usuarios(usuarios):
    for usuario in usuarios:
        email = usuario
        senha = usuarios[usuario]
        print(f"email: {email} \t senha: {senha}")

def emprestimo_devolucao():
    pass

def consultar_livros(livros):
    for livro in livros:
        print(
    f"Título: {livro['titulo']:<25}"
    f"Autor(a): {livro['autor']:<25}"
    f"Codigo ISBN: {livro['codigo']:<25}"
    f"Quantidade: {livro['quantidade']}"
)
        
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
        emprestimo_devolucao()
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