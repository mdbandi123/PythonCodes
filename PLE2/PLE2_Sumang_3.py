salesFile = open("sales.txt", "r")
salesTotal = 0; counter = 0

print("List of sales in Php:")
valHolder = salesFile.readline()
while valHolder != "":
    salesPhp = float(valHolder.rstrip("\n"))
    salesTotal += salesPhp
    counter += 1
    valHolder = salesFile.readline()
    print("Day",counter,":",format(salesPhp,".2f"))
    
salesFile.close()
salesAve = salesTotal/counter
print("\nTotal Sales Amount: Php",format(salesTotal,",.2f"))
print("Average Sales: Php",format(salesAve,",.2f"))

