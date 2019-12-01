
class StackNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self, top: StackNode = None):
        self._top = top

    def pop(self):
        if not self._top:
            return None
        item = self._top
        self._top = self._top.next
        return item

    def push(self, item):
        t = StackNode(item, self._top)
        self._top = t

    def peek(self):
        return self._top

    @property
    def is_empty(self):
        return self._top is None
