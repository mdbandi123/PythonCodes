def sortSel(arrY):
    for i in range(len(arrY)):
        min_inx = i
        print("Loop",i+1)
        for j in range(i+1,len(arrY)):
            if arrY[min_inx] > arrY[j]:
                min_inx = j
        (arrY[i],arrY[min_inx])=(arrY[min_inx],arrY[i])
                
        print(arrY)

def sortBub(arrX): 
    for i in range(len(arrX)):
        print("Loop",i+1)
        for j in range(len(arrX)-1):
            if arrX[j]>arrX[j+1]:
                (arrX[j],arrX[j+1])=(arrX[j+1],arrX[j])
            print(arrX)
    
                
        
        
        
    


#Main
looper = "Y"

length = int(input("Enter number of elements: "))
arr=[0]*length



for i in range(length):
    arr[i] = int(input("Enter the element: "))


##print("\nSelection Sort Array: ")
##sortSel(arr)
##print(arr)
print("\nBubble Sort Array: ")
print(arr)
sortBub(arr)

