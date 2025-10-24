
from model.Cliente import Cliente

class ClientesCadastrados:
    def __init__(self):
        self._clientes = set()

    @property
    def clientes(self):
        """Metodo getter para o atributo clientes"""
        return self._clientes

    def adicionar_cliente(self, cliente: Cliente):
        """Adiciona um cliente ao conjunto de clientes
        Args:
            cliente (Cliente): Objeto Cliente a ser adicionado
        """
       
        if self._clientes.__contains__(cliente):
            print(f'Cliente com CPF "{cliente.cpf}" já está cadastrado.')
            return
         
        self._clientes.add(cliente)

    def listar_clientes(self):
        """Lista todos os clientes cadastrados"""

        print(f"------Clientes Cadastrados:------\n")
        for cliente in self._clientes:
            print(cliente.__str__())

    def buscar_cliente_cpf(self, cpf):
        """Busca um cliente de dentro do conjunto pelo CPF"""

        #A expressão entre parênteses é um gerador
        # Ele procura o cliente onde cliente.cpf é igual ao desejado
        cliente_encontrado = next(
            (cliente for cliente in self._clientes if cliente.cpf == cpf),
            None  # Este é o 'default'. Retorna None se não encontrar nenhum
        )

        if cliente_encontrado:
            print(f"Cliente encontrado: {cliente_encontrado.__str__()}")
        else:
            print("Cliente não encontrado.")
              
