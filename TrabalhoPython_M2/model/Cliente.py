
from model.Livro import Livro

class Cliente:

    def __init__(self, nome: str, cpf: str):
        """Construtor da classe Cliente

        Args:
            nome (str): Nome do cliente
            cpf (str): CPF do cliente
        """
        self._nome = nome
        self._cpf = cpf
        self._lista_emprestimos = []

    @property
    def nome(self):
        """Metodo getter para o atributo nome"""
        return self._nome
    
    @property
    def cpf(self):
        """Metodo getter para o atributo cpf"""
        return self._cpf
    
    @property
    def lista_emprestimos(self):
        """Metodo getter para o atributo ListaEmprestimos"""
        return self._lista_emprestimos
    
    def adicionar_emprestimo(self, livro: Livro):
        """Adiciona um empréstimo à lista de empréstimos do cliente

        Args:
            emprestimo (Livro): Livro emprestado
        """

        self._lista_emprestimos.append(livro)  
        print(f'\nEmpréstimo do livro "{livro.titulo}" adicionado à lista de emprestimos do(a) cliente {self._nome}.\n')
        livro.remover_livro(1)

    def remover_emprestimo(self, livro: Livro):
        """Remove um empréstimo da lista de empréstimos do cliente

        Args:
            emprestimo (Livro): Livro devolvido
        """

        livro.adicionar_livro(1)
        self._lista_emprestimos.remove(livro)
        print(f'\nEmpréstimo do livro "{livro.titulo}" removido da lista de emprestimos do(a) cliente {self._nome}.\n')
    
    def exibe_emprestimos_cliente(self):
        """Exibe os empréstimos do cliente"""
        for livro in self._lista_emprestimos:
            print(f"Livro: {livro.titulo} - Autor: {livro.autor}")

    def __str__(self):
        """Metodo toString para Cliente
            Returns:
                str: Representação em string do objeto Cliente
        """

        return f"Nome: {self._nome} | CPF: {self._cpf} | Livros emprestados: {len(self._lista_emprestimos)}"
    
    def __eq__(self, value:str) -> bool:
        """Metodo de comparação entre dois objetos Cliente
        Args:
            value (Cliente): Objeto Cliente a ser comparado
        Returns:
            bool: True se os objetos forem iguais, False caso contrário
        """

        if not isinstance(value, Cliente):
            return False

        return self._cpf == value.cpf
    
    def __hash__(self) -> int:
        """Metodo hash para o objeto Cliente
        Returns:
            int: Hash do objeto Cliente
        """
        
        return hash(self._cpf)
    

