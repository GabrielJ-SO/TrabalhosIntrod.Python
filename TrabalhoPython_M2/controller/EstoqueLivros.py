
from model.Livro import Livro

class EstoqueLivros:
    def __init__(self):
        self._livros = []

    def adicionar_livro_aoestoque(self, livro):
        """Adiciona um livro ao estoque"""
        self._livros.append(livro)

    def listar_livros_emestoque(self):
        """Lista todos os livros no estoque"""

        print("------Livros Cadastrados------\n")

        for livro in self._livros:
            print(livro.__str__())

    def buscar_livro_titulo(self, titulo_buscado:str):
        """Busca um livro pelo titulo
        Args: 
            titulo:str titulo do livro"""
             
        livros_encontrados = [livro for livro in self._livros if livro.titulo == titulo_buscado]

        for livro in livros_encontrados:
            print(livro.__str__())

    def buscar_livros_autor(self, autor_buscado:str):
        """Busca os livros de """
        livros_encontrados = [livro for livro in self._livros if livro.autor == autor_buscado]

        print(f"Livros do autor {autor_buscado}:")
        for livro in livros_encontrados:
            print(livro.__str__())



        