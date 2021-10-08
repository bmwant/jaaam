from typing import Optional

from tree import Node
from invert_binary_tree import generate_tree_inner


def print_tree_stack(root: Node):
    stack = [(root, 0)]
    while stack:
        node, level = stack.pop()
        if node:
            print('   ' * (level-1), end='')
            print(f'└──{node}') if level else print(node)
            stack.append((node.right, level+1))
            stack.append((node.left, level+1))


if __name__ == '__main__':
    tree = generate_tree_inner(Node(), 2)
    print_tree_stack(tree)
