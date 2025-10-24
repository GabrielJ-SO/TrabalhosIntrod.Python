

class EstoqueLivros:
    def __init__(self):
        self.livros = []

    def adicionar_livro_aoestoque(self, livro):
        """Adiciona um livro ao estoque"""
        self.livros.append(livro)
        print(f'Livro "{livro.titulo}" adicionado ao estoque.')

    def listar_livros_emestoque(self):
        """Lista todos os livros no estoque"""
        for livro in self.livros:
            print(livro.__str__())