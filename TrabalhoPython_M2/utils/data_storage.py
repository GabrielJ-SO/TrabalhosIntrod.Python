
ARQUIVO_CLIENTES = "saves/clientes.txt"
ARQUIVO_LIVROS = "saves/livros.txt"


def salvar_clientes(lista_clientes: list):

    with open(ARQUIVO_CLIENTES, "w", encoding="utf-8") as f:
        for cliente in lista_clientes:
            f.write(cliente.save())


def salvar_livros(lista_livros: list):
    
    with open(ARQUIVO_LIVROS, "w", encoding="utf-8") as f:
        for livro in lista_livros:
            f.write(livro.save())