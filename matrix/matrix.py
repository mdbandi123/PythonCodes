


def add(matA, matB):
    matC = []
    
    for i in range(len(matA)):
        row = []
        for j in range(len(matA[i])):
            row.append(int(matA[i][j])+int(matB[i][j]))
        matC.append(row)    

    return matC

def scalmultiply(matA, scalNum):
    matC = []
    
    for i in range(len(matA)):
        row = []
        for j in range(len(matA[i])):
            row.append(int(matA[i][j])*scalNum)
        matC.append(row)    

    return matC  

def multiply(matA, matB):
    matC = []
    for i in range(len(matA)):
        row = []
        for a in range(len(matB[i])):
            x = 0
            for j in range(len(matA[i])):
                x += (int(matA[i][j])*int(matB[j][a])) 
            row.append(x)
        matC.append(row)    

    return matC

def transpose(matA):
    matC = []
    for i in range(len(matA[0])):
        row = []
        for j in range(len(matA)):
            row.append(int(matA[j][i]))
        matC.append(row)    

    return matC




            



    
    
                 

                

    
    

