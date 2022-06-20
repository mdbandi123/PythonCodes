def createArr():
    arrLen = int(input("Enter number of elements: "))
    arr = [0]*arrLen

    for i in range(arrLen):
        elem = int(input("Enter the element: "))
        arr[i] = elem
    return arr

def bubbleSort(arr):
    arrX = arr.copy()
    print("Array contains:",arrX)
    print("********** Bubble Sort Menu **********")
    
    loopCount = 1
    arrLen = len(arrX)
    for i in range(arrLen-1):      
        for j in range(0, arrLen - i - 1):
            if arrX[j]>arrX[j+1]:
                (arrX[j],arrX[j+1])=(arrX[j+1],arrX[j])
            print("Loop",loopCount)
            print(arrX)
            loopCount += 1

def insertSort(arr):
    arrX = arr.copy()
    print("Array contains:",arrX)
    print("********** Insertion Sort Menu **********")
    
    arrLen = len(arrX)
    for i in range(1, arrLen):
        print("Loop",i)
        j = i-1
        nextElem = arrX[i]
        while (arrX[j] > nextElem) and (j >= 0):
            arrX[j+1] = arrX[j]
            j=j-1
            arrX[j+1] = nextElem
            print(arrX)
        print(arrX)

def mergeSort(arr):
    arrY = arr.copy()
    print("Array contains:",arrY)
    print("********** Merge Sort Menu **********")

    #Splitter Func
    def split(arrY):
        arrX = arrY.copy()
        arrLen = len(arrX)
        if arrLen <= 1:
            return arrX
        
        middle = arrLen // 2
        left = arrX[:middle]
        right = arrX[middle:]

        left = split(left)
        right = split(right)
        return list(merge(left, right))

    #Merge Func
    def merge(leftSide,rightSide):
        x = []
        while len(leftSide) != 0 and len(rightSide) != 0:
            if leftSide[0] < rightSide[0]:
                x.append(leftSide[0])
                leftSide.remove(leftSide[0])
            else:
                x.append(rightSide[0])
                rightSide.remove(rightSide[0])
        if len(leftSide) == 0:
            x = x + rightSide
        else:
            x = x + leftSide
        return x

    print("Sorted array is: \n",split(arrY))
    
def selectSort(arr):
    arrX = arr.copy()
    print("Array contains:",arrX)
    print("********** Selection Sort Menu **********")
    
    arrLen = len(arrX)
    for i in range(arrLen):
        print("Loop",i+1)
        low = i
        for j in range(i+1,arrLen):
            if arrX[j]<arrX[low]:
                low = j
        (arrX[i],arrX[low])=(arrX[low],arrX[i])
        print(arrX)

#main
looper = 'Y'
arrMain = createArr()
print("Array contains:",arrMain)

while looper == 'Y':
    print("\nSort Menu"+
          "\n[B]\tBubble Sort"+
          "\n[I]\tInsertion Sort"+
          "\n[M]\tMerge Sort"+
          "\n[S]\tSelection Sort"+
          "\n[E]\tExit Menu\n")
    choice = input("Enter choice: ").upper()

    if choice == "B":
        bubbleSort(arrMain)

    elif choice == "I":
        insertSort(arrMain)

    elif choice == "M":
        mergeSort(arrMain)

    elif choice == "S":
        selectSort(arrMain)

    elif choice == "E":
        print("End of the Program")
        break
    else:
        print("Invalid Choice")

    looper = input("Do you want to repeat Sort Menu again? Answer: ").upper()
        
          


