class Node:
    def __init__(self, reference_val, pointer_val=None):
        self.reference = reference_val
        self.pointer = pointer_val


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, person_name):
        if self.head is None:
            node = Node(person_name)
            self.length += 1
            self.head = node
            print("Linked List _ head node is created in the name of {0}".format(person_name))
        else:
            # TODO : Insert a new node...


    def pop(self):
        pass

    def print_output(self):
        print("SMart Work")

ll = LinkedList()
ll.push("Kasim")
