from lib.tree import Tree, TreeNode


class _TreeNode(TreeNode):
    def __init__(self, name, parent=None, children=[]):
        super().__init__(name, children=children)
        self.parent = parent

    def set_children(self, *nodes):
        self.children.extend(nodes)
        for node in nodes:
            node.parent = self


def find_common_parent_node(node1, node2, mem={}):
    if node1 is None and node2 is None:
        return None

    if node1.parent:
        if id(node1.parent) in mem:
            return node1.parent
        else:
            mem[id(node1.parent)] = True

    if node2.parent:
        if id(node2.parent) in mem:
            return node2.parent
        else:
            mem[id(node2.parent)] = True

    return find_common_parent_node(node1.parent, node2.parent)
