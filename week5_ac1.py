#Array
#Rows are the outer elements
#Columns are elements in a row

a = [[1,2,3], [4,5,6], [7,8,9]]
##print(a[0]) #prints 1st row of array a
##print(a[1]) #prints 2nd row of array a
##print(a[0][2])#array[row][column]

#Changing an array 
##b = a[0]
##print(b)

##a[0][1] = 8
##print(a)

##b[0] = 9
##print(b)

for i in range(len(a)): #rows
    for j in range(len(a[i])): #columns
        print(a[i][j], end =" ") 
        
for x in a: #x is the row variable
    for y in x: #y is the column variable
        print(y, end = " ") #loop prints all the y's in the x before moving forward
        

#creating an array

##r = 3 #number of rows
##c = 4 #number of columns
##
##a = [[0]*c]*r #initializes a blank 2d array
##b = [[0]*c for in range(r)]#Initializes a blank

##r1 = int(input("Number of row: "))
##c1 = int(input("Number of columns: "))
##for i in range(r1):
##    x = 1
##    a = []
##    for j in range(c1):
##        a.append(int(input("Enter value for 2d array column: ")))
##    matrix.append(a)
##print(matrix)

#insert row value #array.insert(index,[value])

                 
#Stacks
##s1 = [] #empty stack
##s1.append("Holy")
##s1.append("Angel")
##s1.append("University")
##size = len(s1)
##for i in range(size-1,-1,-1):
##    print(i)
##    print("Before pop: ",s1[i])
##s1.pop()
##size = len(s1)
##for i in range(size-1,-1,-1):
##    print("After pop: ",s1[i])
