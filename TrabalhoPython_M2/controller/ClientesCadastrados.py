
from model.Cliente import Cliente
import os

class ClientesCadastrados:
    def __init__(self):
        self._clientes = self.carregar_clientes()

    @property
    def clientes(self):
        """Metodo getter para o atributo clientes"""
        return self._clientes

    def carregar_clientes(self):

        lista_clientes = []

        if not os.path.exists("saves/clientes.txt"):
            return lista_clientes
        
        with open("saves/clientes.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()
        
        for linha in linhas:
            info = linha.split(";")
            novo_cliente = Cliente(info[0], info[1])

            if len(info) > 2 and info[2]:
                titulos = [item.strip() for item in info[2].split(",") if len(item) > 2]
                novo_cliente._lista_emprestimos = titulos

            lista_clientes.append(novo_cliente)
        
        return lista_clientes

    def adicionar_cliente(self, cliente: Cliente):
        """Adiciona um cliente ao conjunto de clientes
        Args:
            cliente (Cliente): Objeto Cliente a ser adicionado
        """
       
        if self._clientes.__contains__(cliente):
            print(f'Cliente com CPF "{cliente.cpf}" já está cadastrado.')
            return

        os.makedirs("saves", exist_ok=True)

        with open("saves/clientes.txt", "a", encoding="utf-8") as f:
            f.write(cliente.save())

        self._clientes.append(cliente)
        print(f'Cliente "{cliente._nome}" cadastrado com sucesso.')

    def listar_clientes(self):
        """Lista todos os clientes cadastrados"""

        print(f"------Clientes Cadastrados:------\n")
        for cliente in self._clientes:
            print(cliente)

    def buscar_cliente_cpf(self, cpf):
        """Busca um cliente de dentro do conjunto pelo CPF"""

        cliente_encontrado = next(
            (cliente for cliente in self._clientes if cliente.cpf == cpf),
            None
        )

        return cliente_encontrado
              