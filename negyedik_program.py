lotto = {
    'otos_lotto': [54, 68, 41, 63, 14],
    'hatos_lotto': [47, 15, 23, 74, 69, 8],
    'skandinav_lotto': [47, 15, 23, 74, 69, 8, 6]
}

print(lotto)

lotto_tipusok = list(lotto)
print(lotto_tipusok)

for lotto_tipus in lotto_tipusok:

    print(lotto_tipus)
    print(lotto[lotto_tipus])