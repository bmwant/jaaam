from typing import List, Optional, TypeVar

from tree import Node, print_tree
from invert_binary_tree import generate_tree_inner


def invert_queue(node: Node) -> Node:
    flatten = []
    queue = [node, 0]
    # push with desired order
    while queue:
        node = queue.pop()
        if node:
            flatten.append(node)
            queue.insert(0, node.right)
            queue.insert(0, node.left)
    # expand into tree
    print(flatten)
    while flatten:
        right = flatten.pop()
        left = flatten.pop()
    return flatten


if __name__ == '__main__':
    tree = generate_tree_inner(Node(), 2)
    print_tree(tree)
    invert_queue(tree)
