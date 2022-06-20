#Main
looper = 'Y'
dict1 = dict()
while looper == 'Y':
    val = int(input("Input a number: ")); counter = 1
    for i in range(val):
        dict1[counter] = (counter*counter)
        counter += 1
    print(dict1)
    looper = input("Do you want to try again? [Y/N]: ").upper();print("");dict1.clear()
    
#EXPERIMENT 13: Dictionary Manipulation (a)
