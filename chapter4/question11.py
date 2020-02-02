def is_patial_tree(small_tree, big_tree):

    def _compare(entire, partial):
        if not partial:
            return True

        if not entire:
            return False

        if not entire.value == partial.value:
            return False

        if partial.left:
            return _compare(entire.left, partial.left)

        if partial.right:
            return _compare(entire.right, partial.right)

        return True

    big_tree_root = search_value(big_tree, small_tree.root.value)
    if not big_tree_root:
        return False
    else:
        return _compare(big_tree_root, small_tree.root)



def search_value(tree, value):
    def _search(node1, value):
        if node1.value == value:
            return node1

        if node1.left:
            left_search = _search(node1.left, value)
            if left_search:
                return left_search
        if node1.right:
            right_search = _search(node1.right, value)
            if right_search:
                return right_search

        return None

    return _search(tree.root, value)
