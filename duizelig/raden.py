raden = 0
checken = True
while checken:
    raden += 1
    vraag = input("Welke woord kun je van de volgende letters maken: U-T-Q-I? ")
    if vraag != "Quit":
        print("Try again")               
    else:
        print("Good job!")
        checken = False 
        print("U heeft er" ,raden, "x over geraden")