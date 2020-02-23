# author : ibrahim

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def insert(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            if self.tail is None:
                self.head.next = node
                node.prev = self.head
                self.tail = node
            else:
                node.prev = self.tail
                self.tail.next = node
                node.next = None
                self.tail = node
        self.size += 1
        print("Node is inserted")

    def reverse_head(self, head):
        #TODO:
        ele = head
        while ele:
            node = Node(ele.data)
            node.prev = ele

        pass

    def view_list(self, head):
        ele = head
        while ele.next:
            print(ele.data)
            ele = ele.next
        print(ele.data)

dll = DLL()
dll.insert(5)
dll.insert(6)
dll.insert(7)
dll.insert(8)

dll.view_list(dll.head)

# reverse_list = dll.reverse_head(dll.head)
