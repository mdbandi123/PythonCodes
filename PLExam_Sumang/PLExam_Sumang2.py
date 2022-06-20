#Main
looper = "Y"
seatArray = [['*','*','X','*','X','X'],
      ['*','X','*','X','*','X'],
      ['*','*','X','X','*','X'],
      ['X','*','X','*','X','X'],
      ['*','X','*','X','*','*'],
      ['*','X','*','*','*','X'],
      ['X','*','*','*','X','X'],
      ['*','X','*','X','X','*'],
      ['X','*','X','X','*','X'],
      ['*','X','*','X','X','X'],
      ['*','*','X','*','X','*'],
      ['*','*','X','X','*','X'],
      ['*','*','*','*','X','*']]

rowDict = {"A":1,
           "B":2,
           "C":3,
           "D":4,
           "E":5,
           "F":6}

while looper == "Y":
    
    innerLoop1 = 1
    innerLoop2 = 1
    numberRow = 1
    
    print("\nSEAT PLAN\n")
    print("\tA B C D E F")
    for row in seatArray:
        print()
        print("Row",numberRow,end="\t")
        numberRow+=1
        for column in row:
            print(column, end = " ")

    numberRow = 1

    
    while innerLoop1 == 1:
        ticType = input("\n\nTicket Type: "
                    +"\n[1] First Class"
                    +"\n[2] Business Class"
                    +"\n[3] Economy Class"
                    +"\nChoice: ")
        
        if ticType.isnumeric():
            ticType = int(ticType)
            if ticType == 1:
                while innerLoop1 == 1:
                    r1 = input("Input desired row for First Class(Row 1 to Row 2): ")
                    if r1.isnumeric():
                        r1 = int(r1)
                        if r1>=1 and r1<=2:
                            r2 = r1
                            innerLoop1 = 0

                        else:
                            print("Invalid Choice")
                    else:
                        print("Invalid Choice")

            elif ticType == 2:
                while innerLoop1 == 1:
                    r1 = input("Input desired row for Business Class(Row 3 to Row 7): ")
                    if r1.isnumeric():
                        r1 = int(r1)
                        if r1>=3 and r1<=7:
                            r2 = r1
                            innerLoop1 = 0

                        else:
                            print("Invalid Choice")
                    else:
                        print("Invalid Choice")

            elif ticType == 3:
                while innerLoop1 == 1:
                    r1 = input("Input desired row for Business Class(Row 8 to Row 13): ")
                    if r1.isnumeric():
                        r1 = int(r1)
                        if r1>=8 and r1<=13:
                            r2 = r1
                            innerLoop1 = 0

                        else:
                            print("Invalid Choice")
                    else:
                        print("Invalid Choice")

            else:
                print("Invalid Choice")
        else:
            print("Invalid Choice")

    while innerLoop2 == 1:
        c1 = input("Desired Seat(A to F): ").upper()
        if c1.isalpha():
            if c1 in rowDict.keys():
                c2 = c1
                innerLoop2 = 0
            else:
                print("Invalid Choice")
                

        else:
            print("Invalid Choice")
        

    checker = seatArray[r2-1][rowDict[c2]-1]

    if checker == "*":
        seatArray[r2-1][rowDict[c2]-1] = "X"
        print("Seat",r2,c2,"Available. Reserving!")

        print("\nUPDATED SEAT PLAN\n")
        print("\tA B C D E F")
        for row in seatArray:
            print()
            print("Row",numberRow,end="\t")
            numberRow+=1
            for column in row:
                print(column, end = " ")

    else:
        print("Seat Already Occupied")

    looper = input("\n\nDo you want to try again? [Y/N]:").upper()
        
        

