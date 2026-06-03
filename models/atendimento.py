from datetime import datetime


class Atendimento:

    def __init__(self, cliente):

        self.cliente = cliente
        self.atendente = None

        self.data_inicio = datetime.now()

        self.data_fim = None

        self.duracao = 0