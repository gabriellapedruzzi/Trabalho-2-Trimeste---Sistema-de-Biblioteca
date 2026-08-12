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
        "codigo": 1,
        "titulo": "National Geographic Brasil",
        "edicao": "284",
        "publicacao": "09/2024",
        "editora": "Azul",
        "quantidade": 1
    }
]

artigos = [
    {
        "codigo": 2, 
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

emprestimos = [
    {
        "titulo": "O Hobbit",
        "autor": "J.R.R. Tolkien",
        "genero": "fantasia",
        "codigo": "978-8595084742", 
        "quantidade": 0
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


def cadastrar_revista():
    while True:
            escolha = input("você deseja cadastrar uma revista nova(s/n): ").lower()
            limpar_terminal()
    
            if escolha == "s" or escolha == "sim":
                codigo_revista = int(input("Insira o codigo da revista: "))
                titulo = input("Insira o titulo: ")
                edicao = input("Insira a edição: ")
                publicacao = input("Insira a data de publicação: ")
                editora = input("Insira a editora da revista: ")
                quantidade = int(input("Insira a quantidade: "))

                nova_revista = {
                    "codigo": codigo_revista,
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
                codigo_artigo = int(input("Insira o codigo do artigo: "))
                titulo = input("Insira o titulo do artigo: ")
                autor = input("Insira o nome dos autores do artigo: ")
                palavras_chave = input("Insira as palavras chaves: ")
                publicacao = input("Insira a data de publicação: ")
                quantidade = int(input("Insira a quantidade de artigos: "))
                
                novo_artigo = {
                    "codigo": codigo_artigo,
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

   
    
def emprestimo():
    while True:
        alternativa = input("Você deseja pegar emprestado um item do acervo(s/n): ").lower()
        limpar_terminal()


        if alternativa == "s" or alternativa == "sim":
            print("""
                1 - Emprestimo de livros
                2 - Emprestimo de revistas
                3 - Emprestimo de artigos 

            """)

            opcao = input("Insira uma opção: ")
            
            if opcao == "1":
                limpar_terminal()
                emprestimo_livro(livros, emprestimos)
            elif opcao == "2":
                limpar_terminal()
                emprestimo_revista(revistas, emprestimos)
            elif opcao == "3":
                limpar_terminal()
                emprestimo_artigo(artigos, emprestimos)
            else:
                print("Insira uma das opções") 

        elif alternativa == "n" or alternativa == "não" or alternativa == "nao":
            limpar_terminal()
            break
        else:
            print("Insira s ou n")

    
def emprestimo_livro(livros, emprestimos):
        codigo = input("Insira o codigo do livro que você deseja pegar emprestado: ")

        for livro in livros:
            if codigo == livro['codigo']:
                if livro['quantidade'] > 0:
                    livro['quantidade'] -= 1
                    emprestimos.append(livro)
                    praso = "7 dias"
                    print(f"Você pegou emprestado {livro['titulo']} e tem {praso} para devolver")
                    return
                else:
                    print("Não ha exemplares desse livro")
                    return

        print("livro não encontrado")

def emprestimo_revista(revistas, emprestimos):
    codigo = int(input("Insira o codigo do livro que você deseja pegar emprestado: "))
    
    for revista in revistas:
        if codigo == revista['codigo']:
            if revista['quantidade'] > 0:
                revista['quantidade'] -= 1
                emprestimos.append(revista)
                praso = "7 dias"
                print(f"Você pegou emprestado {revista['titulo']} e tem {praso} para devolver")
                return
            else:
                print("Não ha exemplares desse livro")
                return

    print("livro não encontrado")

def emprestimo_artigo(artigos, emprestimos):
    codigo = int(input("Insira o codigo do livro que você deseja pegar emprestado: "))
        
    for artigo in artigos:
        if codigo == artigo['codigo']:
            if artigo['quantidade'] > 0:
                artigo['quantidade'] -= 1
                emprestimos.append(artigo)
                praso = "7 dias"
                print(f"Você pegou emprestado {artigo['titulo']} e tem {praso} para devolver")
                return
            else:
                print("Não ha exemplares desse livro")
                return

    print("livro não encontrado")

def devolucao():
    while True:
        alternativa = input("Você deseja devolver um item do acervo(s/n): ").lower()
        limpar_terminal()


        if alternativa == "s" or alternativa == "sim":
            codigo = int(input("Insira o codigo do livro que você deseja devolver:"))
            
            for item in emprestimos:
                if codigo == item['codigo']:
                    print(f"Você devolveu {item['titulo']}")
                    item['quantidade'] += 1
                    emprestimos.remove(item)

        elif alternativa == "n" or alternativa == "não" or alternativa == "nao":
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
            f"° ID: {revista['codigo']:<15}"
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
            f"° ID: {artigo['codigo']:<12}"
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
        5 - Emprestimo 
        6 - devolução
        7 - Consultar acervo da biblioteca
        8 - Consultar usuarios cadastrados
        9 - Relatorio de empréstimo
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
        emprestimo()
    elif opcao == "6":
        devolucao()
    elif opcao == "7":
        consultar_acervo(livros,revistas,artigos)
    elif opcao == "8":
        mostrar_usuarios(usuarios)
    elif opcao == "9":
        relatorio()
    elif opcao == "0":
        limpar_terminal()
        break
    else:
        print("Insira uma das opções")
