from typing import Optional

from tree import Node, print_tree


class GenTreeClass(object):
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


class GenTreeInstance(object):
    def __init__(self):
        self.counter = 0

    def reset(self):
        self.counter = 0

    def generate(self, levels: int) -> Optional[Node]:
        if levels:
            self.counter += 1
            node = Node(self.counter)
            node.left = self.generate(levels-1)
            node.right = self.generate(levels-1)
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



def test_gen_tree_class():
    generator = GenTreeClass()
    tree1 = generator.generate(levels=3)
    print(f'Counter between calls {GenTreeClass.counter}')
    tree2 = generator.generate(levels=2)
    print('First tree')
    print_tree(tree1)
    print('Second tree')
    print_tree(tree2)
    print(f'Counter in the end {GenTreeClass.counter}')


def test_gen_tree_instance():
    generator = GenTreeInstance()
    tree1 = generator.generate(levels=3)
    generator.reset()
    tree2 = generator.generate(levels=2)
    print('First tree')
    print_tree(tree1)
    print('Second tree')
    print_tree(tree2)


if __name__ == '__main__':
    # test_gen_tree_class()
    test_gen_tree_instance()
