#Main
list1=list()
list2=list()
txt1 = open('4C1.txt','r')
txt2 = open('4C2.txt','r')
print("//Text File A: ")
for i in txt1:
    list1.append(i)
    print(i)

print("\n//Text File B: ")
for i in txt2:
    list2.append(i)
    print(i)


print("\n//Combined Words: ")
for i in range(len(list1)):
    print(list1[i].strip(),list2[i].strip())

txt1.close()
txt2.close()

#EXPERIMENT 14: Working with IO Files (c)
