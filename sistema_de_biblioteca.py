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

usuarios = [
    {
        "email": "gabi@gmail.com",
        "senha": "0506"
    },
    {
        "email": "marcia@gmail.com",
        "senha": "1708"
    }
]


def limpar_terminal():
    os.system("cls")

def cadastrar_livros():
    while True:
        escolha = input("você deseja cadastrar um livro novo(s/n): ").lower()
        limpar_terminal()

        if escolha == "s" or escolha == "sim":
            titulo = input("Insira o titulo do livro: ")
            autor = input("Insira o nome do autor do livro: ")
            genero = input("Insira o gênero literario: ")
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
        limpar_terminal()

        if alternativa == "s" or alternativa == "sim":
            email = input("Insira seu email: ")
            senha = input("Insira sua senha: ")

            novo_usuario = {
                "email": email,
                "senha": senha
            }
            usuarios.append(novo_usuario)

        elif alternativa == "n" or alternativa == "não" or alternativa == "nao":
            limpar_terminal()
            break
        else:
            print("Insira s ou n")

def cadastrar_revista():
    while True:
            escolha = input("você deseja cadastrar uma revista nova(s/n): ").lower()
            limpar_terminal()
    
            if escolha == "s" or escolha == "sim":
                id_revista = int(input("Insira o ID da revista: "))
                titulo = input("Insira o titulo: ")
                edicao = input("Insira a edição: ")
                publicacao = input("Insira a data de publicação: ")
                editora = input("Insira a editora da revista: ")
                quantidade = int(input("Insira a quantidade: "))

                nova_revista = {
                    "id": id_revista,
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
            escolha = input("você deseja cadastrar um artigo científico novo(s/n): ").lower()
            limpar_terminal()
    
            if escolha == "s" or escolha == "sim":
                id_artigo = int(input("Insira o ID do artigo: "))
                titulo = input("Insira o titulo do artigo: ")
                autor = input("Insira o nome dos autores do artigo: ")
                palavras_chave = input("Insira as palavras chaves: ")
                publicacao = input("Insira a data de publicação: ")
                quantidade = int(input("Insira a quantidade de artigos: "))
                
                novo_artigo = {
                    "id": id_artigo,
                    "titulo": titulo,
                    "autor": autor,
                    "palavras_chave": palavras_chave,
                    "publicacao": publicacao,
                    "quantidade": quantidade
                }
    
                artigos.append(novo_artigo)
            elif escolha == "n" or escolha == "não" or escolha == "nao":
                limpar_terminal()
                break
            else:
                print("Insira s ou n")

def mostrar_usuarios(usuarios):
    limpar_terminal()

    for usuario in usuarios:
        print(
            f"Email: {usuario["email"]:<25}"
            f"Senha: {usuario["senha"]}"
        )

    print()
    input("Pressione Enter para voltar para o menu")
    limpar_terminal()

def emprestimo_devolucao():
    pass

def consultar_acervo(livros,revistas,artigos):
    limpar_terminal()
    print("LIVROS")
    for livro in livros:
        print(
            f"° Título: {livro['titulo']:<25}"
            f"Autor(a): {livro['autor']:<30}"
            f"Gênero Literario: {livro['genero']:<20}"
            f"Codigo ISBN: {livro['codigo']:<27}"
            f"Quantidade: {livro['quantidade']}"
    )

    print()

    print("REVISTAS")
    for revista in revistas:
        print(
            f"° ID: {revista['id']:<15}"
            f"Titulo: {revista['titulo']:<30}"
            f"Edição: {revista['edicao']:<20}"
            f"Publicação: {revista['publicacao']:<20}"
            f"Editora: {revista['editora']:<20}"
            f"Quantidade: {revista['quantidade']}"
        )

    print()

    print("ARTIGOS CIENTÍFICOS")
    for artigo in artigos:
        print(
            f"° ID: {artigo['id']:<12}"
            f"Titulo: {artigo['titulo']:<60}"
            f"Autores: {artigo['autor']:<45}"
            f"Palavras-chaves: {artigo['palavras_chave']:<37}"
            f"Publicação: {artigo['publicacao']:<10}"
            f"Quantidade: {artigo['quantidade']}"
        )

    print()
    input("Pressione Enter para voltar para o menu")
    limpar_terminal()


def relatorio():
    pass

while True:
    print("""
                -=-=-=-=MENU=-=-=-=-
        1 - Cadastrar livro
        2 - Cadastrar artigo científico
        3 - Cadastrar revista
        4 - Cadastrar usuario
        5 - Emprestimo ou devolução de um livro
        6 - Consultar acervo da biblioteca
        7 - Consultar usuarios cadastrados
        8 - Relatorio de empréstimo
        0 - Fechar sistema
    """)

    opcao = input("Insira uma opção: ")

    if opcao == "1":
        cadastrar_livros()
    elif opcao == "2":
        cadastrar_artigo()
    elif opcao == "3":
        cadastrar_revista()
    elif opcao == "4":
        cadastrar_usuarios(usuarios)
    elif opcao == "5":
        emprestimo_devolucao()
    elif opcao == "6":
        consultar_acervo(livros,revistas,artigos)
    elif opcao == "7":
        mostrar_usuarios(usuarios)
    elif opcao == "8":
        relatorio()
    elif opcao == "0":
        limpar_terminal()
        break
    else:
        print("Insira uma das opções")