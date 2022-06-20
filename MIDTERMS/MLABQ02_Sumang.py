class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    def print(self):
        if self.left:
            self.left.print()
        print(self.data,end="->")
        if self.right:
            self.right.print()

def preOrder(root):
    if root:
        print(root.data, end = "->")
        preOrder(root.left)
        preOrder(root.right)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end = "=")
        inOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end = "*")

        
                
#Sumang, Michael Dave C. WD-202
#Main
print("[1]\tInput Numbers for Nodes")
print("[2]\tInput Letters for Nodes")
choice = int(input("\nEnter choice: "))
length = int(input("Enter number of nodes to input: "))

if choice == 1:
    print("\nNumber input")
    y = int(input("Enter root node: "))
    root = Node(y)
    for i in range(length-1):
        z = int(input("Enter node data to insert: "))
        root.insert(z)
    print("Number Binary Tree contains the following: ")
        
elif choice == 2:
    print("\nLetter input")
    y = input("Enter root node: ")
    root = Node(y)
    for i in range(length-1):
        z = input("Enter node data to insert: ")
        root.insert(z)
    print("Letter Binary Tree contains the following: ")

root.print()

looper = "Y"
while looper == "Y":
    print("\n\nTraversal Menu: ")
    print("[A] Display PreOrder traversal Binary Tree")
    print("[B] Display InOrder traversal Binary Tree")
    print("[C] Display PostOrder traversal Binary Tree")
    print("[E] EXIT")

    choice2 = input("Enter Choice: ").upper()

    if choice2 == "A":
        print("\nPreOrder: ")
        preOrder(root)

    elif choice2 == "B":
        print("\nInOrder: ")
        inOrder(root)

    elif choice2 == "C":
        postOrder(root)

    elif choice2 == "E":
        print("\nPostOrder: ")
        print("exiting")
        break

    else:
        print("\nInvalid Choice")

    looper = input("\nDo you want to try again? [Y]: ").upper()

    
#Sumang, Michael Dave C. WD-202        

             
