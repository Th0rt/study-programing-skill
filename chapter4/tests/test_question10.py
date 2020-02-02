import pytest
from lib.tree import list_to_bst, BinaryTree

from chapter4.question10 import is_patial_tree, search_value


@pytest.fixture
def tree1():
    values = list(range(7))
    return BinaryTree(root=list_to_bst(values))


@pytest.fixture
def tree2():
    values = list(range(15))
    return BinaryTree(root=list_to_bst(values))


def test_it(tree1, tree2):
    assert is_patial_tree(tree1, tree2)
    assert not is_patial_tree(tree2, tree1)


def test_search_value(tree1):
    assert search_value(tree1, 3).value == 3
    assert search_value(tree1, 6).value == 6
    assert search_value(tree1, 7) == None
