import unittest
from linked_list import LinkedList, LinkedListNode


def is_circulation(node: LinkedListNode) -> bool:
    mem = dict()
    while node:
        if node.value in mem:
            if node in mem[node.value]:
                return True
        else:
            mem.setdefault(node.value, []).append(node)
        node = node.next
    return False


class TestQuestion8(unittest.TestCase):
    def test_it(self):
        node1 = LinkedListNode(1)
        node2 = LinkedListNode(2)
        node3 = LinkedListNode(3)
        node4 = LinkedListNode(4)
        node5 = LinkedListNode(5)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node3

        assert is_circulation(node1)

    def test_it2(self):
        node1 = LinkedListNode(1)
        node2 = LinkedListNode(2)
        node3 = LinkedListNode(3)
        node4 = LinkedListNode(4)
        node5 = LinkedListNode(5)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        assert not is_circulation(node1)

    def test_it3(self):
        node1 = LinkedListNode(1)
        node2 = LinkedListNode(2)
        node3 = LinkedListNode(3)
        node4 = LinkedListNode(4)
        node5 = LinkedListNode(1)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        assert not is_circulation(node1)


if __name__ == "__main__":
    unittest.main()
