
import os
from controller.ClientesCadastrados import ClientesCadastrados
from controller.EstoqueLivros import EstoqueLivros
from model.Cliente import Cliente
from model.Livro import Livro

lista_clientes = ClientesCadastrados()
lista_livros = EstoqueLivros()

livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 10)

def menu() -> str:
    """Exibe o menu de opções do sistema de biblioteca
    Returns:
        str: Menu de opções formatado como string
    """

    return f"=============Menu de Opções=============\n" \
            f"1. Cadastrar cliente\n" \
            f"2. Cadastrar livro\n" \
            f"3. Consultar livros\n" \
            f"4. Realizar empréstimo\n" \
            f"5. Realizar devolução\n" \
            f"6. Exibir empréstimos de um cliente\n" \
            f"7. Clientes cadastrados\n" \
            f"0. Sair\n" \
            f"========================================\n" \
#Opção 1
def cadastrar_cliente():
    """Função para cadastrar um novo cliente
    Adiciona o cliente à lista de clientes cadastrados
    """

    nome = input("Nome: ")
    cpf = input("CPF: ")
    
    novo_cliente = Cliente(nome, cpf)
    lista_clientes.adicionar_cliente(novo_cliente)

    print(f'Cliente "{nome}" cadastrado com sucesso.')

#Opção 2
def cadastrar_livro():
    """Função para cadastrar um novo livro
    Adiciona o livro ao estoque de livros

    """

    titulo = input("Título: ")
    autor = input("Autor: ")
    ano_publicacao = int(input("Ano de Publicação: "))
    quantidade = int(input("Quantidade em Estoque: "))

    novo_livro = Livro(titulo, autor, ano_publicacao, quantidade)
    lista_livros.adicionar_livro_aoestoque(novo_livro)

    print(f'Livro "{titulo}" do autor "{autor}" cadastrado com sucesso.')

#Opção 3
def cosulta_livros_cadastrados():

    print (f"1. Consultar livro por titulo.\n"
           f"2. Buscar livros de um autor. \n" \
           f"3. Listar livros cadastrados.\n" )
    
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        titulo = input("Titulo do livro: ")
        lista_livros.buscar_livro_titulo(titulo)

    elif escolha == "2":
        autor = input("Nome do autor: ")
        lista_livros.buscar_livros_autor(autor)

    elif escolha == "3":
        lista_livros.listar_livros_emestoque()

    else:
        print("Opção invalida.")

#Opção 4
def realizar_emprestimo():
    """"""
    
#Opção 8
def consulta_clientes_cadastrados():
    """Função para exibir os clientes cadastrados no sistema"""
    
    print (f"1. Consultar cliente por CPF.\n" \
           f"2. Listar clientes cadastrados.\n" )
    
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        cpf = input("CPF do cliente: ")
        lista_clientes.buscar_cliente_cpf(cpf)
    elif escolha == "2":
        lista_clientes.listar_clientes()
    else:
        print("Opção invalida.")

    
    

