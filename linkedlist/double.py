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
        cursor_node = Node(ele.data)
        while ele:
            cursor_node.prev = Node(ele.next.data)
            if cursor_node.next is None:
                cursor_node.next = ele.prev
            ele = ele.next
            if ele.next:
                prev_node = cursor_node.prev
                prev_node.next = cursor_node
                cursor_node = prev_node
            else:
                prev_node = cursor_node.prev
                prev_node.next = cursor_node
                cursor_node = prev_node
                
                break;
        return cursor_node

    def view_list(self, head):
        ele = head
        while ele.next:
            print(ele.data)
            ele = ele.next
        print(ele.data)

    def reverse_head1(self, head):
        if head is None:
            return None
        curr = None
        while head:
            curr = head
            curr.next, curr.prev = head.prev, head.next
            head = head.next
            curr.next = head
        return curr

dll = DLL()
dll.insert(5)
dll.insert(6)
dll.insert(7)
dll.insert(8)

dll.view_list(dll.head)
rev_head = dll.reverse_head1(dll.head)
dll.view_list(rev_head)

