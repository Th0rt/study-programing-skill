import pytest

from chapter4.question12 import count_root, add_and_filter
from lib.tree import BinaryTree, BinaryTreeNode, list_to_bst


@pytest.fixture
def tree1():
    """ 1-2-3-4 """
    return BinaryTree(
        root=BinaryTreeNode(
            value=1,
            left=BinaryTreeNode(
                value=2, left=BinaryTreeNode(value=3, left=BinaryTreeNode(value=4))
            ),
        )
    )


@pytest.fixture
def tree2():
    """ 1-2-3-4 """
    return BinaryTree(
        root=BinaryTreeNode(
            value=1,
            left=BinaryTreeNode(
                value=2, left=BinaryTreeNode(value=3, left=BinaryTreeNode(value=4))
            ),
            right=BinaryTreeNode(
                value=2, left=BinaryTreeNode(value=3, left=BinaryTreeNode(value=4))
            ),
        )
    )


def test1(tree1):
    assert count_root(3, tree1) == 2


def test2(tree2):
    assert count_root(3, tree2) == 4


def test_add_and_filter():
    assert add_and_filter([6, 5, 3, 0], 4, 9) == (1, [7, 4])
