class Cliente:

    def __init__(self, id_cliente, nome, telefone, prioridade=False):

        self.id = id_cliente
        self.nome = nome
        self.telefone = telefone
        self.prioridade = prioridade