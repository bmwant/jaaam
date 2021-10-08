from typing import List

class Node(object):
    def __init__(self, value: int = None):
        self.value = value
        self.left: Node = None
        self.right: Node = None

    def __str__(self):
        return f'{self.value}'


def generate_tree_inner(node: Node, levels: int) -> Node:
    counter = 0

    def gen_inner(node: Node, levels: int) -> Node:
        nonlocal counter
        counter += 1
        if levels == 0:
            return Node(counter)

        node.value = counter
        node.left = gen_inner(Node(), levels-1)
        node.right = gen_inner(Node(), levels-1)
        return node

    return gen_inner(node, levels)


counter = 0
def generate_tree_global(node: Node, levels: int) -> Node:
    global counter
    counter += 1
    if levels == 0:
        return Node(counter)

    node.value = counter
    node.left = generate_tree_global(Node(), levels-1)
    node.right = generate_tree_global(Node(), levels-1)
    return node


def generate_tree_mutable(node: Node, levels: int, counter: List[int] = [0]):
    """
    NOTE: Do not rely on such a code.
    Exploiting the fact that list element will point to the same variable between
    function invocations.
    """
    counter[0] += 1
    if not levels:
        return Node(counter[0])

    node.value = counter[0]
    node.left = generate_tree_mutable(Node(), levels-1, counter)
    node.right = generate_tree_mutable(Node(), levels-1, counter)
    return node


def print_tree(root: Node, level: int = 0):
    if root is None:
        return
    print_tree(root.right, level+1)
    print('  ' * level, end='')
    print(root)
    print_tree(root.left, level+1)


def invert_tree(root: Node) -> Node:
    pass


if __name__ == '__main__':
    root = Node()
    # tree = generate_tree_global(root, 2)
    # tree = generate_tree_mutable(root, 2)
    tree = generate_tree_inner(root, 2)
    print('Initial tree')
    print_tree(tree)
    print('Inverted tree')
