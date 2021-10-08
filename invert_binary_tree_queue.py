from typing import List, Optional, TypeVar

from tree import Node, print_tree
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


def print_tree_queue(root: Node):
    queue = [(root, 0)]
    while queue:
        node, level = queue.pop()
        if node:
            print('   ' * (level-1), end='')
            print(f'└──{node}') if level else print(node)
            queue.insert(0, (node.left, level+1))
            queue.insert(0, (node.right, level+1))


T = TypeVar('T')


def _get(array: List[T], index: int) -> Optional[T]:
    try:
        return array[index]
    except IndexError:
        pass


def expand_into_tree(elems: List[int]) -> Node:
    queue = []
    counter = 0
    root = Node(elems[counter])
    queue.append(root)
    while queue:
        node = queue.pop()
        if left_elem := _get(elems, counter+1):
            left = Node(left_elem)
            node.left = left
            queue.insert(0, left)
            counter += 1

        if right_elem := _get(elems, counter+1):
            right = Node(right_elem)
            node.right = right
            queue.insert(0, right)
            counter +=1

    return root


def _invert_queue(node: Node) -> List[int]:
    flatten = []
    queue = [node, 0]
    while queue:
        node = queue.pop()
        if node:
            flatten.append(node)
            queue.insert(0, node.right)
            queue.insert(0, node.left)
    return flatten


def invert_tree_queue(root: Node) -> Node:
    inverted_elems = _invert_queue(root)
    return expand_into_tree(inverted_elems)


if __name__ == '__main__':
    elems = [1, 2, 5, 3, 4, 6, 7]
    # tree = generate_tree_inner(Node(), 2)
    # print_tree_stack2(tree)
    tree = expand_into_tree(elems)
    print('Initial tree')
    print_tree(tree)

    print('Inverted tree')
    inverted = invert_tree_queue(tree)
    print_tree(inverted)
