class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if self.key:
            if key<self.key:
                if self.left is None:
                    self.left = Node(key)
                else:
                    self.left.insert(key)
                    
            elif key>self.key:
               if self.right is None:
                   self.right = Node(key)
               else:
                    self.right.insert(key)
        else:
            self.key = key
            
    def print(self):
        if self.key:
            if self.left:
                self.left.print()
            print(self.key,end="->")
            if self.right:
                self.right.print()

def post(rootNode):
    if rootNode:
        print(rootNode.key, end="=")
        post(rootNode.left)
        post(rootNode.right)
        
            
                    

#Main
print("Input Menu")
print("\n[1]\tInput Numbers"
      +"\n[2]\tInput Letters")
choice = int(input("Choice: "))

haba = int(input("Enter the number nodes to input: "))

if choice == 1:
    root = int(input("Enter root node data: "))
    rootNode = Node(root)
    for i in range(haba-1):
        x = int(input("Enter node data to insert: "))
        rootNode.insert(x)

rootNode.print()
post(rootNode)


        
