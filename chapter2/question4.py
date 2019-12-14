from linked_list import LinkedList
import unittest


def move_head(node, delimiter, head_list=None, tail_list=None):
    if not node:
        return head_list.append_node_to_tail(tail_list.head)

    if node.value < delimiter:
        if not head_list:
            head_list = LinkedList(node.value)
        else:
            head_list = head_list.append_node_to_tail(node)
    else:
        if not tail_list:
            tail_list = LinkedList(node.value)
        else:
            tail_list = tail_list.append_node_to_tail(node)

    return move_head(node=node.next, delimiter=delimiter, head_list=head_list, tail_list=tail_list)


class TestQuestion4(unittest.TestCase):
    def test_it(self):
        data = LinkedList(3, 5, 8, 5, 10, 2, 1)
        moved = move_head(data.head, delimiter=5)
        assert moved.get_node().value == 3
        assert moved.next() == 2
        assert moved.next() == 1
        assert moved.next() == 5
        assert moved.next() == 8
        assert moved.next() == 5
        assert moved.next() == 10


if __name__ == "__main__":
    unittest.main()
