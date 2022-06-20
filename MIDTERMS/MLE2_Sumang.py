#Class - Func
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

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data,end="->")
        if self.right:
            self.right.printTree()

            
##### --Menu Functions--
    def search(self, data_find):
        if data_find < self.data:
            if self.left is None:
                return str(data_find)+" Not Found"
            return self.left.search(data_find)
        elif data_find > self.data:
            if self.right is None:
                return str(data_find)+" Not Found"
            return self.right.search(data_find)
        else:
            return str(self.data)+" is Found"

def PreOrder(root):
    if root:
        print(root.data, end = "->")
        PreOrder(root.left)
        PreOrder(root.right)

def InOrder(root):
    if root:
        InOrder(root.left)
        print(root.data, end = "=")
        InOrder(root.right)

def PostOrder(root):
    if root:
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.data, end = "*")

    

           
#Main
looperN = "Y"

x = input("Enter root node data: ")
rootNode = Node(x)
while looperN == "Y":
    childNode = input("Enter node data to insert: ")
    rootNode.insert(childNode)
    looperN = input("Do you want to enter another data? [Y/N]: ").upper()

print("\nBinary Tree contains the following: ")
rootNode.printTree()

looperMain = "Y"
while looperMain == "Y":
    print("\nMain Menu"+
          "\n[A]\tSearch a node"+
          "\n[B]\tDisplay PreOrder travesal of Binary Tree"+
          "\n[C]\tDisplay InOrder traversal of Binary Tree"+
          "\n[D]\tDisplay PostOrder traversal of Binary Tree"+
          "\n[E]\tEXIT")
    choice = input("Enter Choice: ").upper()

    if choice == "A":
        searchVal = input("\nEnter a data to search: ")
        print(rootNode.search(searchVal))

    elif choice == "B":
        print("\nPreOrder traversal of binary tree is")
        PreOrder(rootNode)
        print("")

    elif choice == "C":
        print("\nInOrder traversal of binary tree is")
        InOrder(rootNode)
        print("")

    elif choice == "D":
        print("\nPostOrder traversal of binary tree is")
        PostOrder(rootNode)
        print("")

    elif choice == "E":
        print("Exiting Program")
        break

    else:
        print("Invalid Choice")

    looperMain = input("Do you want to repeat the menu again? [Y/N]: ").upper()
        
        

