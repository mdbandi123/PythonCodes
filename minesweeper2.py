def matrix(n,m):
    rowMat = []
    col = int(n)
    row = int(m)
    while col > 0:
        colMat = list(input())

        if len(colMat) == row:
            rowMat.append(colMat)
            col -= 1
            

    return rowMat

def changer(x):

    for a in range(len(x)):
        for b in range(len(x[a])):
            
            for c in range(len(x[a][b])):
                counter = 0
                if x[a][b][c] != "*":
                    if b == 0:
                        if c == 0:
                            if x[a][b][c+1] == "*" :
                                counter += 1
                            if x[a][b+1][c] == "*":
                                counter += 1
                            if x[a][b+1][c+1] == "*":
                                counter += 1
                        elif c == len(x[a][b])-1:
                            if x[a][b][c-1] == "*" :
                                counter += 1
                            if x[a][b+1][c] == "*":
                                counter += 1
                            if x[a][b+1][c-1] == "*":
                                counter += 1
                        else: 
                            if x[a][b][c+1] == "*" :
                                counter += 1
                            if x[a][b+1][c] == "*":
                                counter += 1
                            if x[a][b+1][c+1] == "*":
                                counter += 1
                            if x[a][b][c-1] == "*" :
                                counter += 1
                            if x[a][b+1][c-1] == "*":
                                counter += 1
                        
                    elif b == len(x[a])-1:
                        if c == 0:
                            if x[a][b][c+1] == "*" :
                                counter += 1
                            if x[a][b-1][c] == "*":
                                counter += 1
                            if x[a][b-1][c+1] == "*":
                                counter += 1
                        
                        elif c == len(x[a][b])-1:
                            if x[a][b][c-1] == "*" :
                                counter += 1
                            if x[a][b-1][c] == "*":
                                counter += 1
                            if x[a][b-1][c-1] == "*":
                                counter += 1
                        
                        else: 
                            if x[a][b][c+1] == "*" :
                                counter += 1
                            if x[a][b-1][c] == "*":
                                counter += 1
                            if x[a][b-1][c+1] == "*":
                                counter += 1
                            if x[a][b][c-1] == "*" :
                                counter += 1
                            if x[a][b-1][c-1] == "*":
                                counter += 1
                    
                    else: 
                        if c == 0:
                            if x[a][b][c+1] == "*" :
                                counter += 1
                            if x[a][b+1][c] == "*":
                                counter += 1
                            if x[a][b-1][c] == "*":
                                counter += 1
                            if x[a][b+1][c+1] == "*":
                                counter += 1
                            if x[a][b-1][c+1] == "*":
                                counter += 1

                        elif c == len(x[a][b])-1:
                            if x[a][b][c-1] == "*" :
                                counter += 1
                            if x[a][b+1][c] == "*":
                                counter += 1
                            if x[a][b-1][c] == "*":
                                counter += 1    
                            if x[a][b+1][c-1] == "*":
                                counter += 1
                            if x[a][b-1][c-1] == "*":
                                counter += 1
                        
                        else: 
                            if x[a][b][c+1] == "*" :
                                counter += 1
                            if x[a][b][c-1] == "*" :
                                counter += 1
                            if x[a][b-1][c] == "*":
                                counter += 1
                            if x[a][b+1][c] == "*":
                                counter += 1
                            if x[a][b-1][c+1] == "*":
                                counter += 1
                            if x[a][b+1][c-1] == "*" :
                                counter += 1
                            if x[a][b-1][c-1] == "*":
                                counter += 1
                            if x[a][b+1][c+1] == "*":
                                counter += 1
                        
                        

                    x[a][b][c] = counter
        
 
    
    for a in range(len(x)):
        print("\n\nField #"+str(a+1))

        for b in range(len(x[a])):
            print()
            for c in range(len(x[a][b])):
                print(x[a][b][c],end="")

                    




#Main
mineList = []
looper = True
while (looper) == True:
    n, m = input().split()
    if (int(n) and int(m)) != 0:
        if (int(n) and int(m)) > 0 and (int(n) and int(m)) < 100:
            mineList.append(matrix(n,m))
    else:
        looper = False

changer(mineList)


