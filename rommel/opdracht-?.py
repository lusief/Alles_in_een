# lijst = [1,23,4,5,]
# print(lijst[1: 4])




# totaal = 0
# for x in range(1, 11):
#     totaal +=x
#     print(x)
#     print(totaal)
# for x in range(11,21,2):
#     totaal= x=+:
#     print(totaal)

# some=11+13+15+17+19
# print (some)
#if item not in dict: 
#dict[key] = value
from time import sleep
    
artiesten = ['DUA LIPA', 'OFENBACH', 'INIGO QUINTERO', 'OFENBACH', 'INIGO QUINTERO', 'INIGO QUINTERO', 'OFENBACH', 'OFENBACH', 'DUA LIPA', 'DUA LIPA', 'INIGO QUINTERO', 'DUA LIPA', 'DUA LIPA', 'OFENBACH', 'INIGO QUINTERO', 'OFENBACH', 'INIGO QUINTERO', 'INIGO QUINTERO', 'OFENBACH', 'OFENBACH', 'DUA LIPA', 'DUA LIPA', 'INIGO QUINTERO', 'DUA LIPA']
tel_dict={}
for a in artiesten:
    print(a)
    sleep(5)
    if a not in tel_dict:
        tel_dict[a]=0
        sleep(5)
        
    tel_dict[a]+=1
    print(tel_dict)
 
# if artiesten not in dict:
#     dict[artiesten] = value
# print('Dua LIPA')
