class NodeDoesNotExistError(Exception):
    pass


class Stack:
    def __init__(self):
        self.top = None

    def pop(self):
        if self.top is None:
            raise NodeDoesNotExistError
        data = self.top.data
        self.top = top.next
        return data

    def push(self, data):
        node = StackNode(data)
        node.next = self.top
        self.top = node

    def peek(self):
        if self.top is None:
            raise NodeDoesNotExistError
        return self.top.data

    def is_empty(self):
        return self.top is None


class StackNode:
    def __init__(self, data, next: "StackNode" = None):
        self.data = data
        self.next = next
