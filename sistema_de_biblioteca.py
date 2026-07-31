import os

livros = [
    {
        "titulo": "Uma janela sombria",
        "autor": "Rachel Gillig",
        "genero": "fantasia",
        "codigo": "978-65-85348-55-3",
        "quantidade": 3
    },
    {
        "titulo": "Mistborn",
        "autor": "Brandon Sanderson",
        "genero": "fantasia",
        "codigo": "978-65-81339-18-0",
        "quantidade": 5
    }
]

revistas = [
    {
        "id": 8987878,
        "titulo": "National Geographic Brasil",
        "edicao": "284",
        "publicacao": "09/2024",
        "editora": "Azul",
        "quantidade": 1
    }
]

artigos = [
    {
        "id": 6586586, 
        "titulo": "A Importância da Libras para Inclusão Escolar do Surdo",
        "autor": "Marilene Domanovski, Adriane Meyer Vassão",
        "palavras_chave": "Libras, Inclusão Escolar, Surdez",
        "publicacao": 2016,
        "quantidade": 3
    }
]

usuarios = {
    "gabi@gmail.com": "05062010",
    "ademar@gmail.com": "ademar123"
}


def limpar_terminal():
    os.system("cls")

def cadastrar_livros():
    while True:
        escolha = input("você deseja cadastrar um livro novo(s/n): ").lower()

        if escolha == "s" or escolha == "sim":
            titulo = input("Insira o titulo do livro: ")
            autor = input("Insira o nome do autor do livro: ")
            genero = input("Insira o genero literario: ")
            codigo = input("Insira o codigo ISBN do livro: ")
            quantidade = int(input("Insira a quantidade de livros: "))
            
            novo_livro = {
                "titulo": titulo,
                "autor": autor,
                "genero": genero,
                "codigo": codigo,
                "quantidade": quantidade
            }

            livros.append(novo_livro)
        elif escolha == "n" or escolha == "não" or escolha == "nao":
            limpar_terminal()
            break
        else:
            print("Insira s ou n")


def cadastrar_usuarios(usuarios):
    while True:
        alternativa = input("Você deseja cadastrar um novo usuario(s/n): ").lower()
        if alternativa == "s" or alternativa == "sim":
            email = input("Insira seu email: ")
            senha = input("Insira sua senha: ")

            usuarios[email] = senha
        elif alternativa == "n" or alternativa == "não" or alternativa == "nao":
            limpar_terminal()
            break
        else:
            print("Insira s ou n")

def cadastrar_revista():
    while True:
            escolha = input("você deseja cadastrar uma revista nova(s/n): ").lower()
    
            if escolha == "s" or escolha == "sim":
                id = int(input("Insira o ID: "))
                titulo = input("Insira o titulo: ")
                edicao = input("Insira a edição: ")
                publicacao = input("Insira a data de publicação: ")
                editora = input("Insira a editora da revista: ")
                quantidade = int(input("Insira a quantidade: "))

                nova_revista = {
                    "id": id,
                    "titulo": titulo,
                    "edicao": edicao,
                    "publicacao": publicacao,
                    "editora": editora,
                    "quantidade": quantidade
                }

                revistas.append(nova_revista)
        
            elif escolha == "n" or escolha == "não" or escolha == "nao":
                limpar_terminal()
                break
            else:
                print("Insira s ou n")

def cadastrar_artigo():
    while True:
            escolha = input("você deseja cadastrar um artigo cíentifico novo(s/n): ").lower()
    
            if escolha == "s" or escolha == "sim":
                titulo = input("Insira o titulo do artigo: ")
                autor = input("Insira o nome do autores do artigo: ")
                palavras_chave = input("Insira as palavras chaves: ")
                publicacao = input("Insira a data de publicação: ")
                quantidade = int(input("Insira a quantidade de artigos: "))
                
                novo_artigo = {
                    "titulo": titulo,
                    "autor": autor,
                    "palavras_chave": palavras_chave,
                    "publicacao": publicacao,
                    "quantidade": quantidade
                }
    
                artigos.append(novo_artigo)
                print(artigos)
            elif escolha == "n" or escolha == "não" or escolha == "nao":
                limpar_terminal()
                break
            else:
                print("Insira s ou n")

def mostrar_usuarios(usuarios):
    limpar_terminal()
    for usuario in usuarios:
        email = usuario
        senha = usuarios[usuario]
        print(f"email: {email:<25} senha: {senha}")

def emprestimo_devolucao():
    pass

def consultar_acervo(livros,revistas,artigos):
    limpar_terminal()
    print("LIVROS")
    for livro in livros:
        print(
            f"° Título: {livro['titulo']:<25}"
            f"Autor(a): {livro['autor']:<30}"
            f"Genero Literario: {livro['genero']:<20}"
            f"Codigo ISBN: {livro['codigo']:<27}"
            f"Quantidade: {livro['quantidade']}"
    )

    print()

    print("REVISTAS")
    for revista in revistas:
        print(
            f"° ID: {revista['id']:<15}"
            f"Titulo: {revista['titulo']:<20}"
            f"Edição: {revista['edicao']:<20}"
            f"Publicação: {revista['publicacao']:<20}"
            f"Editora: {revista['editora']:<20}"
            f"Quantidade: {revista['quantidade']}"
        )

    print()

    print("ARTIGOS CÍENTIFICOS")
    for artigo in artigos:
        print(
            f"° ID: {artigo['id']:<12}"
            f"Titulo: {artigo['titulo']:<60}"
            f"Autoes: {artigo['autor']:<45}"
            f"Palavras-chaves: {artigo['palavras_chave']:<37}"
            f"Publicação: {artigo['publicacao']:<10}"
            f"Quantidade: {artigo['quantidade']}"
        )
        
def relatorio():
    pass

while True:
    print("""
                -=-=-=-=MENU=-=-=-=-
        1 - Cadastrar um livro
        2 - Cadastrar um Usuario
        3 - cadastrar revista
        4 - cadastrar artigo cíentifico
        5 - Emprestimo ou devolução de um livro
        6 - Consultar acervo da biblioteca
        7 - consultar usuarios cadastrados
        8 - Relatorio de emprstimo
        0 - Fechar sistema
    """)

    opcao = input("Insira uma opção: ")

    if opcao == "1":
        cadastrar_livros()
    elif opcao == "2":
        cadastrar_usuarios(usuarios)
    elif opcao == "3":
        cadastrar_revista()
    elif opcao == "4":
        cadastrar_artigo()
    elif opcao == "5":
        emprestimo_devolucao()
    elif opcao == "6":
        consultar_acervo(livros,revistas,artigos)
    elif opcao == "7":
        mostrar_usuarios(usuarios)
    elif opcao == "8":
        relatorio()
    elif opcao == "0":
        break
    else:
        print("Insira uma das opções")
