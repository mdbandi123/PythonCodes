def func1(x,y):
    print("\nIsdisjoint of A to B")
    z = x.isdisjoint(y)
    print(z)

def func2(x,y):
    print("\nIsdisjoint of B to A")
    z = y.isdisjoint(x)
    print(z)

def func3(x,y):
    print("\nDisplay Difference of A to B")
    z = x.difference(y)
    print(z)

def func4(x,y):
    print("\nDisplay Difference of B to A")
    z = y.difference(x)
    print(z)

def func5(x,y):
    print("\nAdd the maximum values of two sets")
    x1 = max(x); y1 = max(y)
    z = int(x1) + int(y1)
    print(z)
    
#Main
looper = 'Y'
setA = set()
setB = set()
for i in range(5):
    vals = input("Enter 5 Values for Set A: ")
    setA.add(vals)
print("")
for i in range(5):
    vals = input("Enter 5 Values for Set B: ")
    setB.add(vals)

fSetA = frozenset(setA);fSetB = frozenset(setB)
while looper == 'Y':
    choice = input("""
    (a) Display Isdisjoint of A to B
    (b) Display Isdisjoint of B to A
    (c) Display Difference of A to B
    (d) Display Difference of B to A
    (e) Add the maximum values of two sets
    (z) Exit

    Choice: """).lower()

    if choice == 'a': func1(fSetA,fSetB)
    elif choice == 'b': func2(fSetA,fSetB)
    elif choice == 'c': func3(fSetA,fSetB)
    elif choice == 'd': func4(fSetA,fSetB)
    elif choice == 'e': func5(fSetA,fSetB)
    elif choice == 'z': break
    else: print("Invalid Input: TRY AGAIN")

    looper = input("\nDo you want to try again? [Y/N]: ").upper()

#EXPERIMENT 12: Sets Manipulation




