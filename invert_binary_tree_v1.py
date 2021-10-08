from typing import Optional

from tree import Node, print_tree


class GenTree(object):
    counter = 0

    @classmethod
    def _generate(cls, levels: int) -> Optional[Node]:
        if levels == 0:
            return None

        cls.counter += 1
        node = Node(cls.counter)
        node.left = cls._generate(levels-1)
        node.right = cls._generate(levels-1)
        return node

    def generate(self, levels: int) -> Optional[Node]:
        cls = self.__class__
        node = cls._generate(levels)
        # NOTE: reset counter for further invocations
        cls.counter = 0
        return node


counter = 0
def generate_tree(levels: int) -> Optional[Node]:
    global counter
    if levels == 0:
        return None

    counter += 1
    node = Node(counter)
    node.left = generate_tree(levels-1)
    node.right = generate_tree(levels-1)
    return node


if __name__ == '__main__':
    generator = GenTree()
    tree1 = generator.generate(levels=3)
    print(f'Counter between calls {GenTree.counter}')
    tree2 = generator.generate(levels=2)
    print('First tree')
    print_tree(tree1)
    print('Second tree')
    print_tree(tree2)
    print(f'Counter in the end {GenTree.counter}')
