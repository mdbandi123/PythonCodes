#Dictionary
dict1 = {
    "stunnum": 12345,
    "studname": "Peter",
    "grade" : 85,
    "remark": "passed"}

dictX = {1:10,
         2:20,
         3:30}

for i in dict1:
    print(i)
#Printing the whole dictionary
##print(dict1)

#Printing a specific value
print(dict1["grade"])
##rem = dict1.get("grade")
##print(rem)
##print(dict1.get("grade"))

#Inserting or Changing values inside a dictionary
##x = input("Enter a key: ")
##y = input("Enter a value: ")
##dict1["address"] = "Guagua"
##dict1["grade"] = 90
##dict1[x] = y
##print(dict1)

#Iteration
#keys
##for i in dict1:
##    print(i)
##
##for i in dict1.keys():
##    print(i)

#values
##for i in dict1:
##    print(dict1[i])
##
##for i in dict1.values():
##    print(i)

#both key and value

##for i,j in dict1.items():
##    print(i, j)

#checking if part of the dict
#keys
##if "grade" in dict1:
##    print("Yes")
##
##else:
##    print("false")

#values
##if 85 in dict1.values():
##    print("yes")
##
##else:
##    print("false")

#copying
##dict2 = dict1
##print(dict1)
##print(dict2)

#removing item
##print(dict1)
##print("popped:")
##dict1.pop("studname")
##print(dict1)
##dict1.popitem()
##print(dict1)
##dict1.clear()
##print(dict1)
##del dict1

#combining
combifile = {"first":dict1,"second":dictX}
print(combifile)
print(combifile["second"])


    


