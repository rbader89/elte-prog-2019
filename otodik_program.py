#Kérjünk a usertől két pozítív egész számot 10 és száz között
#Alapműveletek elvégézse ezzel a két számmal (összeadás, kivonás, szorzás és osztás)
#Készítsünk egy tömböt aminake a terjedelme A és B közötti
#   Ebben vizsgáljuk meg, hogy mely számok párosak, eztirassuk ki számonként
#   Irassuk ki a tömb összegét
print("Adjon meg két darab számot 10 és 100 között")
elso_szam = int(input("Adja meg az első számot:"))
masodik_szam = int(input("Adja meg a második számot:"))

if not (elso_szam >= 10 and elso_szam <= 100):
    print("Rossz első számot adott meg")
    exit()

if not(masodik_szam >= 10 and masodik_szam <= 100):
    print("Rossz második számot adott meg")
    exit()

osszeg = elso_szam + masodik_szam
print("Összeg:", osszeg)

kulonbseg1 = elso_szam - masodik_szam
print("Különbség 1:", kulonbseg1)

kulonbseg2 = masodik_szam - elso_szam
print("Különbség 2:", kulonbseg2)

szorzat = elso_szam * masodik_szam
print("Szorzat:", szorzat)

hanyados1 = elso_szam / masodik_szam
print("Hányados1:", hanyados1)

hanyados2 = masodik_szam / elso_szam
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