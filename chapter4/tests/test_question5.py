import pytest
from lib.tree import BinaryTree, BinaryTreeNode
from chapter4.question5 import is_bst


@pytest.fixture
def binary_tree():
    tree = BinaryTree(
        root=BinaryTreeNode(
            4,
            left=BinaryTreeNode(2, left=BinaryTreeNode(1), right=BinaryTreeNode(3)),
            right=BinaryTreeNode(6, left=BinaryTreeNode(5), right=BinaryTreeNode(7)),
        )
    )
    return tree


@pytest.fixture
def not_binary_tree():
    tree = BinaryTree(
        root=BinaryTreeNode(
            4,
            left=BinaryTreeNode(6, left=BinaryTreeNode(1), right=BinaryTreeNode(3)),
            right=BinaryTreeNode(2, left=BinaryTreeNode(5), right=BinaryTreeNode(7)),
        )
    )
    return tree


def test_is_bst(binary_tree):
    assert is_bst(binary_tree.root)


def test_is_not_bst(not_binary_tree):
    assert not is_bst(not_binary_tree.root)
