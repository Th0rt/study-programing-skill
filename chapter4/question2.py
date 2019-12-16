from lib.tree import Tree, TreeNode
from typing import List


def create_tree(array, tree=Tree(), nodes=[]):
    if len(array) == 0:
        return tree

    if tree.root is None:
        tree = Tree()
        root = TreeNode(array[0])
        tree.root = root
        return create_tree(array[1:], tree, [root])

    created = _bulk_create_children(parents=nodes, array=array[:len(nodes)*2])

    return create_tree(array[len(created):], tree, created)


def _bulk_create_children(parents, array, children=[]):

    if len(array) == 0:
        return children

    created = _create_children(parents[0], array[:2])
    return _bulk_create_children(parents[1:], array[2:], children=children+created)


def _create_children(parent, array):
    if len(array) == 0:
        return []

    children = [TreeNode(data) for data in array]
    parent.children = children
    return children
