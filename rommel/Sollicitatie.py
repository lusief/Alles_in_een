# aankondiging tekst
print("+" * 37)
print('+{:^35}+'.format('Sollicitatieformulier'))
print("+" * 37)
print('Er worden u een aantal relevante vragen gesteld...')
print('Gelieve deze naar eer en geweten in te vullen.')
print('Als blijkt dat u aan de criteria voldoet, komt u in')
print('aanmerking voor een serieus sollicitatiegesprek!')
print('Ontspan maar blijf alert, hier komen de vragen')

# variabelen
Min_gewicht = 90
Max_gewicht = 120
praktijkervaring_met_dieren_dressuur = 4
ervaring_met_jongleren = 5
ervaring_met_acrobatiek = 5

# statement
naam = input('Wat is uw naam? ')
geslacht = input('Wat is uw geslacht? ')
start = 0

while start == 0:
    if geslacht.lower() == "man":
        man = input('Heeft u een snor? ')
        if man.lower() == 'nee':
            print('Ongeldige invoer')
            break
    elif geslacht.lower() == 'vrouw':
        vrouw = input('Heeft u rood krulhaar? ')
        if vrouw.lower() == 'nee':
            print('Ongeldige invoer')
            break
    elif geslacht.lower() == 'iets anders':
        iets_anders = input('Heeft u een brede glimlach? ')
        if iets_anders.lower() == 'ja':
            pass
        elif iets_anders.lower() == 'nee':
            print('Ongeldige invoer')
            break
    else:
        print('Ongeldig geslacht')
        break


    vrachtwagenrijbewijs = input('Bent u in het bezit van een vrachtwagenrijbewijs? (Ja/Nee)').lower()
    if vrachtwagenrijbewijs == 'ja':
        hoge_hoed = input('Heeft u een hoge hoed? (Ja/Nee)').lower()
        if hoge_hoed == 'ja':
            lengte = int(input('Hoe lang bent u in centimeters? '))
            if lengte >= 150:
                gewicht = int(input('Hoeveel weegt u in kilogram? '))
                if Min_gewicht <= gewicht <= Max_gewicht:
                    praktijkervaring_met_dieren_dressuur = int(input('Hoeveel jaren heeft u ervaring met dieren dressuur? '))
                    if praktijkervaring_met_dieren_dressuur >= 4:
                        ervaring_met_jongleren = int(input('Hoeveel jaren heeft u ervaring met jongleren? '))
                        if ervaring_met_jongleren >= 5:
                            ervaring_met_acrobatiek = int(input('Hoeveel jaren heeft u ervaring met acrobatiek? '))
                            if ervaring_met_acrobatiek >= 5:
                                print(f'Beste {naam},')
                                print('Gefeliciteerd! U mag solliciteren naar de functie van Circusdirecteur bij Circus HotelDeBotel.')
                            else:
                                print('Helaas, u voldoet niet aan alle criteria voor deze functie.')
                                print('U heeft niet genoeg ervaring met acrobatiek.')
                        else:
                            print('Helaas, u voldoet niet aan alle criteria voor deze functie.')
                            print('U heeft niet genoeg ervaring met jongleren.')
                    else:
                        print('Helaas, u voldoet niet aan alle criteria voor deze functie.')
                        print('U heeft niet genoeg ervaring met dieren dressuur.')
                else:
                    print('Helaas, u voldoet niet aan alle criteria voor deze functie.')
                    if gewicht < Min_gewicht:
                        print('U bent te licht.')
                    if gewicht > Max_gewicht:
                        print('U bent te zwaar.')
            else:
                print('Helaas, u voldoet niet aan alle criteria voor deze functie.')
                print('U bent te kort.')
        else:
            if hoge_hoed.lower() == 'nee':
                print('Helaas, u voldoet niet aan alle criteria voor deze functie.')
                print('U heeft geen hoge hoed.')
    elif vrachtwagenrijbewijs.lower() == 'nee':
        print('Helaas, u voldoet niet aan alle criteria voor deze functie.')
        print('U bent niet in het bezit van een vrachtwagenrijbewijs.')
    else:
        print('Ongeldige invoer.')


# if geslacht=='man':
#     man=input('heb je een snor ? ')
#     if man=='ja':
#         geschikt=True
#         pass
# elif geslacht=='vrouw':
#     vrouw=input('Heeft u rood krulhaar? ')
#     if vrouw== 'ja':
#         geschikt=True
#         pass
# elif geslacht == 'zeg ik lierven niet !':
#     zeg_ik_liever_niet= input('heb je een brede glimlach ? ')
#     if zeg_ik_liever_niet ==' ja':
#         geschikt=True





    