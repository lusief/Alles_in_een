from random import choice
COMPELMENTEN = ('LEKKER BEZIG,','JE DOET HET GEWELDIG,','JE BENT SUPER')

def generate_complementen(naam: str) ->str :
    complementen = ('EKKER BEZIG,','JE DOET HET GEWELDIG,','JE BENT SUPER') #naam is een parameter die ik gebruik is de funcvtie als variabel
    r_complimenten = choice(complementen)+naam
     
    return r_complimenten

naam_gamer = input ('wat is je naam? ')#de vraag is de argument en de antwoord gaat in de variabel
complementen = generate_complementen(naam_gamer)
complementen2= generate_complementen('jan')
print (complementen)
print (complementen2)


# def add_length(zin):
#     lijst_lengte=[]
#     woorden =  zin .split()
#     for woord in woorden:
#         nieuw_woord= f'{woord}{len(woord)}'
#         lijst_lengte.append(nieuw_woord)
#     return lijst_lengte
    
# print(add_length('dit is een voorbeld van een zin'))
    