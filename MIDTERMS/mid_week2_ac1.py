#Binary Tree

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data,end="->")
        if self.right:
            self.right.PrintTree()

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data> self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findval(self,key_find):
        if key_find < self.data:
            if self.left is None:
                return str(key_find)+" Not Found"
            return self.left.findval(key_find)
        elif key_find > self.data:
            if self.right is None:
                return str(key_find)+" Not Found"
            return self.right.findval(key_find)
        else:
            return str(self.data)+" is found"

#Main
##a1 = input("Enter node data: ")
root = Node('7')
##ans = "Y"
##while ans == "Y":
##    b1 = input("Enter node data: ")
##    root.insert(b1)
##    ans = input("Do you want to insert again? [Y/N]: ").upper()
root.insert('5')
root.insert('22')
root.insert('33')
root.insert('18')
root.insert('3')
root.insert('10')
root.insert('-1')



print("Binary Tree Contains: ")
root.PrintTree()
print("")
##print(root.findval("lem"))
