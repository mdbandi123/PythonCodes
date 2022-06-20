
def translator(x,y):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    aList = list(alphabets)
    bList = list(x)
    cList = list(y)

    for i in range(len(bList)):
        if bList[i] != " " and bList[i] in aList:
            j = aList.index(bList[i])
            bList[i] = cList[j]

    return bList

def printer(x):
    for i in range(len(x)):
        print()
        for j in range(len(x[i])):
            print(x[i][j], end="")

#main
looper = True
messageHolder = []
t = int(input())

for i in range(t):
    message = input()
    cypher = input()
    messageHolder.append(translator(message,cypher))

printer(messageHolder)


    
    
