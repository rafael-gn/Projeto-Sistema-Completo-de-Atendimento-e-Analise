from datetime import datetime

from models.atendimento import Atendimento

from structures.queue import Queue
from structures.priority_queue import PriorityQueue
from structures.stack import Stack

fila_comum = Queue()
fila_prioridade = PriorityQueue()

historico = []

pilha_desfazer = Stack()


def abrir_atendimento(cliente):

    atendimento = Atendimento(cliente)

    if cliente.prioridade:
        fila_prioridade.enqueue(
            atendimento
        )

    else:
        fila_comum.enqueue(
            atendimento
        )

    print(
        "Cliente entrou na fila"
    )


def chamar_proximo():

    if not fila_prioridade.is_empty():

        atendimento = (
            fila_prioridade.dequeue()
        )

        return atendimento

    if not fila_comum.is_empty():

        atendimento = (
            fila_comum.dequeue()
        )

        return atendimento

    return None