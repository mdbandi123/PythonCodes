def menu():
    print("[1]\t Append a number")
    print("[2]\t Insert a number in desired position")
    print("[3]\t Delete an index")
    print("[4]\t Sum the list")
    print("[5]\t Count the number of times a certain number is in the list")
    print("[6]\t Display an index of the 1st position of a number")
    print("[7]\t Display the highest and lowest value in the list")
    print("[8]\t Sort the elements in Ascending Order")
    print("[9]\t Reverse the order of the element")
    print("[10]\t Remove the element")
    print("[11]\t Exit\n")

def option1(list1):
    print("Menu 1")
    newNum = int(input("Enter a number to add: "))
    list1.append(newNum)
    print("New list after adding: ",list1)

def option2(list1):
    print("Menu 2")
    newInd = int(input("Enter the index you want to insert value to: "))
    newNum = int(input("Enter the new value to insert: "))
    list1.insert(newInd,newNum)
    print("New list after inserting: ",list1)

def option3(list1):
    print("Menu 3")
    delInd = int(input("Enter the index you want to delete: "))
    del list1[delInd]
    print("New list after deleting: ",list1)

def option4(list1):
    print("Menu 4")
    total = 0
    for i in list1:
        total += i
    print("The sum of the elements: ",total)

def option5(list1):
    print("Menu 5")
    countNum = int(input("Enter the number you want to count: "))
    print("The number of",countNum,"in the list is:",list1.count(countNum))

def option6(list1):
    print("Menu 6")
    element = int(input("Enter the element you want to display the index of: "))
    print(element,"is in index",list1.index(element))

def option7(list1):
    print("Menu 7")
    print("List contains:",list1)
    print("The highest value is", max(list1))
    print("The lowest value is", min(list1))

def option8(list1):
    print("Menu 8")
    list1.sort()
    print("Sorted list:", list1)

def option9(list1):
    print("Menu 9")
    list1.reverse()
    print("Reversed list:", list1)

def option10(list1):
    print("Menu 10")
    remNum = int(input("Enter the element you want to remove: "))
    list1.remove(remNum)
    print("New list after removing:", list1)
    
#Main
repeater = "Y"
listMain = [0]*10; x=0
menu()
for i in listMain:
    val = int(input("Enter a number: "))
    listMain[x] = val
    x += 1
print("Original List: ",listMain)

while repeater == "Y":
    choice = int(input("\nEnter Choice: "))
    if choice == 1:
        option1(listMain)
    elif choice == 2:
        option2(listMain)
    elif choice == 3:
        option3(listMain)
    elif choice == 4:
        option4(listMain)
    elif choice == 5:
        option5(listMain)
    elif choice == 6:
        option6(listMain)
    elif choice == 7:
        option7(listMain)
    elif choice == 8:
        option8(listMain)
    elif choice == 9:
        option9(listMain)
    elif choice == 10:
        option10(listMain)
    elif choice == 11:
        print("Program Exit")
        exit()
    else:
        print("Invalid Input")

    repeater = input("Try Again? [Y/N]: ").upper()

    

              
    

    
    

