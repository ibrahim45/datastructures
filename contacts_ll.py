class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.elements = []
        self.size = 0
    
    def insert(self, val):
        new_node = Node(val)
        self.size += 1 
        if self.head is None:
            self.head = new_node
        else:
            if self.tail is None:
                self.head.next = new_node
                self.tail = new_node
            else:
                previous_node = self.tail
                self.tail = new_node 
                previous_node.next = self.tail
                self.head.next = previous_node
    

