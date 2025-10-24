
import os
from controller.ClientesCadastrados import ClientesCadastrados
from model.Cliente import Cliente
from model.Livro import Livro

lista_clientes = ClientesCadastrados()

livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 10)

def menu() -> str:
    """Exibe o menu de opções do sistema de biblioteca
    Returns:
        str: Menu de opções formatado como string
    """

    return f"=============Menu de Opções=============\n" \
            f"1. Cadastrar cliente\n" \
            f"2. Cadastrar livro\n" \
            f"3. Listar livros em estoque\n" \
            f"4. Realizar empréstimo\n" \
            f"5. Realizar devolução\n" \
            f"6. Exibir empréstimos de um cliente\n" \
            f"7. Consultar livro\n" \
            f"8. Clientes cadastrados\n" \
            f"9. Sair\n" \
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

    print(f'Livro "{titulo}" do autor "{autor}" cadastrado com sucesso.')
    
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

    
    

