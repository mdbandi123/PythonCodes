#Classes
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def list_Printer(self):
        temp = self.head
        print("\nCurrent Linked List Contains the Following: ")
        while(temp):
            print(temp.data, end="->")
            temp = temp.next

    def insert_Beginning(self, newData):
        nNode = Node(newData)
        nNode.next = self.head
        self.head = nNode

    def insert_Between(self, prevNode, newData):
        temp = self.head
        while(temp):
            if (prevNode == temp.data):
                nNode = Node(newData)
                nNode.next = temp.next
                temp.next = nNode
                return
            temp = temp.next

        print("\nPrevious node must be in the Linked List")
        return

    def insert_End(self, newData):
        nNode = Node(newData)
        if self.head is None:
            self.head = nNode
            return

        else:
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = nNode
            
    def del_Function(self, delNode):
        temp = self.head
        if (temp is not None):
            if (delNode == temp.data):
                self.head = temp.next
                temp = None
                return
            
            while(temp):
                if (delNode == temp.data):
                    prev.next = temp.next
                    return
                prev = temp
                temp = temp.next
                
        print("\nNode does not exist")
        return
        

#Non - Class Functions
def beginNodeInsert():
    newNodeVal = input("Enter value to insert at the beginning: ")
    llist.insert_Beginning(newNodeVal)

def betweenNodeInsert():
    curNode = input("Enter the node you want to insert your new node value after: ")
    newNodeVal = input("Enter value to insert after: ")
    llist.insert_Between(curNode, newNodeVal)

def endNodeInsert():
    newNodeVal = input("Enter value you want to insert at the end: ")
    llist.insert_End(newNodeVal)

def delNode():
    delNodeVal = input("Enter value you want to delete: ")
    llist.del_Function(delNodeVal)


    
#Main
llist = LinkedList()

looper = "Y"
while looper == "Y":
    print("\n\nLinked List Menu"
          +"\n[A] Insert new node value at Beginning"
          +"\n[B] Insert new node value Between 2 Nodes"
          +"\n[C] Insert new node value at End"
          +"\n[D] Delete Node"
          +"\n[E] Exit")
    choice = input("Enter Choice: ").upper()

    if choice == "A":
        beginNodeInsert()
        llist.list_Printer()

    elif choice == "B":
        betweenNodeInsert()
        llist.list_Printer()

    elif choice == "C":
        endNodeInsert()
        llist.list_Printer()

    elif choice == "D":
        delNode()
        llist.list_Printer()

    elif choice == "E":
        print("Exiting Program")
        break

    else:
        print("Invalid Choice")

    looper = input("\nDo you want to try again? [Y/N]: ").upper()

    
