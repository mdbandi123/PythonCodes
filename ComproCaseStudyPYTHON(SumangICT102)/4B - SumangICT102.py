#Main
list1=list()
txt = open('4B.txt','r')
print("Song Titles from File: ")
for i in txt:
    list1.append(i)
    print(i)

print("\n//Longest Text: ",max(list1,key=len))
txt.close()

#EXPERIMENT 14: Working with IO Files (b)
