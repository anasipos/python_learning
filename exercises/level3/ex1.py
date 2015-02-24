import collections

__author__ = 'anamaria.sipos'


class PreorderArgError(Exception):
    pass


def is_tree(tree):
    return type(tree) == tuple and len(tree) == 3


def preorder(tree):
    if len(tree) == 0:
        return

    tree_copy = tree[:]
    stack = collections.deque()

    stack.append(tree_copy)

    while len(stack) > 0:
        current = stack.popleft()
        if is_tree(current):
            yield current[0]

            left_node = current[1]
            right_node = current[2]
            if left_node is not None:
                stack.append(left_node)
            if right_node is not None:
                stack.append(right_node)
        else:
            raise PreorderArgError()