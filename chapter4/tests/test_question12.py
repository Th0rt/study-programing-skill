import pytest

from chapter4.question12 import count_root, _count
from lib.tree import BinaryTree, BinaryTreeNode, list_to_bst


@pytest.fixture
def tree1():
    """ 1-2-3-4 """
    return BinaryTree(root=BinaryTreeNode(
        value=1,
        left=BinaryTreeNode(
            value=2,
            left=BinaryTreeNode(
                value=3,
                left=BinaryTreeNode(value=4)
                )
            )
        )
    )


def test1(tree1):
    assert count_root(10, tree1) == 10


def test_count():
    assert _count(4, 9, stack=[6, 5, 3]) == [9, 7, 4]
