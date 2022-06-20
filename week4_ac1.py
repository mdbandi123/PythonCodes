#Map
##map(function,iterable)

#map() with string

##def print_iterator(it):
##    for i in it:
##        print(i,end='')
##
##def to_upper_case(s):
##    return str(s).upper()

##map_iterator = map(to_upper_case, ('abc'))
##print_iterator(map_iterator)


#map() with lambda

##def print_iterator(it):
##    for i in it:
##        print(i,end=' ')
##
##
list_numbers = [2,4,3,5]
map_iterator = list(map(lambda x: x*2, list_numbers))
print(map_iterator)
##
dic_code = {1: "abc", 2: "xyz", 3: "dfdgf", 4: "hehi", 5: "jihg", 6: "knhs"}
dic_names = dict(map(lambda x: (x[0], "$" +x[1] + "#"), dic_code.items()))
print("Updated Dictionary: ")
print(dic_names)
##
##dic_code = {1:5, 2:8, 3:7, 4:6 , 5:5, 6:4}
##dic_values = dict(map(lambda x: (x[0], x[1] * 5), dic_code.items()))
##print(dic_values)
##print(dic_code)

##d1 = {"studno" : 20568987, "name": "Mark Lugtu", "age":21}
##dFile = open("dataStud.txt", "w")
##for i, j in d1.items():
##    x = str(i); y=str(j)
##    dFile.write(x+"\n"+y+"\n")
##dFile.close()
##
##dFile = open("dataStud.txt","r")
##s = dFile.readline()
##while s!= "":
##    s1 = s.strip("\n")
##    print(s1)
##    s = dFile.readline()
##dFile.close()
