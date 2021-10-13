from tree import Node, print_tree_horizontal
from invert_binary_tree import generate_tree_inner


def main():
    print('-' * 64)  # 64 in dec
    tree1 = generate_tree_inner(Node(), 2)
    print_tree_horizontal(tree1)

    print('-' * 0o100)  # 64 in oct
    tree2 = generate_tree_inner(Node(), 3)
    print_tree_horizontal(tree2)

    print('-' * 0x40)  # 64 in hex
    tree3 = generate_tree_inner(Node(), 4)
    print_tree_horizontal(tree3)

    print('-' * 0b1000000)  # 64 in bin


if __name__ == '__main__':
    main()