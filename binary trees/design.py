# Binary tree implementation
class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

class Tree:
    def __init__(self):
        self.root = None

    def new_node(self, data):
        node = Node(data)
        return node

    def find_last_node(self, node):
        ele = self.root
        adjacent_ele = None
        while ele:
            if not ele.left:
                pass
            elif not ele.right:
                pass
            els


    def insert(self, data):
        node = self.new_node(data)
        if self.root:
            if self.root.left is None:
                self.root.left = node
            elif self.root.right is None:
                self.root.right = node
            else:
                pass
        else:
            self.root = node
        return self.root

    def delete(self):
        pass

tree = Tree()