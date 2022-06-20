def stackFunction(s1):
    looper = "Y"
    while looper == "Y":
        print("\nStack Menu")
        choice = int(input("[1] Push Value"
                       +"\n[2] Pop Value"
                       +"\n[3] Stack Exit"
                       +"\nChoice: "))

        if choice == 1:
            x = input("Enter the value to add in stack: ")
            s1.append(x)
            print("Stack Contains: ")
            size = len(s1)
            for i in range(size-1,-1,-1):
                print(s1[i])

        elif choice == 2:
            y = s1.pop()
            print("Pop Value: "+y)
            print("Stack Contains After pop(): ")
            size = len(s1)
            for i in range(size-1,-1,-1):
                print(s1[i])

        elif choice == 3:
            print("RETURNING TO MAIN MENU")
            break

        else:
            print("Invalid Choice")

        looper = input("Do you want to try again [STACK MENU]? [Y/N]: ").upper()
        
    return s1

def queueFunction(q1):
    looper = "Y"
    while looper == "Y":
        print("\nQueue Menu")
        choice = int(input("[1] Enqueue Value"
                       +"\n[2] Dequeue Value"
                       +"\n[3] Queue Exit"
                       +"\nChoice: "))

        if choice == 1:
            x = input("Enter the value to enqueue: ")
            q1.append(x)
            print("Queue Contains: ")
            print(q1)

        elif choice == 2:
            y = q1.pop(0)
            print("Dequeue value: "+y)
            print("Queue Contains: ")
            print(q1)

        elif choice == 3:
            print("RETURNING TO MAIN MENU")
            break

        else:
            print("Invalid Choice")

        looper = input("Do you want to try again [QUEUE MENU]? [Y/N]: ").upper()
        
    return q1
            
        
              
        
#Main
s1 = []
q1 = []
looper = "Y"

while looper == "Y":
    print("\nMAIN MENU")
    choice = input("[A] Stacks"
                   +"\n[B] Queue"
                   +"\n[E] Exit"
                   +"\nChoice: ").upper()

    if choice == "A":
        s1 = stackFunction(s1)
        print(s1) #Remove Later

    elif choice == "B":
        queueFunction(q1)
        print(q1) #Remove Later

    elif choice == "E":
        print("EXITING THE PROGRAM")
        break

    else:
        print("INVALID CHOICE")

    looper = input("Do you want to try again? [Y/N]: ").upper()
