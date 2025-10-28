
from model.Livro import Livro
import os

class EstoqueLivros:
    def __init__(self):
        
        self._livros = self.carregar_livros()
        
    @property
    def livros(self):
        """Metodo getter para o atributo clientes"""
        return self._livros

    def carregar_livros(self):

        lista_livros = []

        if not os.path.exists("saves/livros.txt"):
            return lista_livros
        
        with open("saves/livros.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()
        
        for linha in linhas:
            info = linha.split(";")
            novo_livro = Livro(info[0], info[1], int(info[2]), int(info[3]))
            lista_livros.append(novo_livro)
        
        return lista_livros
        
    def adicionar_livro_aoestoque(self, livro):
        """Adiciona um livro ao estoque"""

        if livro in self._livros:
            print("Este livro ja esta cadastrado no sistema!!!")
            return

        os.makedirs("saves", exist_ok=True)

        with open("saves/livros.txt", "a", encoding="utf-8") as f:
            f.write(livro.save())

        self._livros.append(livro)
        print(f'Livro "{livro.titulo}" do autor "{livro.autor}" cadastrado com sucesso.')

    def listar_livros_emestoque(self):
        """Lista todos os livros no estoque"""

        print("------Livros Cadastrados------\n")

        for livro in self._livros:
            print(livro)

    def buscar_livro_titulo(self, titulo_buscado:str):
        """Busca um livro pelo titulo
        Args: 
            titulo:str titulo do livro"""
             
        livros_encontrados = [livro for livro in self._livros if livro.titulo.strip().lower() == titulo_buscado.strip().lower()]

        return livros_encontrados

    def buscar_livros_autor(self, autor_buscado:str):
        """Busca os livros de um autor"""
        livros_encontrados = [livro for livro in self._livros if livro.autor.strip().lower() == autor_buscado.strip().lower()]

        print(f"Livros do autor {autor_buscado}:")
        for livro in livros_encontrados:
            print(livro)