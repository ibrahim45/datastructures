# author : ibrahim

import copy

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size =  0

    def create_node(self, val):
        node = Node(val)
        return node
    
    def pick_ele_neighbourhoods(self, pos_val):
        ele = self.head 
        pos = 1
        next_ele = self.head.next
        prev_ele = None

        while ele:
            if pos == pos_val:
                break; 
            if ele.next:
                prev_ele = ele
                ele = ele.next
                next_ele = ele.next
                pos += 1
            else:
                print("Position does n't exists in list")
                break;

        return ele

    def insert(self, val):
        for data_val in val:
            node = self.create_node(data_val)
            if self.head:
                if self.head.next is None:
                    self.tail = node
                    self.head.next = self.tail
                else:
                    self.tail.next = node
                    self.tail = node
            else:
                self.head = node
            self.size += 1 
    
    def insert_before_head(self, val):
        """
        insert_before_head
        """
        if self.head:
            node = self.create_node(val)
            temp_head = self.head
            self.head = node
            self.head.next = temp_head
            self.size += 1
        else:
            self.insert([val])

    def insert_before_tail(self, val):
        """
        insert_before_tail
        """
        if self.tail:
            node = self.create_node(val)
            ele = self.head
            prev_ele = None
            while ele.next:
                prev_ele = ele
                ele = ele.next
            prev_ele.next = node
            prev_ele.next.next = self.tail
        else:
            self.insert([val])

    def delete_at_position(self, pos_val):
        ele = self.head 
        pos = ele.data
        next_ele = self.head.next
        prev_ele = None

        while ele:
            if pos == pos_val:
                if prev_ele is None:
                    self.head = next_ele
                elif next_ele is None:
                    prev_ele.next = None
                    self.tail = prev_ele
                else:
                    prev_ele.next = next_ele
                break;
            if ele.next:
                prev_ele = ele
                ele = ele.next
                next_ele = ele.next
                pos = ele.data
            else:
                print("Position does n't exists in list")
                break;
            
    def search(self, val):
        ele = self.head
        pos = 1
        while ele:
            if ele.data == val:
                print("Value exists in position {}".format(pos))
                break;
            if ele.next is None:
                print("value does n't exists")
                break;
            ele = ele.next
            pos += 1

    def join_nodes(self, prev_ele, next_ele, ele):
        new_ele = copy.deepcopy(ele)
        new_ele.next = next_ele
        if next_ele is None:
            self.tail = new_ele
        if prev_ele is None:
            self.head = new_ele
        else:
            prev_ele.next = new_ele

    def swap_position(self, right_pos, left_pos):
        right_ele = self.pick_ele_neighbourhoods(right_pos)
        left_ele = self.pick_ele_neighbourhoods(left_pos)
        if right_pos == left_pos:
            print("right and left cant be the same position")
        else:
            ele = self.head
            prev_ele = None
            next_ele = self.head.next
            pos = 1
            while ele:
                if right_pos == pos:
                    self.join_nodes(prev_ele, next_ele, left_ele)
                elif left_pos == pos:
                    self.join_nodes(prev_ele, next_ele, right_ele)
                if ele.next:
                    prev_ele = ele
                    ele = ele.next
                    next_ele = ele.next
                    pos += 1
                else:
                    print("Position does n't exists in list")
                    break;

    def view_list(self):
        ele = self.head
        while ele.next:
            print(ele.data)
            ele = ele.next
        print(ele.data)


linkedlist = LinkedList()
linkedlist.insert([6, 7, 1, 2, 3])
linkedlist.insert_before_head(18)
linkedlist.view_list()

## insert before last element 
print("## insert before last element")
linkedlist.insert_before_tail(19)
linkedlist.view_list()

linkedlist.search(3)

print("## deleting first position")
linkedlist.delete_at_position(1)
linkedlist.delete_at_position(199)
linkedlist.delete_at_position(18)

print("Swap the element")
linkedlist.swap_position(1, 5)
linkedlist.view_list()
