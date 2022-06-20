def runThrough(x):
    for i,j in x.items():
        print("The",i,"runs through",j)

def xPress(x):
    print("\nThe following Expressway are included in this data set: ")
    for i in x.keys():
        print("-",i)

def Prov(x):
    print("\nThe following Provinces are included in this data set: ")
    for i in x.values():
        print("-",i)

#Main
xPressProv = {"Tplex" : "Pangasinan",
              "Slex" : "Subic",
              "Cavitex" : "Bacoor, Cavite",
              "Mcx" : "Muntinlupa",
              "Star Tollway": "Laguna"}

runThrough(xPressProv)
xPress(xPressProv)
Prov(xPressProv)
