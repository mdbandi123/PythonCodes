class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        temp = self.head
        while (temp.next):
            temp = temp.next
        temp.next = Node(data)

    def print(self):
        temp = self.head
        print("\nThe linked list original order: ")
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

    def printRev(self):
        revArr=[]
        temp = self.head
        while(temp):
            revArr.append(temp.data)
            temp = temp.next

        revArr.reverse()
        print("\nThe linked list in reverse order: ")
        for i in revArr:
            print(i, end=" ")

#Main
looper = "Y"
while looper == "Y":
    linkedlist = LinkedList()
    listLen = int(input("\nEnter the no of elements for Linked List: "))

    headVal = int(input("Enter data in linked list: "))
    linkedlist.head = Node(headVal)
    for i in range(listLen-1):
        ext = int(input("Enter data in linked list: "))
        linkedlist.insert(ext)
    linkedlist.print()
    linkedlist.printRev()
    looper = input("\nDo you want to try again? [Y]: ").upper()

#Sumang, Michael Dave C. WD-202
        
        
                  
    
