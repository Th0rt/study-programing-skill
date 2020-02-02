import pytest
from chapter4.question12 import BinaryTree


@pytest.fixture
def tree():
    values = list(range(7))
    return BinaryTree(values)


def test_it(tree):
    assert tree.root.value == 3
    assert tree.root.left.value == 1
    assert tree.root.right.value == 5


def test_get_random(tree):
    assert tree.get_random_node()

