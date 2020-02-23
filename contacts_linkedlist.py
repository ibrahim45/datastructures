class Node:
    def __init__(self, first_name, last_name, phone_number):
        # print("Initializing contact node...")
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.elements = []
        self.size = 0
    
    def insert(self, contact_fname, contact_lname, phone_number):
        # insert a new node
        node = Node(contact_fname, contact_lname, phone_number)
        if self.head is None:
            # print("Inserting head node in linked list")
            self.head = node
            self.elements.append(node)
            self.size += 1
        else:
            # print("Inserting new node in linked list")
            self.elements[self.size-1].next = node
            self.elements.append(node) 
            self.size += 1

    def remove(self):
        try:
            print("Removing an node")
            self.elements[self.size-2].next = None      
            self.tail = self.elements[self.size-2]
            print("Removed node is - {0}".format(self.elements[self.size-1].__dict__))
            self.elements.pop()
            self.size -= 1
        except IndexError:
            print(len(self.elements))
            self.head = None

    def print_output(self):
        cursor_node = self.head   
        if cursor_node is not None:
            while cursor_node.next is not None:
                print("Current Node - {0}".format(cursor_node.first_name))
                # print(cursor_node.__dict__)
                next_node = cursor_node.next
                cursor_node = next_node
                # print("Next Node - {0}".format(cursor_node.__dict__))

            print("Last Node -{0}".format(cursor_node.first_name))
            # print("Head Node Value is - {0}".format(self.head.__dict__))
            # print("Tail Node Value is - {0}".format(self.tail.__dict__))
        else:
            print("Linked List is empty")

    def search_element(self, search_name):
        cursor_node = self.head
        while cursor_node.next != None:
            cursor_node = cursor_node.next
            if cursor_node.first_name == search_name:
                return cursor_node.__dict__
        return "Contact name does n't exist in linked list"

    def check_element_exists(self, search_name):
        cursor_node = self.head
        while cursor_node.next != None:
            cursor_node = cursor_node.next
            if cursor_node.first_name == search_name:
                return cursor_node
        return None

    def insert_before(self, x, y):
        if check_element_exists(x) and check_element_exists(y):
            x_node = check_element_exists(x)
            y_node = check_element_exists(y)
            temp_node = None
            if 

        else:
            print("Given name-{0}, -{1} does n't exist".format(x, y))

        
    
    def remove_before(self):
        pass

ll = LinkedList()
ll.insert("Aswin", "Gurusamy", "123456789")
ll.insert("Siva", "chandran", "234567891")
ll.insert("Ranjith", "Manickam", "345678912")
ll.insert("Karthick", "Indh", "456789123")
ll.print_output()

print("Search an element")
print(ll.search_element("Siva"))

print("swap an linked list")
# Before Swap: Aswin->Siva->Ranjith->Karthick 
# After Swap: Aswin->-Karthick->Siva->Ranjith
# After Swap: Aswin->-Karthick->Ranjith->Siva

ll.insert_before("Siva", "Karthick")



# ll.remove()
# ll.remove()
# ll.remove()
# ll.remove()
# ll.print_output()

# # load contacts
# contacts = ['Aswin', 'Siva', 'Ranjith']
# for contact_name in contacts:
#     node = Node(contact_name)
#     print(node.first_name)


