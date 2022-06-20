#Main
fName = input("Enter file name: ")
letter = input("Enter letter to be searched: ")
counter = 0

textFile = open(fName, "r")
x = textFile.read()
for i in x:
    if i == letter:
        counter += 1
textFile.close()

print("Occurances of the letter:",counter)
