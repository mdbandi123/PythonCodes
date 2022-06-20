#Linked List

class Node:
    def __init__(self, data = None): #None is not required but represents and initialized empty value
        self.data = data #Value or data stored in the node
        self.next = None #Reference to the next node, null for last node
        
class SLinkedList:
    def __init__(self):
        self.head = None

    def printList(self): #Prints contents of linked list
        temp = self.head
        while (temp):
            print(temp.data, end="->")
            temp = temp.next

    def Begin(self, newData): #Assigns a node at the beginning
        nNode = Node(newData)
        nNode.next = self.head
        self.head = nNode

    def After(self, prevNode, newData): #Assigns node at a specified place
        if prevNode is None:
            print("Previous node must be in the Linked List")
            return
        nNode = Node(newData)
        nNode.next = prevNode.next
        prevNode.next = nNode

    def End(self, newData):#Assigns a node at the ending 
        nNode = Node(newData)
        if self.head is None: #checks if empty
            self.head = nNode
            return

        else:
            last = self.head
            while (last.next): #Looks for the last node
                last = last.next
            last.next = nNode

    def Delete(self, key):
        temp = self.head #Assigns the head value (start value) of the linked list
        if (temp is not None):
            if temp.data==key: #the key is in the linked list temp var
                self.head = temp.next
                temp = None
                return
            #Code up until here if the node to be deleted is the head

        while (temp is not None): #If node to be deleted is after the last node
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if (temp == None):
            print("\nNode does not exist")
            exit()
            return

        prev.next = temp.next
        

        
        
#Main
llist = SLinkedList()
llist.head = Node(11)
e2 = Node(22)
e3 = Node(33)

#Link first Node to second node
llist.head.next = e2

#Link second node to third node
e2.next = e3

print("linked list: ")
llist.printList()

llist.Begin(44)
print("\nlinked list after insertion at start: ")
llist.printList()

llist.After(e2, 55)
print("\nlinked list after insertion at specific node: ")
llist.printList()

llist.End(77)
print("\nlinked list after insertion at end: ")
llist.printList()


print("\nlinked list before deletion: ")
llist.printList()
llist.Delete(55)
print("\nlinked after before deletion: ")
llist.printList()



