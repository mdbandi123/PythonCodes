class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.node = data

def PreOrder(root):
    if root:
        print(root.node, end = "-")
        PreOrder(root.left)
        PreOrder(root.right)

def InOrder(root):
    if root:
        InOrder(root.left)
        print(root.node, end = "-")
        InOrder(root.right)

def PostOrder(root):
    if root:
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.node, end = "-")

#main
root = Node(10)
root.left = Node(5)
root.left.left = Node(2)
root.left.right = Node(8)
root.right = Node(14)
root.right.left = Node(12)
root.right.right = Node(16)
print()
print("PreOrder Traversal: ")
PreOrder(root)
print()
print("InOrder Traversal: ")
InOrder(root)
print()
print("PostOrder Traversal: ")
PostOrder(root)
