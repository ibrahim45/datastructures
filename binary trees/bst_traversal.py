# author: Ibrahimsha
# Theme : BST - Post order Traversal

class Node:
    def __init__(self, data, right=None, left= None):
        self.data = data
        self.right = right
        self.left = left
    
class BST:
    def __init__(self):
        self.root = None
        self.count = 0
        self.height = 0
        self.min = None
        self.max = None
        self.pre_traversal = [] # CLR
        self.post_traversal = [] # LRC
        self.inorder_traversal = [] # LCR --> gives acending order
        self.inorder_traversal_opp = [] # RCL --> gives descending order
    
    def create_node_obj(self, data):
        return Node(data)
    
    def add_nodes_to_tree(self, ele, node):
        if ele.data >= node.data:
            if ele.left is None:
                ele.left = node
                return;
            else:
                ele = ele.left
        else:
            if ele.right is None:
                ele.right = node
                return;
            else:
                ele = ele.right
        return 1

    def insert(self, data):
        node = self.create_node_obj(data)
        if self.root is None:
            self.root = node
            break;
        else:
             self.add_nodes_to_tree(self.root, node)
        self.count += 1
        print("Node is attached to tree")
        
    def get_max(self, ele):
        return ele.data if ele.right is None else self.get_max(ele.right)
       
    def get_min(self, ele):
        return ele.data if ele.left is None else self.get_min(ele.left)
 
    def order_traversal(self, ele):
        #CLR
        self.pre_traversal.append(ele.data)
        if ele.left:
            self.order_traversal(ele.left)
        if ele.right:
            self.order_traversal(ele.right)

    def in_order_traversal(self, ele):
        #LCR
        if ele.left:
            self.in_order_traversal(ele.left)
        self.inorder_traversal.append(ele.data)
        if ele.right:
            self.in_order_traversal(ele.right)
            
    def in_order_traversal_opp(self, ele):
        #LCR
        if ele.left:
            self.in_order_traversal_opp(ele.left)
        self.inorder_traversal_opp.append(ele.data)
        if ele.right:
            self.in_order_traversal_opp(ele.right)
            
    def post_order_traversal(self, ele):
        #LCR
        if ele.left:
            self.post_order_traversal(ele.left)
        self.post_traversal.append(ele.data)
        if ele.right:
            self.post_order_traversal(ele.right)
            

    def search(self):
        pass
        
    def delete(self):
        pass
