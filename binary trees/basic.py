# author : ibrahimsha
# Theme:  basic iplementation of binary tree
import sys

pipe  = "|"
minus  = " -"
connector  = "|_"

class Node:
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left

class Tree:

    def __init__(self):
        self.root = None
        self.count = 0

    def count(self):
        return self.count

    def new_node(self, data, right=None, left=None):
        node = Node(data, right, left)
        self.count += 1
        return node

    def add_node_in_subtree(self, root, node):
        ele = root
        while ele:
            if ele.data >= node.data:
                if ele.left:
                    ele = ele.left
                else:
                    ele.left = node
                    print("Child Left Node created sucessfully...")
                    return;
            else:
                if ele.right:
                    ele = ele.right
                else:
                    ele.right = node
                    print("Child Right Node created sucessfully...")
                    return;

    def insert(self, data):
        node = self.new_node(data)
        if not self.root:
            self.root = node
            print("Root Node created successfully...")
        else:
            result = self.add_node_in_subtree(self.root, node)
            print("All child nodes created successfully..")


    def delete(self):
        pass

    def search(self):
        pass

    def access(self):
        pass

    # def print_format(self):
    #     ele = self.root
    #     counter = 1
    #     while ele:
    #         if ele.left:
    #             print(pipe)
    #             print(connector + counter * minus + " " + str(ele.left.data))
    #             ele = ele.left
    #         elif ele.right:
    #             print(pipe)
    #             minusval = counter * minus
    #             print(connector + minusval + " " + str(ele.right.data))
    #             ele = ele.right
    #     sys.exit()

    def print_output(self, root):
        ele = root
        while ele:
            print(ele.data)
            if ele.left:
                # print(ele.left.data)
                self.print_output(ele.left)
            if ele.right:
                # print(ele.right.data)
                self.print_output(ele.right)
            break;

    def get_height(self, ele):
        if ele is None:
            return -1
        return max(self.get_height(ele.left), self.get_height(ele.right)) + 1

    def get_min(self, ele):
        if ele is None:
            return -1
        return min(self.get_height(ele.left), self.get_height(ele.right))



tree = Tree()
tree.insert(4)
tree.insert(2)
tree.insert(5)
tree.insert(1)
tree.insert(3)
# tree.print_format() # TODO: Need to be done
tree.print_output(tree.root)
print("height of node is  {0}".format(tree.get_height(tree.root)))
print("min val of node is  {0}".format(tree.get_height(tree.root)))







