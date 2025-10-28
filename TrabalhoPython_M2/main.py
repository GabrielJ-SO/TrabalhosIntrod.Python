
import os
import utils.Utils as Utils
from model.Livro import Livro
from controller.EstoqueLivros import EstoqueLivros
from model.Cliente import Cliente




opcoes = {"1": Utils.cadastrar_cliente,
         "2": Utils.cadastrar_livro,
         "3": Utils.cosulta_livros_cadastrados,
         "4": Utils.realizar_emprestimo,
         "5": Utils.realizar_devolucao,
         "6": Utils.listar_emprestimos_cliente,
         "7": Utils.consulta_clientes_cadastrados}

while True:
    print(Utils.menu())
    escolha = input("Escolha uma opção: ")

    if escolha == "0":
        print("Saindo do sistema...")
        break

    if escolha in opcoes:
        os.system("cls")
        opcoes[escolha]()

    else:
        print("Opção inválida.")

