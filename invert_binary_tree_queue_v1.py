from typing import List, Optional, TypeVar
from enum import Enum, auto
from dataclasses import dataclass

from tree import Node
from invert_binary_tree import generate_tree_inner


def invert_stack(node: Node) -> Node:
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


@dataclass
class Arg(object):
    node: Node
    level: int = 0

class Action(Enum):
    TRAVERSE = auto()
    PRINT = auto()


def print_tree_stack(node: Node):
    stack = [(Action.TRAVERSE, Arg(node=node, level=0))]
    while stack:
        action, arg = stack.pop()
        node = arg.node
        level = arg.level
        if node is None:
            continue
        if action == Action.TRAVERSE:
            stack.append((Action.TRAVERSE, Arg(node=node.left, level=level+1)))
            stack.append((Action.PRINT, Arg(node=node, level=level)))
            stack.append((Action.TRAVERSE, Arg(node=node.right, level=level+1)))
        elif action == Action.PRINT:
            print('  ' * level, end='')
            print(node)
        else:
            raise ValueError(f'Encountered improper action: {action}')


if __name__ == '__main__':
    tree = generate_tree_inner(Node(), 2)
    print('Initial tree')
    print_tree_stack(tree)
    # inverted = invert_stack(tree)
    # print('Inverted tree')
    # print_tree(inverted)
