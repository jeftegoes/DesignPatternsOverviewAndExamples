from node import Node


def traverse_in_order(root):
    def traverse(current):
        if current.left:
            for left in traverse(current.left):
                yield left
        yield current

        if current.right:
            for right in traverse(current.right):
                yield right

    for node in traverse(root):
        yield node



if __name__ == '__main__':
    #   1
    #  / \
    # 2   3

    # in-order: 213
    # preorder: 123
    # postorder: 231
    root = Node(1, Node(2), Node(3))

    it = iter(root)

    print([next(it).value for x in range(3)])

    for x in root:
        print(x.value)

    for y in traverse_in_order(root):
        print(y.value)