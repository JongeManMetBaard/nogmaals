stopDag = input("Welke dag moet ik stoppen? (ma) (di) (wo) (do) (vr) (za) (zo) ")
deur = 1
checken = False 
while not checken:
    if deur == 1:
        print("Maandag")
        printdag = ("ma")
        deur = 2
    elif deur == 2:
        print("Dinsdag")
        printdag = ("di")
        deur = 3
    elif deur == 3:
        print("Woensdag")
        printdag = ("wo")
        deur = 4
    elif deur == 4:
        print("Donderdag")
        printdag = ("do")
        deur = 5
    elif deur == 5:
        print("Vrijdag")
        printdag = ("vr")
        deur = 6
    elif deur == 6:
        print("Zaterdag")
        printdag = ("za")
        deur = 7
    elif deur == 7:
        print("Zondag")
        printdag = ("zo")        
    checken = stopDag == printdag 