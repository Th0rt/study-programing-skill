from dataclasses import dataclass


class LinkedList:
    def __init__(self, head: "LinkedListNode" = None):
        self.head = head

    def append_to_tail(self, data):
        node = self.head
        while node.next:
            node = node.next
        node.next = LinkedListNode(data)


@dataclass
class LinkedListNode:
    data: int
    next: "LinkedListNode" = None
