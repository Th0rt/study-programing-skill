class NodeDoesNotExistError(Exception):
    pass


class QueueNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.first: QueueNode = None
        self.last: QueueNode = None

    def add(self, data):
        node = QueueNode(data)
        if self.last is not None:
            self.last.next = node
        self.last = node
        if self.first is None:
            self.first = node

    def remove(self):
        if self.first is None:
            raise NodeDoesNotExistError
        data = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return data

    def peek(self):
        if self.first is None:
            raise NodeDoesNotExistError
        return self.first.data

    def is_empty(self):
        return self.first is None
