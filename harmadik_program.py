gyumolcsok = ['alma', 'körte', 'banán', 'narancs', 'alma', 'banán']
print(len(gyumolcsok))
# for i in range(len(gyumolcsok)):

#     print(gyumolcsok[i])
print(gyumolcsok)
gyumolcsok.reverse()
print(gyumolcsok)
gyumolcsok.sort()
print(gyumolcsok)
for gyumolcs in gyumolcsok:

    print(gyumolcs)

    karakter = 0

    for betu in gyumolcs:

        karakter = karakter + 1

        betu = betu.swapcase()
        print(betu)

    print(karakter)