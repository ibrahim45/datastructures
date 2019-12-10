class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.elements = 
        self.tail = None
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
    
    def remove(self):
        new_node = Node()
        
    def print_output(self):
        print(self.head)
        print(self.size)


ll = LinkedList()

# insert a new node 5 Val
ll.insert(5)
ll.insert(6)
ll.insert(7)

ll.print_output()