
import os
import utils.Utils as Utils
from model.Livro import Livro
from controller.EstoqueLivros import EstoqueLivros


estoque = EstoqueLivros()

livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 10)

print(livro1)

opcoes = {"1": Utils.cadastrar_cliente,
         "2": "Cadastrar livro",
         "3": "Listar livros em estoque",
         "4": "Realizar empréstimo",
         "5": "Realizar devolução",
         "6": "Exibir empréstimos de um cliente",
         "7": "Consultar livro",
         "8": Utils.consulta_clientes_cadastrados,
         "9": "Sair"}

while True:
    print(Utils.menu())
    escolha = input("Escolha uma opção: ")

    if escolha == "9":
        print("Saindo do sistema...")
        break

    if escolha in opcoes:
        os.system("cls")
        opcoes[escolha]()

    else:
        print("Opção inválida.")

