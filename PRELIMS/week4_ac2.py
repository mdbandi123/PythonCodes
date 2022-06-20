#Array

#to create and declare and array
from array import*
a = array("f",[14,10,12,4,6])

import array as arr
b = arr.array('i', [1,2,3,4,5])

#blank array
a1 = array("i",[])

##print(a)
##print(a1)


#calling an array
##print(a[4])
##print(a[-5])
##print(a[1:3])
##print(a[1:])
##print(a[:3])
##print(a[-4:-2])
##print(a[-5:])
##print(a[:-2])

#adding/appending
##n = int(input("Enter the length of your array: "))
##for i in range(n):
##    no = int(input("Enter number: "))
##    a1.append(no)
#in loop
##ans = "Y"
##while ans == "Y":
##    no = int(input("Enter number: "))
##    a1.append(no)
##    ans = input("do you want to try again? [Y/N] :").upper()
##
##print(a1)

#using insert / insert(pos,value)
##a.insert(1,14.5)
##print(a)

#Popping
a.pop(2)
print(a)

#remove
a.remove(14)
print(a)

#delete
del a[1]
print(a)
