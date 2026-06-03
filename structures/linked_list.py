class Node:

    def __init__(self, cliente):

        self.cliente = cliente
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, cliente):

        novo = Node(cliente)

        if not self.head:
            self.head = novo
            return

        atual = self.head

        while atual.next:
            atual = atual.next

        atual.next = novo

    def find(self, cliente_id):

        atual = self.head

        while atual:

            if atual.cliente.id == cliente_id:
                return atual.cliente

            atual = atual.next

        return None

    def remove(self, cliente_id):

        if not self.head:
            return False

        if self.head.cliente.id == cliente_id:
            self.head = self.head.next
            return True

        anterior = self.head
        atual = self.head.next

        while atual:

            if atual.cliente.id == cliente_id:
                anterior.next = atual.next
                return True

            anterior = atual
            atual = atual.next

        return False

    def count_recursive(self, node):

        if node is None:
            return 0

        return 1 + self.count_recursive(node.next)