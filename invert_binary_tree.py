class Node(object):
    def __init__(self, value: int = None):
        self.value = value
        self.left: Node = None
        self.right: Node = None

    def __str__(self):
        return f'{self.value}'


def generate_tree_(node: Node, levels: int) -> Node:
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


def generate_tree(node: Node, levels: int, counter) -> Node:
    if levels == 0:
        return Node(counter)

    node.value = counter
    node.left = generate_tree(Node(), levels-1, counter+1)
    node.right = generate_tree(Node(), levels-1, counter+1)
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
    tree = generate_tree(root, 2)
    print('Initial tree')
    print_tree(tree)
    print('Inverted tree')
