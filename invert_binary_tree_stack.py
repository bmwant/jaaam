from enum import Enum, auto
from dataclasses import dataclass

from tree import Node
from invert_binary_tree import generate_tree_inner


@dataclass(kw_only=True)
class Arg(object):
    node: Node
    level: int = 0


class Action(Enum):
    TRAVERSE = auto()
    PRINT = auto()
    SWAP = auto()


def invert_tree_stack(node: Node) -> Node:
    stack = [(Action.TRAVERSE, Arg(node=node))]
    root = node
    while stack:
        action, arg = stack.pop()
        node = arg.node
        if node is None:
            continue

        match action:
            case Action.TRAVERSE:
                stack.append((Action.TRAVERSE, Arg(node=node.left)))
                stack.append((Action.TRAVERSE, Arg(node=node.right)))
                stack.append((Action.SWAP, Arg(node=node)))
            case Action.SWAP:
                tmp = node.left
                node.left = node.right
                node.right = tmp
            case _:
                raise ValueError(f'Invalid action: {action}')
    return root


def print_tree_stack(node: Node):
    stack = [(Action.TRAVERSE, Arg(node=node, level=0))]
    while stack:
        action, arg = stack.pop()
        node = arg.node
        level = arg.level
        if node is None:
            continue
        
        match action:
            case Action.TRAVERSE:
                stack.append((Action.TRAVERSE, Arg(node=node.left, level=level+1)))
                stack.append((Action.PRINT, Arg(node=node, level=level)))
                stack.append((Action.TRAVERSE, Arg(node=node.right, level=level+1)))
            case Action.PRINT:
                print('  ' * level, end='')
                print(node)
            case _:
                raise ValueError(f'Encountered improper action: {action}')


if __name__ == '__main__':
    tree = generate_tree_inner(Node(), 2)
    print('Initial tree')
    print_tree_stack(tree)
    inverted = invert_tree_stack(tree)
    print('Inverted tree')
    print_tree_stack(inverted)
