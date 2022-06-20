def startSort(x):
    for i in range(len(x)):
        min_idx = i
        for j in range(i+1,len(x)):
            if x[j]<x[min_idx]:
                min_idx=j
        (x[i],x[min_idx])=(x[min_idx],x[i])
    return x
    
    

def sortSelect(arr):
    for i in range(len(arr)):
        min_idx = i
        print("Loop",i+1)
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_idx]:
                min_idx=j
        (arr[i],arr[min_idx])=(arr[min_idx],arr[i])
        print(arr)
        
def sortBubble(arr):
    for i in range(len(arr)):
        print("Loop",i+1)
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                (arr[j],arr[j+1])=(arr[j+1],arr[j])
            print(arr)
                

def minAndMax(arr):
    print("************ Menu A ***********")
    print("Maximum value:",max(arr))
    print("Minimum value:",min(arr))
    

def centralTend(arr):
    print("************ Menu B ***********")
    #Mean
    meantotal=0
    for i in arr:
        meantotal = meantotal+i
    mean = meantotal/len(arr)
    print("Mean of array:", mean)

    #Median
    if len(arr)%2==0:
         i=(len(arr)/2)
         i2=(len(arr)/2)-1
         med = (int(arr[int(i)])+int(arr[int(i2)]))/2    
    else:
        i=(len(arr)/2)-.5
        med = arr[int(i)]
    print("Median of array:",med)

    #Mode
    mode = arr[0]
    modeCount = arr.count(mode)
    for i in arr:
        if arr.count(i)>modeCount:
            mode = i
            modeCount = arr.count(i)
    print("Mode of array:",mode)

def negative(arr):
    print("************ Menu C ***********")
    arr2 = []
    total = 0
    for i in arr:
        if i<0:
            arr2.append(i)
    print("Negative value(s) array:",arr2)

    for i in arr2:
        total = total+i

    print("Sum of negative array is",total)

def positive(arr):
    print("************ Menu D ***********")
    arr2 = []
    total = 0
    for i in arr:
        if i>0:
            arr2.append(i)
    print("Positive value(s) array:",arr2)

    for i in arr2:
        total = total+i

    print("Sum of positive array is",total)

def sortMenu(arr):
    print("************ Menu E ***********")
    looperS = "Y"
    while looperS == "Y":
        print("\nMain Menu"
              +"\n[B]\tBubble Sort"
              +"\n[S]\tSelection Sort")
        choiceS = input("Enter Choice: ").upper()
        if choiceS == "B":
            sortBubble(arr)
        elif choiceS == "S":
            sortSelect(arr)
        else:
            print("Invalid Choice")

        looperS = input("Do you want to try again? [Y]: ").upper()
        

#Main
looper = "Y"
arrLen = int(input("Enter number of elements: "))
arr = [0]*arrLen

for i in range(arrLen):
    arr[i] = int(input("Enter the element: "))

print("Array contains:",arr)

while looper == "Y":
    print("\nMain Menu"
          +"\n[A]\tDisplay the Maximum and Minimum"
          +"\n[B]\tDisplay the mean. median, and mode of Array"
          +"\n[C]\tDisplay the negative values and the sum of the Array"
          +"\n[D]\tDisplay the positive values and the sum of the Array"
          +"\n[E]\tSort Menu"
          +"\n[Q]\tEXIT PROGRAM")

    choice = input("Enter choice: ").upper()

    print("******************************")
    print("Sorted Array:",startSort(arr))

    if choice == "A":
        minAndMax(arr)

    elif choice == "B":
        centralTend(arr)

    elif choice == "C":
        negative(arr)

    elif choice == "D":
        positive(arr)

    elif choice == "E":
        sortMenu(arr)

    elif choice == "Q":
        print("exiting program")
        break

    else:
        print("Invalid Choice: ")

    looper = input("Do you want to try again? [Y]: ").upper()

#Sumang,Michael Dave WD-202
        
    

