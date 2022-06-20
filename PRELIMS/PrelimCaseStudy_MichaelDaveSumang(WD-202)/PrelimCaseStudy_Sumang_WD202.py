def pleOne():
    def menu1():
        print("\nPLE 1")
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
    
    #PLE1 Main
    looper1 = "Y"
    listMain = [0]*10; x=0
    menu1()
    for i in listMain:
        val = int(input("Enter a number: "))
        listMain[x] = val
        x += 1
    print("Original List: ",listMain)

    while looper1 == "Y":
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
            break;
        else:
            print("Invalid Input")

        looper1 = input("Try Again? [Y/N]: ").upper()
        
def pleTwo1():
    def words():
        wordFile = open('word.txt', 'r')
        wordVar = wordFile.read()
        print(wordVar + "\n")
        x = wordVar.replace('"', '')
        x = x.replace("'s", '')
        z = x.split()
        wordFile.close()
        return z

    #PLE 2 - 1 Main
    looper2 = "Y"
    while looper2 == "Y":
        print()
        doubleWord = set()
        perWord = words()
        for i in perWord:
            if i.isalpha():
                checker = i.lower()
                if not(checker in doubleWord):
                    print(checker+" "+str(perWord.count(i)).lower())
                    doubleWord.add(checker)
        looper2 = input("Try again? [Y/N]: ").upper()


def pleTwo2():
    def append():
        nameFile = open("names.txt", "a")
        name = input("Enter name in file: ")
        nameFile.write(name+"\n")
        nameFile.close()

    def read():
        nameFile = open("names.txt", "r")
        print("The file contains the following: ")
        i = nameFile.readline()
        while i != '':
            print(i)
            i = nameFile.readline()
        nameFile.close()

    def write():
        nameFile = open("names.txt", "w")
        name = input("Enter name in file: ")
        nameFile.write(name+"\n")
        nameFile.close()
        
    #PLE2 - 2Main
    looper22 = "Y"
    while looper22 == "Y":
        print("Menu\n"
              +"[A] Append data on the file\n"
              +"[R] Read data on the file\n"
              +"[W] Write data on the file\n"
              +"[E] Exit\n")
        choice = input("\nEnter choice: ").lower()
        if choice == "a":
            append()
        elif choice == "r":
            read()
        elif choice == "w":
            write()
        elif choice == "e":
            print("Program Exit")
            break
        else:
            print("Invalid Choice")
        looper22 = input("Try again? [Y/N]: ").upper()

def pleTwo3():
    #PLE2 - 3 Main
    salesFile = open("sales.txt", "r")
    salesTotal = 0; counter = 0

    print("List of sales in Php:")
    valHolder = salesFile.readline()
    while valHolder != "":
        salesPhp = float(valHolder.rstrip("\n"))
        salesTotal += salesPhp
        counter += 1
        valHolder = salesFile.readline()
        print("Day",counter,":",format(salesPhp,".2f"))
        
    salesFile.close()
    salesAve = salesTotal/counter
    print("\nTotal Sales Amount: Php",format(salesTotal,",.2f"))
    print("Average Sales: Php",format(salesAve,",.2f"))

def pleThree1():
    def runThrough(x):
        for i,j in x.items():
            print("The",i,"runs through",j)

    def xPress(x):
        print("\nThe following Expressway are included in this data set: ")
        for i in x.keys():
            print("-",i)

    def Prov(x):
        print("\nThe following Provinces are included in this data set: ")
        for i in x.values():
            print("-",i)

    #PLE3 - 1 Main
    xPressProv = {"Tplex" : "Pangasinan",
                  "Slex" : "Subic",
                  "Cavitex" : "Bacoor, Cavite",
                  "Mcx" : "Muntinlupa",
                  "Star Tollway": "Laguna"}
    print()
    runThrough(xPressProv)
    xPress(xPressProv)
    Prov(xPressProv)

def pleThree2():
    def choiceA(x):
        dFile = open("dictionaryKo.txt", "a")
        key = input("Enter a new key: ")
        val = input("Enter a new val: ")
        x[key] = val
        dFile.write(key+"\n"+val+"\n")
        dFile.close()
        return x

    def choiceB(x):
        checker = input("Enter a key to search: ")
        if checker in x.keys():
            print(checker,"IS a key in the dictionary")
        else:
            print(checker,"IS NOT a key in the dictionary")

    def choiceC(x):
        key = input("Enter a key to remove: ")
        dFile = open("dictionaryKo.txt", "r")
        dFileWord = dFile.read()
        x1 = dFileWord.replace(key,'')
        x1 = x1.replace(x[key],'')
        dFile.close()
        dFile = open("dictionaryKo.txt", "w")
        x2 = x1.split()
        for i in x2:
            dFile.write(i+"\n")
        dFile.close()
        del x[key]
        return x

    def choiceD(x):
        print("The values of the dictionary are: ")
        for i in x.values():
            print(i)
        
    #PLE3 - 2 Main
    dict1 = dict()
    looper = "Y"
    while looper == "Y":
        print("\nMain Menu"
              +"\n[A]\t Add a key pair value to a dictionary"
              +"\n[B]\t Check if a given key exist in the dictionary or not"
              +"\n[C]\t Remove a given key from the dictionary"
              +"\n[D]\t Display the values of the dictionary"
              +"\n[E]\t Exit\n")

        choice = input("Enter Choice Here: ").upper()
        if choice == "A":
            dict1.update(choiceA(dict1))

        elif choice == "B":
            choiceB(dict1)

        elif choice == "C":
            dict1.update(choiceC(dict1))

        elif choice == "D":
            choiceD(dict1)

        elif choice == "E":
            break

        else:
            print("Invalid Input")

        looper = input("Do you want to try again? [Y/N] answer: ").upper()

def pleThree3():
    #PLE3 - 3 Main
    fName = input("Enter file name: ")
    letter = input("Enter letter to be searched: ")
    counter = 0

    textFile = open(fName, "r")
    x = textFile.read()
    for i in x:
        if i == letter:
            counter += 1
    textFile.close()

    print("Occurances of the letter:",counter)
       
#Main
looper = "Y"
while looper == "Y":
    mainMenu = input("\nMain Menu"
                     +"\n[A] PLE 1"
                     +"\n[B] PLE 2 - Program 1"
                     +"\n[C] PLE 2 - Program 2"
                     +"\n[D] PLE 2 - Program 3"
                     +"\n[E] PLE 3 - Program 1"
                     +"\n[F] PLE 3 - Program 2"
                     +"\n[G] PLE 3 - Program 3"
                     +"\n[Z] Exit"
                     +"\nChoice: ").upper()

    if mainMenu == "A":
        pleOne()

    elif mainMenu == "B":
        pleTwo1()

    elif mainMenu == "C":
        pleTwo2()

    elif mainMenu == "D":
        pleTwo3()

    elif mainMenu == "E":
        pleThree1()

    elif mainMenu == "F":
        pleThree2()
        
    elif mainMenu == "G":
        pleThree3()

    elif mainMenu == "Z":
        print("Central Program Exiting")
        break;

    else:
        print("Invalid Choice")

    looper = input("\nWould you like to try again and go back to the main menu? [Y/N]: ").upper()
    

