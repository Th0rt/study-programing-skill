from typing import List


class TreeNode:
    def __init__(self, name: str, children: List["TreeNode"] = None):
        self.name = name
        self.children: children


class Tree:
    def __init__(self, root: TreeNode = None):
        self.root = root
