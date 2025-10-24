

class Livro:


    def __init__(self, titulo: str, autor: str, ano_publicacao: int, quantidade_disponivel: int):
        """Construtor da classe Livro

        Args:
            titulo (str): Título do livro
            autor (str): Autor do livro
            ano_publicacao (int): Ano de publicação do livro
            quantidade_disponivel (int): Quantidade disponível do livro
        """
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._quantidade_disponivel = quantidade_disponivel

    @property
    def titulo(self):
        """Metodo getter para o atributo titulo"""
        return self._titulo
    
    @property
    def autor(self):
        """Metodo getter para o atributo autor"""
        return self._autor
    @property
    def ano_publicacao(self):
        """Metodo getter para o atributo ano_publicacao"""
        return self._ano_publicacao
    
    @property
    def quantidade_disponivel(self):
        """Metodo getter para o atributo quantidade_disponivel"""
        return self._quantidade_disponivel
    
    @quantidade_disponivel.setter
    def quantidade_disponivel(self, quantidade: int):
        """Metodo setter para o atributo quantidade_disponivel"""

        self._quantidade_disponivel = quantidade

    def __str__(self) -> str:
        """Exibe as informações do livro:
        Título, Autor, Ano de Publicação e Quantidade Disponível.
        """
        return f"Título: {self._titulo}\nAutor: {self._autor}\nAno de Publicação: {self._ano_publicacao}\nQuantidade Disponível: {self._quantidade_disponivel}\n"
    
    def adicionar_livro(self, quantidade: int):
        """Adiciona uma quantidade ao estoque do livro
         Args:
            quantidade (int): Quantidade a ser adicionada

        Returns:
            int: Quantidade em estoque atualizada"""
        
        if quantidade <= 0:
            print("A quantidade não pode ser negativa.")
            return self._quantidade_disponivel
        
        self._quantidade_disponivel += quantidade
        print(f"Quantidade adicionada: {quantidade}")

    def remover_livro(self, quantidade: int):
        """Remove uma quantidade do estoque do livro
        Args:
            quantidade_removida (int): Quantidade a ser removida

        Returns:
            int: Quantidade em estoque atualizada"""
          
        if quantidade > self._quantidade_disponivel:
            print("A quantidade a ser removida é maior do que a disponível em estoque.")
            return self._quantidade_disponivel
        
        if quantidade <= 0:
            print("A quantidade não pode ser negativa.")
            return self._quantidade_disponivel

        self._quantidade_disponivel -= quantidade
        print(f"Quantidade removida: {quantidade}")
        