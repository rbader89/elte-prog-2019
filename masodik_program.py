szam = int(input("Adj meg egy számot: "))

for i in range(szam):

    vizsgalando_szam = i + 1

    if vizsgalando_szam % 2 == 0:

        print("Ez egy páros szám", vizsgalando_szam)

    else:

        print("Ez egy páratlan szám", vizsgalando_szam)