def cadastrar_livros():
    print(111)
def cadastrar_usuarios():
    pass
def emprestimo_devolução():
    pass
def consultar_livros():
    pass
def relatorio():
    pass

while True:
    print("""
        1 - Cadastrar um livro
        2 - Cadastrar um Usuario
        3 - Emprestimo ou devolução de um livro
        4 - Consultar livros disponiveis
        5 - Relatorio de emprstimo
        0 - Fechar sistema
    """)

    opcao = input("Insira uma opção: ")

    if opcao == "1":
        cadastrar_livros()
    elif opcao == "2":
        cadastrar_usuarios()
    elif opcao == "3":
        emprestimo_devolução()
    elif opcao == "4":
        consultar_livros()
    elif opcao == "5":
        relatorio()
    elif opcao == "0":
        break
    else:
        print("insira uma das opções")