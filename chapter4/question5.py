def is_bst(node):
    if node.left:
        left_is_bst = _is_bst(node.left)
    if node.right:
        right_is_bst = _is_bst(node.right)
    node_is_bst = _is_bst(node)
    return all([node_is_bst, left_is_bst, right_is_bst])


def _is_bst(node):
    if node.left and node.right:
        return node.left.data < node.data < node.right.data
    if node.left:
        return node.left < node.data
    if node.right:
        return node.data < node.right
