import pytest
from chapter4.question6 import (
    find_next_node,
    _BinaryTreeNode,
    _find_next_node_to_parents,
    _find_next_node_to_children,
)
from lib.tree import BinaryTree


@pytest.fixture
def nodes():
    return [_BinaryTreeNode(n) for n in range(15)]


@pytest.fixture
def comprete_binary_tree(nodes):
    nodes[7].set_children(left=nodes[3], right=nodes[11])

    nodes[3].set_children(left=nodes[1], right=nodes[5])
    nodes[11].set_children(left=nodes[9], right=nodes[13])

    nodes[1].set_children(left=nodes[0], right=nodes[2])
    nodes[5].set_children(left=nodes[4], right=nodes[6])
    nodes[9].set_children(left=nodes[8], right=nodes[10])
    nodes[13].set_children(left=nodes[12], right=nodes[14])

    return BinaryTree(root=nodes[7])


@pytest.fixture
def uncomprete_binary_tree(nodes):
    nodes[7].set_children(left=nodes[3], right=nodes[11])

    nodes[3].set_children(left=nodes[1], right=nodes[5])
    nodes[11].set_children(left=nodes[9], right=nodes[13])

    nodes[1].set_children(left=nodes[0], right=None)
    nodes[5].set_children(left=None, right=nodes[6])
    nodes[9].set_children(left=None, right=nodes[10])
    nodes[13].set_children(left=nodes[12], right=nodes[14])

    return BinaryTree(root=nodes[7])


def test_find_next_node_1(comprete_binary_tree, nodes):
    for n in range(14):
        assert find_next_node(nodes[n]).name == n + 1

    assert find_next_node(nodes[14]) == None  # this is last node.


def test_find_next_node_2(uncomprete_binary_tree, nodes):
    assert find_next_node(nodes[1]).name == 3
    assert find_next_node(nodes[3]).name == 5
    assert find_next_node(nodes[7]).name == 9


def test_find_next_node_to_parents(comprete_binary_tree, nodes):
    node = nodes[2]
    assert _find_next_node_to_parents(node, pointer=node.parent).name == 3


def test_find_next_node_to_children(comprete_binary_tree, nodes):
    node = nodes[3]
    assert _find_next_node_to_children(node, pointer=node.right).name == 4
