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
    
#Main
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
