def inputChecker(dictWords,scramWords):
    for a in range(len(dictWords)):
        if not (len(dictWords[a])>0 and len(dictWords[a])<7 and dictWords[a].isalpha()):
            #print("e1")
            return False
    if len(scramWords)==1 and scramWords[0].islower() and len(scramWords[0]) > 0 and len(scramWords[0]) < 7 and scramWords[0].isalpha():
        for i in dictWords:
            if i.islower() == False or dictWords.count(i) > 1:
                #print("e2")
                return False
        return True
    else:
        #print("e3")
        return False


def tester(dictWords,scramWords):
    for i in dictWords:
        c1=0
        if len(i)==len(scramWords[0]):      
            for j in range(len(i)):
                d1 = i.count(i[j])
                d2 = scramWords[0].count(i[j])
                if d1==d2:
                    c1+=1
            if c1 == len(i):        
                return True    
    #print("e4")                     
    return False
           
       

#main
dictWords = input().split()
scramWords = input().split()
checker = inputChecker(dictWords,scramWords)

if checker:
    print(tester(dictWords,scramWords))

else: 
    print(checker)



