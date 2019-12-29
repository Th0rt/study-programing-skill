from lib.tree import BinaryTree, BinaryTreeNode


class _BinaryTreeNode(BinaryTreeNode):
    parent = None
    left = None
    right = None

    def __init__(self, name, left=None, right=None):

        super().__init__(name, left=left, right=right)

        if self.left:
            self.left.parent = self

        if self.right:
            self.right.parent = self

    def set_left(self, node):
        self.left = node
        node.parent = self

    def set_right(self, node):
        self.right = node
        node.parent = self

    def set_children(self, left=None, right=None):
        if left:
            self.set_left(left)
        if right:
            self.set_right(right)


def find_next_node(node):
    if node.right:
        return _find_next_node_to_children(node, node.right)
    else:
        return _find_next_node_to_parents(node, pointer=node.parent)



def _find_next_node_to_parents(node, pointer):
    if pointer is None:
        return None

    if pointer.name > node.name:
        return pointer

    return _find_next_node_to_parents(node, pointer=pointer.parent)


def _find_next_node_to_children(node, pointer):
    if pointer is None:
        raise ValueError()

    if pointer.left is None:
        return pointer

    return _find_next_node_to_children(node, pointer.left)
