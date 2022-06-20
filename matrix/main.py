from matrix import add, scalmultiply, multiply, transpose



def matrixA(x):
    y1 = []
    for i in range(int(x[0])):
        j = True
        while j == True:
            y2 = input().split()
            if len(y2) == int(x[1]):
                j = False
        y1.append(y2)
    return y1    

def matrixB(x):
    y1 = []
    for i in range(int(x[0])):
        j = True
        while j == True:
            y2 = input().split()
            if len(y2) == int(x[1]):
                j = False
        y1.append(y2)
    return y1

def printer(matC):
    for i in matC:
        print()
        for j in i:
            print(j,end=" ")    

#Main
dimB = []
matB = []
scalNum = 0
opName = input().lower()
dimA = input().split()
matA = matrixA(dimA)


if opName == "add":
    dimB = input().split()
    matB = matrixB(dimB)
    if dimA == dimB:
            printer(add(matA, matB))
    else:
        print("Matrix Undefined")

elif opName == "scalmultiply":
    scalNum = int(input())
    printer(scalmultiply(matA, scalNum))

elif opName == "multiply":
    dimB = input().split()
    matB = matrixB(dimB)
    if len(dimA[1]) == len(dimB[0]):
        printer(multiply(matA,matB))
    else:    
        print("Matrix Undefined")

elif opName == "transpose":
    printer(transpose(matA))

