from random import randint


class BinaryTreeNode:
    def __init__(self, id, value, left=None, right=None):
        self.id = id
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, values):
        self.root = self._create_nodes(values)
        self.node_count = len(values)

    def _create_nodes(self, values, ids=None):
        if not values:
            return None
        if not ids:
            ids = list(range(len(values)))

        mid_index = len(values) // 2
        node = BinaryTreeNode(id=ids[mid_index], value=values[mid_index])
        node.left = self._create_nodes(values[:mid_index], ids=ids[:mid_index])
        node.right = self._create_nodes(
            values[mid_index + 1 :], ids=ids[mid_index + 1 :]
        )
        return node

    def get_random_node(self):
        i = randint(0, self.node_count)
        node = self.root

        while node:
            if node.id == i:
                return node
            node = node.left if node.id > i else node.right

        return None
