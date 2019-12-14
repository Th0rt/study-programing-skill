from linked_list import LinkedListNode
import unittest


def extract_common_node(node1, node2):
    return extract_nodes_in_mem(node=node1, mem=memorize_nodes(node2))


def extract_nodes_in_mem(node, mem):
    extracts = []
    while node:
        if node.value in mem.keys():
            if node in mem[node.value]:
                extracts.append(node)
        node = node.next
    return extracts


def memorize_nodes(node):
    mem = dict()
    while node:
        mem.setdefault(node.value, []).append(node)
        node = node.next
    return mem


class TestQuestion7(unittest.TestCase):
    def test_it(self):
        node1 = LinkedListNode(1)
        node2 = LinkedListNode(2)
        node3 = LinkedListNode(3)
        node4 = LinkedListNode(4)
        node5 = LinkedListNode(5)

        # List1, node1 -> 2 -> 3
        node1.next = node2
        node2.next = node3

        # List2, node5 -> 4 -> 3
        node5.next = node4
        node4.next = node3

        assert extract_common_node(node1, node5) == [node3]

    def test_memorize_nodes(self):
        node1 = LinkedListNode(1)
        node2 = LinkedListNode(2)
        node3 = LinkedListNode(3)
        node4 = LinkedListNode(2)
        node5 = LinkedListNode(1)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        actual = memorize_nodes(node1)
        expect = {
            1: [node1, node5],
            2: [node2, node4],
            3: [node3]
        }
        assert actual == expect


if __name__ == "__main__":
    unittest.main()
