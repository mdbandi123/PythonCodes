def func1(x):
    print("\nChoice A: Sum of all items")
    total = 0
    for i in range(len(x)):
       z = 'D'+str(i+1)
       total += x[z]
    print("Answer:",total)

def func2(x):
    print("\nChoice B: Product of all positive numbers")
    total = 1
    for i in range(len(x)):
       z = 'D'+str(i+1)
       if x[z] > 0:
           total *= x[z]
    print("Answer:",total)

def func3(x):
    print("\nChoice C: Product of all negative numbers")
    total = 1
    for i in range(len(x)):
       z = 'D'+str(i+1)
       if x[z] < 0:
           total *= x[z]
    print("Answer:",total)

def func4(x):
    print("\nChoice D: Remove a key from the dictionary")
    y = input("Enter a key to remove: ").upper()
    del x[y]
    print("Answer:",x)

def func5(x):
    print("\nChoice E: Sort the items")
    sortDict = dict()
    listVals = list(x.values())
    listKeys = list(x.keys())
    listVals.sort()
    for i in range(len(listVals)):
        for key, value in x.items():
            if value == listVals[i]:
                sortDict[key] = listVals[i]
    print(sortDict)
 
#Main
dict1 = dict()
amount = int(input("How many values would you like to use? : "))
for i in range(amount):
    z = 'D'+str(i+1);
    val = int(input("Enter value for "+z+":"))
    dict1[z] = val
looper = 'Y'
while looper == 'Y':
    print("""
    //DICTIONARY VALUES:
    """,dict1)

    choice = input("""
    (a) Sum of all Items
    (b) Product of all positive numbers
    (c) Product of all negative numbers
    (d) Remove a key from the dictionary
    (e) Sort the items
    (z) Exit

    Choice: """).lower()

    if choice == 'a': func1(dict1)
    elif choice == 'b': func2(dict1)
    elif choice == 'c': func3(dict1)
    elif choice == 'd': func4(dict1)
    elif choice == 'e': func5(dict1)
    elif choice == 'z': break
    else: print("Invalid Input: TRY AGAIN")

    looper = input("Do you want to try again? [Y/N]: ").upper();print("")

#EXPERIMENT 13:Dictionary Manipulation (b)



