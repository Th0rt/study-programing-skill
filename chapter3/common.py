from dataclasses import dataclass


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


@dataclass
class QueueNode:
    data: int
    next: "QueueNode" = None


class Queue:
    def __init__(self):
        self._first = None
        self._last = None

    def add(self, item):
        t = QueueNode(item)
        if self._last:
            self._last.next = t

        self._last = t

        if self._first is None:
            self._first = self._last

    def remove(self):
        data = self._first.data
        self._first = self._first.next
        if self._first is None:
            self._last = None
        return data

    def peek(self):
        if self._first is None:
            return None
        return self._first.data

    @property
    def is_empty(self):
        return self._first is None
