def count_root(threshold, tree):
    return _count_root(threshold, tree.root)


def _count_root(threshold, node, interims=[], root_count=0):
    if node is None:
        return root_count

    interims.append(0)  # node単体の値を計算対象に入れるため、0を加える
    equals, smalls = add_and_filter(
        nums=interims, additional=node.value, threshold=threshold
    )
    root_count += len(equals)

    if node.left:
        root_count += _count_root(threshold, node.left, smalls)

    if node.right:
        root_count += _count_root(threshold, node.right, smalls)

    return root_count


def add_and_filter(nums, additional, threshold):
    """
    numsの各値にaddtionalを加算し、threshold比較する。
    その後、thresholdと比較し、thresholdと等しい値と、thresholdより小さい数を返す。
    """
    equals = []
    smalls = []

    for num in nums:
        t = num + additional

        if t < threshold:
            smalls.append(t)
        if t == threshold:
            equals.append(t)

    return equals, smalls
