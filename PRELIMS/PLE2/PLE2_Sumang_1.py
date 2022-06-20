def words():
    wordFile = open('word.txt', 'r')
    wordVar = wordFile.read()
   
    x = wordVar.replace('"', '')
    x = x.replace("'s", '')
    print(x)
    z = x.split()
    wordFile.close()
    return z

#Main
looper = "Y"
while looper == "Y":
    doubleWord = set()
    perWord = words()
    for i in perWord:
        if i.isalpha():
            checker = i.lower()
            if not(checker in doubleWord):
                print(checker+" "+str(perWord.count(i)).lower())
                doubleWord.add(checker)
    looper = input("Try again? [Y/N]: ").upper()


        
