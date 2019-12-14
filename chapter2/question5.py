import unittest
from linked_list import LinkedList, LinkedListNode


def multiple_linked_list(x, y, result=None, carry_over=0):
    if not x and not y:
        return result

    x_vlaue = x.value if x else 0
    y_value = y.value if y else 0

    tens, ones = divmod(x_vlaue + y_value + carry_over, 10)

    if not result:
        result = LinkedList(ones)
    else:
        result.append_node_to_tail(LinkedListNode(ones))

    return multiple_linked_list(
        x.next if x else None,
        y.next if y else None,
        result=result,
        carry_over=tens
    )


def multiple_linked_list_reverse(x, y):
    num = linked_list_to_int(x) + linked_list_to_int(y)
    return int_to_linked_list(num)


def int_to_linked_list(n):
    nums = [int(num) for num in str(n)]
    return LinkedList(*nums)


def linked_list_to_int(x: LinkedListNode, s=""):
    if not x:
        return int(s)
    return linked_list_to_int(x.next, s=s+str(x.value))


class TestQuestion5(unittest.TestCase):
    def test_it(self):
        x = LinkedList(7, 1, 6)
        y = LinkedList(5, 9, 2)
        actual = multiple_linked_list(x.current, y.current)
        assert actual.current.value == 2
        assert actual.next() == 1
        assert actual.next() == 9

    def test_it2(self):
        x = LinkedList(7, 1)
        y = LinkedList(5, 9, 2)
        actual = multiple_linked_list(x.current, y.current)
        assert actual.current.value == 2
        assert actual.next() == 1
        assert actual.next() == 3

    def test_it3(self):
        x = LinkedList(7)
        y = LinkedList(5, 9, 2)
        actual = multiple_linked_list(x.current, y.current)
        assert actual.current.value == 2
        assert actual.next() == 0
        assert actual.next() == 3

    def test_it4(self):
        x = LinkedList(5, 9, 2)
        y = LinkedList(7, 1)
        actual = multiple_linked_list(x.current, y.current)
        assert actual.current.value == 2
        assert actual.next() == 1
        assert actual.next() == 3

    def test_it5(self):
        x = LinkedList(5, 9, 2)
        y = LinkedList(7)
        actual = multiple_linked_list(x.current, y.current)
        assert actual.current.value == 2
        assert actual.next() == 0
        assert actual.next() == 3

    def test_multiple_linked_list_reverse(self):
        x = LinkedList(6, 1, 7)
        y = LinkedList(2, 9, 5)

        actual = multiple_linked_list_reverse(x.current, y.current)
        assert actual.current.value == 9
        assert actual.next() == 1
        assert actual.next() == 2

    def test_linked_list_to_int(self):
        x = LinkedList(6, 1, 7)
        assert linked_list_to_int(x.head) == 617

    def test_int_to_linked_list(self):
        x = 123
        actual = int_to_linked_list(x)
        assert actual.current.value == 1
        assert actual.next() == 2
        assert actual.next() == 3


if __name__ == "__main__":
    unittest.main()
