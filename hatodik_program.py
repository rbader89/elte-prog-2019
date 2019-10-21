#Kérjünk a usertől két pozítív egész számot 10 és száz között
#Alapműveletek elvégézse ezzel a két számmal (összeadás, kivonás, szorzás és osztás)
#Készítsünk egy tömböt aminake a terjedelme A és B közötti
#   Ebben vizsgáljuk meg, hogy mely számok párosak, eztirassuk ki számonként
#   Irassuk ki a tömb összegét

is_error = False

def osztas(szam1, szam2):

    eredmeny = szam1 / szam2

    return eredmeny

def kivonas(szam1, szam2):

    eredmeny = szam1 - szam2

    return eredmeny

def adatbekero():

    elso_szam = int(input("Adja meg az első számot:"))
    masodik_szam = int(input("Adja meg a második számot:"))

    eredmeny = [elso_szam, masodik_szam]

    return eredmeny

def fofuggveny():

    print("Adjon meg két darab számot 0 és 100 között")

    eredmeny = adatbekero()

    elso_szam = eredmeny[0]
    masodik_szam = eredmeny[1]


    if not (elso_szam >= 0 and elso_szam <= 100):

        raise ArithmeticError("Rossz első számot adott meg: " + str(elso_szam))

    if not(masodik_szam >= 0 and masodik_szam <= 100):

        raise ArithmeticError("Rossz második számot adott meg: " + str(masodik_szam))

    osszeg = elso_szam + masodik_szam
    print("Összeg:", osszeg)

    kulonbseg1 = kivonas(elso_szam, masodik_szam)
    print("Különbség 1:", kulonbseg1)

    kulonbseg2 = kivonas(masodik_szam, elso_szam)
    print("Különbség 2:", kulonbseg2)

    szorzat = elso_szam * masodik_szam
    print("Szorzat:", szorzat)

    hanyados1 = osztas(elso_szam, masodik_szam)
    print("Hányados1:", hanyados1)

    hanyados2 = osztas(masodik_szam, elso_szam)
    print("Hányados2:", hanyados2)

    lista = list(range(elso_szam, masodik_szam))
    lista.append(masodik_szam)
    print(lista)

    tomb_osszege = 0

    for szam in lista:

        tomb_osszege += szam
        #Ez megyegyezik a 'tomb_osszege = tomb_osszege + szam' művelettel

        if szam % 2 == 0:
            print(szam, "páros szám")
        else:
            print(szam, "páratlan szám")

    print("Tömb összege", tomb_osszege)
    tomb_osszege2 = sum(lista)

    print("Tömb összege2", tomb_osszege2)

try:    

    fofuggveny()

except ValueError as error:
    is_error = True
    print(error)
    print("Nem számot adott meg")

except ZeroDivisionError as error:
    is_error = True
    print(error)
    print("A nullával való osztás nem engedélyezett")

except ArithmeticError as error:
    is_error = True
    print(error)

except Exception as error:
    is_error = True
    print(error)
    print("Hiba történt")

finally:

    if is_error == True:

        fofuggveny()
    else:
        print("A program futás véget ért!")
        exit()