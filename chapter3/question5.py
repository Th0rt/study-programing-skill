from chapter3.common import Stack, StackNode


class AscSortedStack:
    def __init__(self, top=None):
        self._stack = Stack(top=top)

    def pop(self):
        return self._stack.pop()

    def push(self, item):
        if self._stack.is_empty:
            self._stack.push(item)
            return None

        storage = Stack()
        while not self._stack.is_empty:
            if item <= self._stack.peek().data:
                break
            storage.push(self._stack.pop().data)

        self._stack.push(item)

        while not storage.is_empty:
            self._stack.push(storage.pop().data)

    @property
    def is_empty(self):
        return self._stack.is_empty
