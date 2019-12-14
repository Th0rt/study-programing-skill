import pytest

from lib.tree import Node, Tree
from chapter4.question2 import _create_children, create_tree, _bulk_create_children


class TestQuestion2:
    @pytest.fixture
    def test_data(self):
        return [0, 1, 2, 3, 4, 5, 6, 7]

    def test_it(self, test_data):
        pass

        tree = create_tree(test_data)

        node0 = tree.root
        assert node0.name == 0

        node1, node2 = node0.children
        assert node1.name == 1
        assert node2.name == 2

        node3, node4 = node1.children
        assert node3.name == 3
        assert node4.name == 4

        node5, node6 = node2.children
        assert node5.name == 5
        assert node6.name == 6

        node7 = node3.children[0]
        assert node7.name == 7

    def test_bulk_create_children1(self):
        parents = [Node(1), Node(2)]
        array = [3, 4, 5, 6]
        children = _bulk_create_children(parents, array)
        assert [node.name for node in parents[0].children] == [3, 4]
        assert [node.name for node in parents[1].children] == [5, 6]

    def test_create_s1(self):
        children = _create_children(Node(0), array=[])

        assert [] == []

    def test_create_s2(self):
        children = _create_children(Node(0), array=[1])

        assert [child.name for child in children] == [1]

    def test_create_nodes3(self):
        children = _create_children(Node(0), array=[1, 2])

        assert [node.name for node in children] == [1, 2]
