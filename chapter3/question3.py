import unittest
import pdb


class NodeNotExistError(Exception):
    pass


class ExceedMaxStackLengthError(Exception):
    pass


class StackNode:
    def __init__(self, data, index: int = None, next=None):
        self.index = index
        self.data = data
        self.next = next


class Stack:
    max_length = 4

    def __init__(self, index: int = None, top=None, next=None):
        self.index = index
        self._top = top
        self.next = next

    def pop(self):
        if self.is_empty:
            return None

        item = self._top
        self._top = self._top.next
        return item

    def push(self, item):
        if self.is_empty:
            index = 0
        else:
            index = self.peek().index + 1

        if index > self.max_length:
            raise ExceedMaxStackLengthError

        self._top = StackNode(index=index, data=item, next=self._top)

    def peek(self):
        return self._top

    @property
    def is_empty(self):
        return self._top is None


class SetOfStacks:
    def __init__(self, top: Stack = None):
        self._top = top

    def pop(self):
        if self.is_empty:
            return None

        t = self.peek().pop()
        if self.peek().is_empty:
            self._top = self._top.next
        return t

    def pop_at(self, index):
        if self.peek().index < index:
            return None

        stack = self.peek()
        while stack:
            if stack.index == index:
                return stack.pop()
            stack = stack.next

    def push(self, item):
        if not self.is_empty:
            try:
                self.peek().push(item)
            except ExceedMaxStackLengthError:
                self._add_stack(item)
        else:
            self._add_stack(item)

    def _add_stack(self, item):
        if self.is_empty:
            index = 0
        else:
            index = self.peek().index + 1

        self._top = Stack(
            index=index,
            top=StackNode(index=0, data=item),
            next=self._top
        )

    def peek(self):
        return self._top

    @property
    def is_empty(self):
        return self._top is None


class TestQuestion3(unittest.TestCase):
    def test_push_error(self):
        s = Stack()

        for num in range(5):
            s.push(num)

        with self.assertRaises(ExceedMaxStackLengthError):
            s.push(1)

    def test_push_6times(self):
        s = SetOfStacks()
        for num in range(6):
            s.push(num)

        stack1_id = id(s.peek())
        assert s.pop().data == 5

        stack2_id = id(s.peek())
        assert s.pop().data == 4
        assert s.pop().data == 3
        assert s.pop().data == 2
        assert s.pop().data == 1
        assert s.pop().data == 0

        assert stack1_id != stack2_id

    def test_pop_at(self):
        s = SetOfStacks()
        for num in range(6):
            s.push(num)

        assert s.pop_at(1).data == 5
        assert s.pop_at(0).data == 4


if __name__ == "__main__":
    unittest.main()
