from typing import List

from tree import Node, print_tree


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


def invert_tree(node: Node) -> Node:
    if node is None:
        return

    left_inverted = invert_tree(node.left)
    right_inverted = invert_tree(node.right)
    node.right = left_inverted
    node.left = right_inverted
    return node


if __name__ == '__main__':
    root = Node()
    # tree = generate_tree_global(root, 2)
    # tree = generate_tree_mutable(root, 2)
    tree = generate_tree_inner(root, 2)
    print('Initial tree')
    print_tree(tree)
    print('Inverted tree')
    inverted = invert_tree(tree)
    print_tree(inverted)
