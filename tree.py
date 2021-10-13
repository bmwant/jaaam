class Node(object):
    def __init__(self, value: int = None):
        self.value = value
        self.left: Node = None
        self.right: Node = None

    def __str__(self):
        return f'{self.value}'

    def __repr__(self) -> str:
        return self.__str__()


def print_tree(root: Node, level: int = 0):
    if root is None:
        return
    print_tree(root.right, level+1)
    print('  ' * level, end='')
    print(root)
    print_tree(root.left, level+1)


def get_height(root: Node, height: int = 0) -> int:
    """
    NOTE: this implementation assumes each branch has equal height
    """
    if root is None:
        return height
    return get_height(root.left, height+1)


def print_tree_horizontal(root: Node, level: int = 0):
    queue = [(root, 0)]
    prev_level = 0
    padding = 2**get_height(root)
    while queue:
        node, level = queue.pop()
        if node:
            if level != prev_level:
                padding >>= 1
                print()
            print(f'{node!s: ^{2*padding}}', end='')
            queue.insert(0, (node.left, level+1))
            queue.insert(0, (node.right, level+1))
            prev_level = level
    print()