from datetime import datetime

class Atendimento:
    def __init__(self, cliente, atendente=None):
        self.cliente = cliente
        self.atendente = atendente
        self.data_inicio = datetime.now()
        self.data_fim = None