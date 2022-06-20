#Func
def sort(x):
    print("Bubble Sort Array: ")
    for i in range(len(x)):
        print("Loop",i+1)
        for j in range(len(x)-1):
            if x[j] > x[j+1]:
                (x[j], x[j+1]) = (x[j+1], x[j])
            print(x)
    
    
def mean(x):
    total = 0
    for i in x:
        total = total + int(i)
    mean = total/len(arr)
    print("Mean of the numbers:",mean)

def median(x):
    if len(x)%2==0:
         i=(len(x)/2)
         i2=(len(x)/2)-1
         med = (int(x[int(i)])+int(x[int(i2)]))/2    
    else:
        i=(len(x)/2)-.5
        med = x[int(i)]

    print("Median of the numbers:",med)
    
#Sumang, Michael Dave WD-202
    
#Main
lenArr = int(input("Enter number of elements: "))
arr = [0]*lenArr

for i in range(len(arr)):
    arr[i] = int(input("Enter the element: "))

print("Array Contains:",arr)
sort(arr)
print(arr)
mean(arr)
median(arr)

#Sumang, Michael Dave C. WD-202


