
import os
from controller.ClientesCadastrados import ClientesCadastrados
from controller.EstoqueLivros import EstoqueLivros
from model.Cliente import Cliente
from model.Livro import Livro
from utils import data_storage

lista_clientes = ClientesCadastrados()
lista_livros = EstoqueLivros()

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


#Opção 3
def cosulta_livros_cadastrados():
    """Função para consultar livros cadastrados no sistema"""

    print (f"1. Consultar livro por titulo.\n"
           f"2. Buscar livros de um autor. \n" \
           f"3. Listar livros cadastrados.\n" )
    
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        titulo = input("Titulo do livro: ")

        try:   
            print(lista_livros.buscar_livro_titulo(titulo)[0])
        except IndexError:
            print("Livro não encontrado.")

    elif escolha == "2":
        autor = input("Nome do autor: ")
        lista_livros.buscar_livros_autor(autor)

    elif escolha == "3":
        lista_livros.listar_livros_emestoque()

    else:
        print("Opção invalida.")


#Opção 4
def realizar_emprestimo():
    """Função para realizar o empréstimo de um livro a um cliente"""
    
    cpf = input("Digite o CPF do cliente para qual o emprestimo sera realizado: ")

    if not lista_clientes.buscar_cliente_cpf(cpf):
        print(f"Clinte não encontrado no sistema.")
        return
    
    try:
        titulo = input("Digite o titulo do livro do qual deseja emprestar: ")
        livro = lista_livros.buscar_livro_titulo(titulo)[0]    
    except IndexError:    
        print("O livro não existe, ou ainda não foi cadastrado.")
        return

    cliente = lista_clientes.buscar_cliente_cpf(cpf)
    if livro.quantidade_disponivel > 0:
        livro.remover_quantidade(1)
    else:
        print("Quantidade insuficiente para emprestimos.")
        return

    cliente.adicionar_emprestimo(livro.titulo)
    data_storage.salvar_clientes(lista_clientes.clientes)
    data_storage.salvar_livros(lista_livros.livros)
    print("Emprestimo realizado com sucesso.")
    

#Opção 5
def realizar_devolucao():
    """Função para realizar a devolução de um livro emprestado para um cliente"""

    cpf = input("Digite o CPF do cliente para qual a devolução sera realizado: ")

    if not lista_clientes.buscar_cliente_cpf(cpf):
        print(f"Clinte não encontrado no sistema.")
        return
    try:
        titulo = input("Digite o titulo do livro do qual deseja devolver: ")
        livro = lista_livros.buscar_livro_titulo(titulo)[0]
    except IndexError:
        print("O livro não existe, ou ainda não foi cadastrado.")
        return

    cliente = lista_clientes.buscar_cliente_cpf(cpf)

    for title in cliente.lista_emprestimos:
        if title.strip().lower() == titulo.strip().lower():
            cliente.remover_emprestimo(title)
            print("Devolucao feita com sucesso.")
            livro.adicionar_quantidade(1)
            data_storage.salvar_clientes(lista_clientes.clientes)
            data_storage.salvar_livros(lista_livros.livros)
            return
        else:
            print("Livro nao encontrado")
  

#Opção 6
def listar_emprestimos_cliente():
    """Função para listar os empréstimos de um cliente específico"""

    cpf = input("Digite o CPF do cliente para acessar sua lista de emprestimos: ")
    cliente = lista_clientes.buscar_cliente_cpf(cpf)

    if cliente == None:
        print(f"Cliente com CPF {cpf} não encontrado.")
        return
    elif not cliente.lista_emprestimos:
        print(f"O cliente {cliente.nome} não possui empréstimos.")
        return
    
    print(f"Livros emprestado para o cliente {cliente.nome}:")
    for titulo in cliente.lista_emprestimos:
        print(lista_livros.buscar_livro_titulo(titulo)[0].titulo)


#Opção 7
def consulta_clientes_cadastrados():
    """Função para exibir os clientes cadastrados no sistema"""
    
    print (f"1. Consultar cliente por CPF.\n" \
           f"2. Listar clientes cadastrados.\n" )
    
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        cpf = input("CPF do cliente: ")
        if lista_clientes.buscar_cliente_cpf(cpf) == None:
            print(f"Cliente com CPF {cpf} não encontrado.")
        else:
            print(lista_clientes.buscar_cliente_cpf(cpf))

    elif escolha == "2":
        lista_clientes.listar_clientes()

    else:
        print("Opção invalida.")
