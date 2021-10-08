class Node(object):
    def __init__(self, value: int = None):
        self.value = value
        self.left: Node = None
        self.right: Node = None

    def __str__(self):
        return f'{self.value}'


def print_tree(root: Node, level: int = 0):
    if root is None:
        return
    print_tree(root.right, level+1)
    print('  ' * level, end='')
    print(root)
    print_tree(root.left, level+1)
