class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    output = None
    if root.info is None:
        return None

    if root.info > v1:
        output = lca(root.left, v1, None)
    if not output:
        return output

    return root;




tree = BinarySearchTree()
t = "4, 2, 3, 1, 7, 6"

arr = t.split(",")

for i in range(len(arr)):
    tree.create(int(arr[i]))

# v = list(map(int, input().split()))
v1, v2 = 1, 7
ans = lca(tree.root, v1, v2)
print (ans.info)
