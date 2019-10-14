#Készítsetek egy programot, ami amegadott 
#   matematika, földrajz, magyar és történelem jegyek alapján készít bizonyítványt
#Minden tárgynál írjátok ki a kerekített átlagot (év végi jegy) és az 
#   adott tárgyhoz a legjobb valamint a legrosszabb jegyet
#Az egyes tárgyhoz tartozó jegyeket egy szótárban tároljátok tömbként
#A usertől a jegyeket vesszővel elválasztva kérjétek be, ezt alakítsátok tömbbé
#Ellenőrizzétek, hogy csak 1 és 5 közötti számokat adott
#A házikat a baderrichard@hotmail.com címre küldjétek 2019. 10. 20. 20:00-ig

#Tippek
#Szöveg darabolása listává: https://www.w3schools.com/python/ref_string_split.asp
#Szöveg lista szám listává konvertálása: https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int

print("Adja meg az érdemjegyeket veszzővel (',') elválasztva!")
matek = input("Matematika: ")
foldrajz = input("Földrajz: ")
magyar = input("Magyar: ")
tori = input("Történelem: ")

naplo = {
    'matek': [],
    'magyar': [],
    'foldrajz': [],
    'tori': []
}

matek_list = matek.split(',')
foldrajz_list = foldrajz.split(',')
magyar_list = magyar.split(',')
tori_list = tori.split(',')

naplo['matek'] = list(map(int, matek_list))
naplo['magyar'] = list(map(int, magyar_list))
naplo['foldrajz'] = list(map(int, foldrajz_list))
naplo['tori'] = list(map(int, tori_list))

targyak = list(naplo)

zarojegyek = []

for targy in targyak:

    jegyek = naplo[targy]

    maxJegy = max(jegyek)
    minJegy = min(jegyek)

    if minJegy < 1 and maxJegy > 5:
        print("A magedott", targy, "érdemjegy nem 1 és 5 között van!")
        exit()
    
    jegy = round(sum(jegyek) / len(jegyek))

    zarojegyek.append(jegy)

    print("Tárgy:", targy)
    print("Osztályzat:", jegy)
    print("Legjobb", targy, "jegy:", maxJegy)
    print("Legrosszabb", targy, "jegy:", minJegy)

ev_vegi_atalg = sum(zarojegyek) / len(zarojegyek)
print("Év végi átlag", ev_vegi_atalg)