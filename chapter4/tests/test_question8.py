import pytest


from chapter4.question8 import _TreeNode, find_common_parent_node


@pytest.fixture
def nodes1():
    node0 = _TreeNode(0)
    node1 = _TreeNode(1)
    node2 = _TreeNode(2)

    node0.set_children(node1, node2)
    return [node0, node1, node2]


@pytest.fixture
def nodes2():
    node0 = _TreeNode(0)
    node1 = _TreeNode(1)
    node2 = _TreeNode(2)
    node3 = _TreeNode(3)
    node4 = _TreeNode(4)

    node0.set_children(node1, node2)
    node1.set_children(node3)
    node3.set_children(node4)
    return [node0, node1, node2, node3, node4]


def test_find_common_parent_node1(nodes1):
    assert find_common_parent_node(nodes1[1], nodes1[2]) == nodes1[0]


def test_find_common_parent_node2(nodes2):
    assert find_common_parent_node(nodes2[4], nodes2[2]) == nodes2[0]
