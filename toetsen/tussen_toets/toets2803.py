# zorg ervoor dat test_lib.py in dezelfde directory zit als de toets
from test_lib import test, report

def is_even(getal: int) -> bool:
    return getal % 2 == 0
def get_even_list(lijst: list) -> list:
    nuw_list = []
    for getal in lijst:
        if getal % 2 == 0:
            nuw_list.append(getal)
    return nuw_list

def omgedraaid_even(lijst: list) -> list:
    even_getallen = [getal for getal in lijst if getal % 2 == 0]
    return even_getallen[::-1]

def aantal_even_getallen(lijst: list) -> int:
    nuw_list = []
    for getal in lijst:
        if getal % 2 == 0:
            nuw_list.append(getal)
    return len(nuw_list)

def is_palindroom(woord: str) -> bool:
    if woord == woord[::-1]:
        return True
    else:
        return False

def omgedraaid(lijst: list) -> list:
    return list(reversed(lijst))

def lijsten_samenvoegen(lijst1: list, lijst2: list) -> list:
    return lijst1 + lijst2
    # return lijst1

def aantal_palindromen(lijst: list) -> int:
    nuw_list = []
    for woord in lijst:
        if is_palindroom(str(woord)):
            nuw_list.append(woord)
    return len(nuw_list)
    # return 0

def aantal_even_getallen_op_even_index(lijst: list) -> int:
    nuw_list = []
    for getal in lijst:
        if getal % 2 == 0:
            nuw_list.append(getal)
    return len(nuw_list)

            
    # return 0

# opdracht 1a
# bepaal of een getal even is.
# schrijf minimaal 2 extra testen. De eerste 2 testcases zijn weggegeven.
expected = True
result = is_even(2)
test('Opdracht 1a (test 1) is correct', expected, result)

expected = False
result = is_even(3)
test('Opdracht 1a (test 2) is correct', expected, result)

# haal deze regel uit commentaar om de uitslag te laten zien. (en verplaats de regel naar je volgende opdracht)
#report()

# vraag 1b
# Zorg ervoor dat de functie get_even_list() enkel de even getallen uit de lijst teruggeeft.
# schrijf daarna per opgave minimaal 2 extra testen. De eerste 2 testcases zijn weggegeven.
expected = [2,4]
result = get_even_list([1,2,3,4,5])
test('Opdracht 1b (test 1) is correct', expected, result)

expected = [24, 16, 12, 2]
result = get_even_list([27, 15, 24, 16, 7, 12, 1, 2])
test('Opdracht 1b (test 2) is correct', expected, result)

# # vraag 2
# # Hoeveel even getallen zitten er in de lijst?
# # Voeg minimaal 2 testen toe!
expected = 2
result = aantal_even_getallen([1,2,3,4,5])
test('Opdracht 2 (test 1) is correct', expected, result)

# # vraag 3
# # reversed is een leuke functie, die je echter prima zelf kunt schrijven. Schrijf een functie die een lijst reversed (zonder reversed).
# # voeg 2 testen toe!
expected = [5, 4, 3, 2, 1]
result = omgedraaid([1, 2, 3, 4, 5])
test('Opdracht 3 (test 1) is correct', expected, result)

# # vraag 4
# # schrijf een functie die een lijst teruggeeft met alle even getallen uit de lijst, maar dan reversed.
# # voeg 2 testen toe!
expected = [4, 2]
result = omgedraaid_even([1, 2, 3, 4, 5])
test('Opdracht 4 (test 1) is correct', expected, result)

# # vraag 5
# # Voeg twee lijsten samen.
# # voeg 2 testen toe!
expected = [1, 2, 3, 4, 5, 6]
result = lijsten_samenvoegen([1, 2, 3],  [4, 5, 6])
test('Opdracht 5 (test 1) is correct', expected, result)

# # vraag 6
# # Schrijf een functie die true teruggeeft als een woord een palindroom is. (voorbeelden hiervan zijn: anna, lepel, parterretrap)
# # ook nu weer: voeg 2 testen toe!
expected = True
result = is_palindroom('anna')
test('Opdracht 6 (test 1) is correct', expected, result)

# # vraag 7
# # Hoeveel palindromen zitten er in de lijst?
# # voeg 2 testen toe!
expected = 3
result = aantal_palindromen(['anna', 'lepel', 'developer', 'parterretrap', 'test'])
test('Opdracht 7 (test 1) is correct', expected, result)

# # vraag 8
# # Breinkraker: hoeveel even getallen bevinden zich op een even index in de lijst? (index  0 is ook even)
# # voeg 2 testen toe!
expected = 3
result = aantal_even_getallen_op_even_index([2, 3, 4, 5, 6])
test('Opdracht 8 (test 1) is correct', expected, result)

expected = 3
result = aantal_even_getallen_op_even_index([1, 2, 3, 4, 5, 6])
test('Opdracht 8 (test 2) is correct', expected, result)

report()









