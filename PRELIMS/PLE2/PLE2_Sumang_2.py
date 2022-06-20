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
    
#Main
looper = "Y"
while looper == "Y":
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
    looper = input("Try again? [Y/N]: ").upper()
    
    
