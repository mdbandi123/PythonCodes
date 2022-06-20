#Sorting
##def bubbleSort(array):
##    loop1 = 1
##    for i in range(len(array)):
##        print("Loop ",loop1,":")
##        loop1 = loop1 + 1
##        for j in range(0, len(array) - i - 1):
##            if array[j] > array[j+1]:
##                (array[j], array[j+1]) = (array[j+1], array[j])
##            print(array)
def bubbleSort(array):
    loop1 = 1
    for i in range(len(array)):
        print("\nLoop ",loop1,":")
        loop1 = loop1 + 1
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                (array[j], array[j+1]) = (array[j+1], array[j])
            print(array)
            

def selectionSort(array):
    loop1 = 1
    size = len(array)
    for step in range(size):
        min_idx = step
        print("loop ",loop1,":")
        for i in range(step + 1, size):
            #select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
        #put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])
        loop1 = loop1+1
        print(array)
#main()
data1 = ['T', 'H', 'E', 'L', 'O' , 'U', 'D']
data2 = [10, 3, -2, 4, 5, 98, 12]
data3 = ['G','O','D','I','S','H','A','P']
##print("\nOriginal unsorted: ")
##bubbleSort(data1)
##
##print("\nOriginal unsorted: ")
##bubbleSort(data2)
##
##print("\nOriginal unsorted: ")
##bubbleSort(data3)

####print("Bubble sorted: ")
####print(data)
##print("\nSelection sort: ")
##selectionSort(data1)
##print("\nSelection sort: ")
##selectionSort(data2)
print("\nSelection sort: ")
selectionSort(data3)
####        
