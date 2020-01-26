from typing import List


class TreeNode:
    def __init__(self, name: str, children: List["TreeNode"] = None):
        self.name = name
        self.children = children


class Tree:
    def __init__(self, root: TreeNode = None):
        self.root = root


class BinaryTreeNode(TreeNode):
    def __init__(self, value: str, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree(Tree):
    def __init__(self, root: BinaryTreeNode = None):
        self.root = root


def list_to_bst(values):
    if not values:
        return None

    mid_index = len(values) // 2
    node = BinaryTreeNode(values[mid_index])
    node.left = list_to_bst(values[:mid_index])
    node.right = list_to_bst(values[mid_index + 1 :])
    return node
