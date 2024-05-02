eiren = ['roze', 'geel', 'groen', 'blauw', 'rood']
plekken = [9, 0, 4, 6, 3, 9, 10, 7, -1, -5, -70,70]

# geldige_kleuren = []
# lege_list = []

# for plek in plekken:
#     if 0 <= plek < len(eiren):
#         geldige_kleuren.append(eiren[plek])
#     else:
#         lege_list.append(plek)

# print(geldige_kleuren)
# print(lege_list)


lege_list = []
for plek in plekken:
    if len(eiren) * -1 <= plek <= len(eiren):
        print(eiren[plek])
    else:
        lege_list.append(plek)
print(lege_list)
