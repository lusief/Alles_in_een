# # x=15
# # y=10
# # z=5
# # if x>y and y>z:
# #     print('a')
# # elif y>x and y>z:
# #     print('b')
# # else:
# #     print('c')


# # leeftijd=int(input('hoe oud'))
# # if leeftijd >=7 or leeftijd <=90:
# #     print('oke')
# # else:
# #     print('niet')

# # leeftijd=input('hoe oud ')
# # meerjarege=leeftijd>16

# # naam='a10'
# # if naam> 'a9':
# #     print('ok')
# # elif naam< 'a9':
# #     print('no')
# # else:
# #     print('c')

# hoog=55
# if hoog<166:
#     print('m')
# elif hoog <134:
#     print('n')
# else:
#     print('b')

klantenpas_ja=input('heeft u een pas')in ['ja','Ja']
bedrag=float(input('tebetalen'))
if klantenpas_ja:
    print('m')
elif klantenpas_ja and bedrag >30:
    print('n')
else:
    print('v')