def function1(x):
    print("\n[1] IN")
    tf = input("Input Value: ")
    if tf in x:
        print("Output : True")
    else:
        print("Output : False")

def function2(x):
    print("\n[2] ENUMERATE")
    print("Output :")
    for i in range(len(x)):
        print("(",i,",",x[i],")")

def function3(x):
    print("\n[3] MAX")
    print("Output :")
    y = max(x)
    print(y)

def function4(x):
    print("\n[3] MIN")
    print("Output :")
    y = min(x)
    print(y)
    
#Main
looper = 'Y'
while looper == 'Y':
    list1 = []
    for i in range(10):
        vals = input("Enter 10 Values: ")
        list1.append(vals)
        
    tup1 = tuple(list1)
    function1(tup1)
    function2(tup1)
    function3(tup1)
    function4(tup1)
    list1.clear()
    looper = input("\nDo you want to try again? [Y/N]: ").upper()


#EXPERIMENT 11: Tuple Manipulation    
