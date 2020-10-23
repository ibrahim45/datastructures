
class Node:
    def __init__(self, data):
        self.left, self.right = None, None
        self.data = data
        self.children = 0

    def ___print___(self):
        print("Node--data is {}, left pointer is {} and right pointer is {} ".format(
            self.data,
            self.left,
            self.right
        ))


def print_tree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.data)
        printTree(node.right, level + 1)

class BinaryTree:

    def __init__(self):
        self.root = None



