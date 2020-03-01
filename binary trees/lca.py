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
    print(root.info)
    output = None
    if root.info is None:
        return None;
    
    if v1 > root.info and v2 > root.info:
        output = lca(root.right, v1, v2)

    if v1 < root.info and v2 < root.info:
        output = lca(root.left, v1, v2)


    if output and output.info in [v1,v2]:
        root = output
    return root;




tree = BinarySearchTree()
t = 8
a = "8, 4, 9, 1, 2, 3, 6, 5"
a = "8 6 5 7 11 12 13 10 9"
arr = list(map(int, a.split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, 9, 12)
print (ans.info)
