
def count_root(num, tree, stack=[], root_count=0):


    return True


def _count(num, limit, stack=[])
    if stack is []:
        if num < limit:
            stack.append(node.value)
        return stack

    num2 = stack[0] + num
    if num2 < limit:
        stack.append(num2)

    return _count(num, limit, stack=stack[1:])
