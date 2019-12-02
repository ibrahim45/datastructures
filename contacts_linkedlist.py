class Node:
    def __init__(self, first_name, last_name=None):
        # print("Initializing contact node...")
        self.first_name = first_name
        self.last_name = last_name
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.elements = []
        self.size = 0
    
    def insert(self, contact_name):
        # insert a new node
        node = Node(contact_name)
        if self.head is None:
            # print("Inserting head node in linked list")
            self.head = node
            self.elements.append(self.head)
            self.size += 1
        else:
            # print("Inserting new node in linked list")
            self.elements[self.size-1].next = node
            self.elements.append(node) 
            self.size += 1

    def remove(self):
        print("Removing an node")
        self.elements[self.size-2].next = None      
        self.tail = self.elements[self.size-2]
        self.elements.pop()
        self.size -= 1

    def print_output(self):
        cursor_node = self.head   
        while cursor_node.next is not None:
            print("Current Node - {0}".format(cursor_node.first_name))
            # print(cursor_node.__dict__)
            next_node = cursor_node.next
            cursor_node = next_node
            # print("Next Node - {0}".format(cursor_node.__dict__))

        print("Last Node -{0}".format(cursor_node.first_name))

ll = LinkedList()
ll.insert("Aswin")
ll.insert("Siva")
ll.insert("Ranjith")
ll.print_output()
ll.remove()
ll.remove()
ll.remove()
ll.remove()
ll.print_output()

# # load contacts
# contacts = ['Aswin', 'Siva', 'Ranjith']
# for contact_name in contacts:
#     node = Node(contact_name)
#     print(node.first_name)


