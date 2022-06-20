def selectSort(arr):
    arrX = arr.copy()
    arrLen = len(arrX)

    for i in range(arrLen):
        print("Loop",i+1)
        low = i
        for j in range(i+1,arrLen):
            if arrX[j]<arrX[low]:
                low = j
        (arrX[i],arrX[low])=(arrX[low],arrX[i])
        print(arrX)
            

unsorted_list = [4,67,-89,-2,3]

selectSort(unsorted_list)

