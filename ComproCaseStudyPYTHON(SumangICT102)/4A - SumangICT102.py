#Main
looper = True
while looper == True:
    val = input("Input String: ").upper()
    if val.isalpha():
        txt = open('4A.txt','a')
        txt.write(val+'\n')
        looper = True
        txt.close
    else:
        looper = False
        

txt = open('4A.txt','r')
txt_read = txt.read()
print("(text file)")
print(txt_read)

#EXPERIMENT 14: Working with IO Files (a)
