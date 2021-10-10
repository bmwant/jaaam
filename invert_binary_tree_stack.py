from typing import List, Optional, TypeVar
from enum import Enum, auto
from dataclasses import dataclass

from tree import Node
from invert_binary_tree import generate_tree_inner


@dataclass
class Arg(object):
    node: Node
    level: int = 0

class Action(Enum):
    TRAVERSE = auto()
    PRINT = auto()


def invert_stack(node: Node) -> Node:
    stack = []
    return node


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
    inverted = invert_stack(tree)
    print('Inverted tree')
    print_tree_stack(inverted)
