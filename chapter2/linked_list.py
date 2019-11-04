import unittest


class LinkedList:
    def __init__(self, *args):
        self.head, self.tail = self.create_nodes(values=args)
        self.current = self.head

    def next(self):
        self.current = self.current.next

    def get_node(self):
        return self.current

    def create_nodes(self, head=None, tail=None, values=[]):
        if not values:
            return head, tail

        elif not head:
            return self.create_nodes(head=LinkedListNode(values[0]), tail=None, values=values[1:])

        elif not tail:
            head.next = LinkedListNode(values[0])
            return self.create_nodes(head=head, tail=head.next, values=values[1:])

        else:
            tail.next = LinkedListNode(values[0])
            return self.create_nodes(head=head, tail=tail.next, values=values[1:])


class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
