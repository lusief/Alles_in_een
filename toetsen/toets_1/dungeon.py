import time, math, random

player_attack = 2
player_defense = 1
player_health = 3
sleutel = 0
aantal_rupee = 0
schild = 0
bom = 0
dolk = 0
bos_key = 0
log_boek = ''
kamers = [0] * 16
kamers [1] += 1
lange_trap = 0

# === [kamer 1] === #
if kamers [1]:
    log_boek += 'Dungeon binne gelopen\n'
    print('Door de twee grote deuren loop je een gang binnen.')
    print('Het ruikt hier muf en vochtig.')
    print('Je ziet een deur voor je.')
    log_boek += 'Loopt naar de eerste kamer van de dungeon\n'
    kamers [7] += 1
    print('')
    time.sleep(1)

# === [kamer 7] === #
if kamers [7] == 1:
    betoverde_kamer = random.randint(1,10)
    print('Je loopt binne je voet magie in de lucht')
    print('Blijkbaar heeft een euwen oud tovenaar heeft de kamer  betoverd')
    if betoverde_kamer != 5:
        print ('Je vindt een rupee in het kamer je pakt hem op en\nLoop door naar de volgende deur')
        aantal_rupee += 1
        print(f'Je hebt nu {aantal_rupee} rupees')
        log_boek += 'Je hebt een rupee gevoneden\n'
    else:
        print('Je loop met lege handen door') 
    print('In het kamer zie je twee deuren elke met zijn numer der boven op 2/8.')
    speler = input('Je denkt welke deur nu? 2 of 8? ').lower()
    if speler in ['2','8']:
        if speler == '8' or speler == '2':
            kamers [int(speler)] += 1
            log_boek += f'Je kooz om naar kamer {speler} te gaan\n'
            print('')
            time.sleep(1)

# === [kamer 2] === #
if kamers [2] == 1:
    RANDOM_1, RANDOM_2 = random.randint(10, 25), random.randint(10, 25)
    RANDOM_3, RANDOM_4 = random.randint(-5, 76), random.randint(-5, 76)
    antwoord_1 = RANDOM_1 + RANDOM_2
    antwoord_2 = RANDOM_3 - RANDOM_4
    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Het standbeeld heeft een rupee vast.')
    print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
    vraag_1_input = int(input(f'Daarboven zie je een som staan {RANDOM_1} + {RANDOM_2} = ? {antwoord_1} '))
    vraag_2_input = int(input(f'Daarboven zie je een som staan {RANDOM_3} - {RANDOM_4} = ? {antwoord_2} '))
    if vraag_1_input == antwoord_1 and vraag_2_input == antwoord_2:
        aantal_rupee += 1
        print(f'Je hebt nu {aantal_rupee} rupees')
        print('Het standbeeld laat de rupee vallen en je pakt het op.')
        log_boek += 'Je hebt de raadsel geraaden\nJe kreeg 1 rupee\n'
    else:
        print('Je hoort een geluid komet uit de kamer acht de deur met nummer 6')
        lange_trap += 1
        log_boek += 'Er komt geluid uit kamer 6\n'
    print('Je ziet nu twee deuren elke met zijn nummer der boven op 6/8.')
    speler = input('Je denkt welke deur nu? 6 of 8? ').lower()
    if speler in ['6','8']:
        if speler == '8' or speler == '6':
            kamers [int(speler)] += 1
            log_boek += f'Je loopt door naar de kamer {speler}\n'
            print('')
            time.sleep(1)

# === [kamer 6] === #
if kamers [6] == 1:
    zombie_attack = 1
    zombie_defense = 0
    zombie_health = 2
    print('Dapper loop je de kamer binnen.')
    print('Je loopt tegen een zombie aan.')

    zombie_hit_damage = (zombie_attack - player_defense)
    if zombie_hit_damage <= 0:
        print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
        log_boek += 'Je hebt goed verdedigd tegen de zombie\n'
    else:
        zombie_attack_amount = math.ceil(player_health / max(1,zombie_hit_damage))
        
        player_hit_damage = (player_attack - zombie_defense)
        player_attack_amount = math.ceil(zombie_health / player_hit_damage)

        if player_attack_amount < zombie_attack_amount:
            health_damig = player_attack_amount * zombie_hit_damage
            player_health -= health_damig
            log_boek += 'Je hebt de zombie verslaan!\n'
            log_boek += f'Je health is {player_health}\n'
            print(f'In {player_attack_amount} rondes versla je de zombie.')
            print(f'Je health is nu {player_health}.')
            print('Na dat je de zombie verslaat krijg je een drop item')
            print('"""""""""""""Sleutel""""""""""""""')
        else:
            print('Helaas is de zombie te sterk voor je.')
            print('Game over.')
            log_boek += 'Je health is',player_health,'je bent dood gegaan!!\n'
            print(log_boek)
            exit()  
    sleutel += 1
    log_boek += 'Je hebt een sleutel gevonden\n'
    if lange_trap == 1:
        deur_bericht = 'Je ziet nu drie deuren elke met zijn nummer der boven op 3/8/, en een zonder nummer .'
        log_boek += 'Je kijkt eerst bij het deur zonder nummer\n'
        print('Je kijkt eerst bij het deur zonder nummer')
        print('Je deuwt de deur open ')
        print('Je ziet een super lange trap')
        spaler = input('Je denk zou ik dat lange trap lopen? ').lower()
        if spaler == 'ja':
            log_boek += 'Je hebt gekozen om de super lange trap om te lopen\n'
            print('Je begint de trap op te lopen')
            print('aan het einde van de trap zie je een deur met nummer 15 je deut de deur open')
            kamers [15] += 1
            print('')
            time.sleep(1)
            log_boek += 'Je loopt kamer 15 binnen\n'
        else:
            print('Je loopt terug naar de kamer 6')
    else:
        print('Je ziet nu twee deuren elk met zijn nummer erboven, 3/8.')
        log_boek += 'Je kiest tussen 2 deuren\n'
    log_boek += 'Je hebt gekozen om de lange trap nit op te gaan\n'
    log_boek += 'Je loopt terug naar klamer 6\n'
    speler = input('Je denkt welke deur nu? 3 of 8? ').lower()
    if speler in ['3','8']:
        if speler == '3' or speler == '8':
            kamers [int(speler)] += 1
            log_boek += f'Je hebt gekozen om kamer {speler} binnen te lopen\n'
            print('')
            time.sleep(1)

# ==[kamer 15]== #
if kamers [15] == 1:
    print('Je loopt binne je ziet een balista in het miden van de kamer gericht op een raam')
    print('Naast de het raam is een deur met nummer 10 boven op ')
    print('Je kijk eerst uit het raam en je ziet een arch demon binne zitten')
    print('Je bvegint te denken om wat nu te doen')
    speler = input('Ga ik de balist gebruiken of loop ik naar de binne om tegen de arch demon te vechte? ').lower()
    if speler == 'gebruik balista' :
        log_boek += 'Je hebt gekozen om de balista te gebruiken om de Arch demon te doden\n'
        print('Met een hard knalende geluid wordt een groote pijl tegen de arch demon geschoten')
        print('De archt demon schriuet van pijn en gaat dood')
        print('en de deur daar naast brast open')
        kamers [5] += 1
        print('')
        time.sleep(1)
    else:
        print('Je deut de deur met naar de arch demon open ')
        log_boek += 'je kooz om gelijk tegen de Arch demon te vechten\n'
        kamers [10] += 1
        print('')
        time.sleep(1)

# == [kamer 8] == #
if kamers [8] == 1:
    dobelsteen_1 = random.randint(1,6)
    dobelsteen_2 = random.randint(1,6)
    print('Je de duwt de deur open en loopt een lange kamer binne')
    print('in het lange kamer is er een goblin')
    black_goblin =input('Hij vraagt jou als je met hem wilt gokken? ').lower()
    if black_goblin == 'ja':
        print('Laat we dan gelijk beginnen')
        print('Je gooit met de dobelsteens')
        totaal_nummer_dobelseen = dobelsteen_1 + dobelsteen_2
        log_boek += f'Je hebt {totaal_nummer_dobelseen} gerold\n'
        if totaal_nummer_dobelseen > 7:
            rupee_verdubeling = (aantal_rupee * 2)
            antaal_rupee = rupee_verdubeling
            log_boek += 'Je rupees zijn verdubelt\n'
        elif totaal_nummer_dobelseen == 7:
            aantal_rupee += 1
            player_health += 4
            log_boek += 'Je 1 rupee gekregen\n'
            log_boek += f'Je health nu is {player_health}\n'
        elif totaal_nummer_dobelseen < 7:
            player_health -= 1
            log_boek += f'Je heath is met 1 punt lager gegaan je health nu is {player_health}\n'
            print(f'Maar je health is vermindert met 1 punt!')
        print(f"Je hebt {totaal_nummer_dobelseen} in totaal gerold")
        print(f'Je heb nu {aantal_rupee} rupes')
    else :
        print('Dan niet!!')
        log_boek += 'Je kooz om niet te goken met de Goblien'
    print('Je ziet nu drie deuren elke met zijn nummer der boven op 3/9/14.')
    speler = input('Je denkt welke deur nu? 3 of 9 of 14? ').lower()
    if speler in ['3','9','14']:  
        if speler == '3' or speler == '9' or speler == '14':
            kamers [int(speler)] += 1
            log_boek += f'Je kooz om kamer {speler} binnen te lopen\n'
            print('')
            time.sleep(1)

# == [kamer 14] == #
if kamers [14] == 1:
    print('je dwut de deur open en loopt binnen')
    print('Mindden in de kamer zweveft een zwarte sleutel')
    print ('je pakt hem op en je houdt hem bij')
    bos_key += 1
    log_boek += 'Je hebt een zwarte sleutel gevonden\n'
    kamers [9] += 1
    log_boek += 'Je loopt nu naar kamer nummer 9\n'
    print('')
    time.sleep(1)

# == [kamer 9] == #
if kamers [9] == 1:
    blessings = ['defense', 'health']
    random_blessing = random.choice(blessings)
    print('Je duwt de deur open en loopt een lange kamer binnen.')
    print('Aan het einde van de kamer zie je een glanzende witte deur.')
    print('Het glanst zo fel dat je het van ver kunt zien.')
    print('Je rent daarheen.')
    print('Je duwt de deur open.')
    if random_blessing == 'defense':
        player_defense += 1
        log_boek += 'Je hebt de belssing van defense gekregen\n'
        log_boek += f'Je defense is met 1 punt hoger gegaan\nJe defense nu is {player_defense}\n'
        print('Je voelt een kracht om je heen die je verdediging versterkt. Verdediging +1')
    elif random_blessing == 'health':
        player_health += 2
        log_boek += f'Je health is met 2 punt hoger gegaan\nJe health nu is {player_health}\n'
        print('Je voelt een genezende kracht die je gezondheid herstelt. Gezondheid +2')
    print('Je ziet nu twee deuren elke met zijn nummer der boven op 3/4.')
    speler = input('Je denkt welke deur nu? 3 of 4? ').lower()
    if speler in ['3','4']:
        if speler == '3' or speler == '4':
            kamers [int(speler)] +=1
            log_boek += f'Je kooz om kamer {speler} binnen te lopen\n' 
            print('')
            time.sleep(1)

# === [kamer 3] === #
def payitem(player_choice, player_defense, schild, aantal_rupee, player_attack, bom):
    items_to_buy = player_choice.split(" en ")
    for item in items_to_buy:
        if 'schild' == item:
            player_defense += 1
            schild += 1
            aantal_rupee -= 1
        elif 'dolk' == item:
            player_attack += 1
            aantal_rupee -= 1
        elif 'bom' == item:
            bom += 1
            aantal_rupee -= 1
        else:
            print(f"Unknown item: {item}")
    return player_attack, player_defense, schild, bom, aantal_rupee
if kamers[3] == 1:
    items = ['schild', 'dolk', 'bom']
    print('Je duwt hem open en stapt een hele lange kamer binnen.')
    print(f'In deze kamer staat een tafel met daarop een {" en ".join(items)}')
    print('Vanonder de tafel springt een goblin en schreeuwt ooooi!!')
    print('De items op de tafel zijn niet zomaar aan te raken, maar wel te koop.')
    print(f'Ik voel dat je {aantal_rupee} rupees hebt!')
    if aantal_rupee >= 3:
        player_choice = input('Wil je alle items kopen? ').lower()
        if player_choice == 'ja':
            player_attack += 1
            player_defense += 1
            schild += 1
            bom += 1
            aantal_rupee -= 3
            log_boek += 'Je hebt gekozen om alle items te kopen\n'
        else:
            player_choice = input(f'wat wil je hebben dan? {" of ".join(items)}? ').lower()
            result = payitem(player_choice, player_defense, schild, aantal_rupee, player_attack, bom)
            player_attack, player_defense, schild, bom, aantal_rupee = result
            log_boek += f'Je hebt een {player_choice} gekocht\n'
    elif aantal_rupee == 2:
        player_choice = input('Welke 2 items wil je hebben? (bijv. "bom en schild") ').lower()
        result = payitem(player_choice, player_defense, schild, aantal_rupee, player_attack, bom)
        player_attack, player_defense, schild, bom, aantal_rupee = result
        log_boek += f'Je hebt twee items gekocht {player_choice}\n'
    elif aantal_rupee == 1:
        print('En elke item kost 1 rupee')
        while True:
            player_choice = input(f'Dus welke wil je hebben? {" of ".join(items)}? ').lower()
            if player_choice in items:
                result = payitem(player_choice, player_defense, schild, aantal_rupee, player_attack, bom)
                player_attack, player_defense, schild, bom, aantal_rupee = result
            else:
                print('Je kan maar 1 item kopen')
                log_boek += 'Je probeert meer dan 1 item te kopen\n'
    else:
        print('Je hebt niet genoeg rupees!')
        log_boek += 'Je had geen genoeg rupees om ites te kopen\n'
    print('Je ziet nu drie deuren elk met zijn nummer erboven: 4/11.')
    speler = input('Je denkt welke deur nu? 4 of 11? ').lower()
    if speler in ['4','11']:
        if speler == '4' or speler == '11':
            kamers[int(speler)] += 1
            log_boek += f'Je hebt gekoezen om kamer {speler} binnen te lopen\n'
            print('')
            time.sleep(1)

# === [kamer 11] === #
if kamers[11] == 1:
    print('Je duwt de deur open.')
    print('Je ziet een hele lange kamer gevuld met stambuizen.')
    print('Je loopt enkele stappen binnen, en de deuren sluiten zich achter je.')

    log_boek += 'Je duwt de deur open.\n'
    log_boek += 'Je ziet een hele lange kamer gevuld met stambuizen.\n'
    log_boek += 'Je loopt enkele stappen binnen, en de deuren sluiten zich achter je.\n'

    if schild == 1:
        print('Je loopt door, en plotseling beginnen de stambuizen pijlen op je af te schieten.')
        print('Gelukkig heb je een schild gekocht.')
        print('Anders was je nu al dood.')
        print('Je ziet een lange deur en duwt hem open.')
        kamers[10] += 1
        log_boek += 'Door een schild overleef je de kamer die vol zit met vallen.\n'
        log_boek += 'Je loopt door naar de deur met nummer 10.\n'
    elif schild != 1:
        print('Je loopt naar binnen.')
        print('Je voelt dat de kamer te rustig is.')
        print('Je begint door de kamer te lopen.')
        print('Na enkele stappen beginnen de stambuizen te bewegen.')
        print('Ze beginnen jou te bekogelen met pijlen.')
        print('Je probeert te rennen maar...')
        print('Je wordt geschoten in je been en in je arm.')
        print('Je denkt: "Ik ben nu al dood. Ik heb geen kans meer."')
        print('""""""""""""""" Game Over """""""""""""""')
        print(log_boek)
        exit()
        print('')
        time.sleep(1)
# === [kamer 4] === #
if kamers[4] == 1:
    zombie_bos_attack = 2
    zombie_bos_defense = 0
    zombie_bos_health = 3
    print('Dapper loop je de kamer binnen.')
    print('Je loopt tegen een zombie bos aan.')
    log_boek += 'Dapper loop je de kamer binnen.\n'
    log_boek += 'Je loopt tegen een zombie bos aan.\n'
    
    zombie_bos_hit_damage = max(0, zombie_bos_attack - player_defense)

    if zombie_bos_hit_damage <= 0:
        print('Jij hebt een te goede verdediging voor de zombie, hij kan je geen schade doen.')
        log_boek += 'Jij hebt een te goede verdediging voor de zombie, hij kan je geen schade doen.\n'
    else:
        zombie_bos_attack_amount = math.ceil(player_health / (1, zombie_bos_hit_damage))
        player_hit_damage = max(0, player_attack - zombie_bos_defense)
        player_attack_amount = math.ceil(zombie_bos_health / (1, player_hit_damage))

        if player_attack_amount < zombie_bos_attack_amount:
            health_damage = player_attack_amount * zombie_bos_hit_damage
            player_health -= health_damage
            print(f'In {player_attack_amount} rondes versla je de zombie.')
            log_boek += f'In {player_attack_amount} rondes versla je de zombie.\n'
        else:
            print('Helaas is de zombie te sterk voor je.')
            print('Game over.')
            log_boek += 'Helaas is de zombie te sterk voor je.\nGame over.\n'
            exit()
    print("Je ziet drie deuren elke met zijn nummer er bovenop: 10/12/13")
    log_boek += "Je ziet drie deuren elke met zijn nummer er bovenop: 10/12/13\n"
    speler = input('Je denkt welke deur nu? 10 of 12 of 13? ').lower()
    if speler in ['12', '13', '10']:
        if speler == '12' or speler == '13':
            kamers[int(speler)] += 1
            print('')
            time.sleep(1)
            log_boek += f'Je hebt gekozen om kamer {speler} binnen te lopen.\n'
        elif speler == '10':
            if bos_key == 1 or bom == 1:
                print('Je gebruikt de zwarte sleutel om de kamer binnen te lopen')
                kamers[10] += 1
                print('')
                time.sleep(1)
                log_boek += f'Je hebt gekozen om kamer {speler} binnen te lopen.\n'
            elif bos_key == 0 and bom == 1:
                print('Je probeert de deur open te maken maar het lukt je niet')
                print('Je loopt paar stappen naar achteren en gooit met de bom naar de deur!')
                print('......Boooom!!!!')
                print('De deur gaat open en je loopt naar binnen')
                kamers[10] += 1
                print('')
                time.sleep(1)
                log_boek += 'Je hebt de deur met een bom geopend en bent naar binnen gelopen.\n'
            else:
                print('Je hebt geen zwarte sleutel en geen bom, dus je kan maar alleen deur 12 openen.')
                kamers[12] += 1
                log_boek += 'Je hebt geen zwarte sleutel en geen bom, dus je kan maar alleen deur 12 openen.\n'
                print('')
                time.sleep(1)
# == [kamer 13] == #
if kamers[13]:
    if bom == 1:
        print('Je maakt de hek open met een bom naar toe te gooien')
        print('Je vindt binnen een zwaard. Je pakt het en houdt het bij je.')
        player_attack += 2
        log_boek += 'Je hebt het hek vernietigd met een bom\nJe vindt achter het hek een zwaard.\n'
        log_boek += f'Je aanval is nu met 2 punten gestegen\nJe aanval is nu {player_attack}.\n'
    else:
        print('Je kon het hek niet openen en je loopt weg.')
        log_boek += 'Je kon het hek niet openen en je loopt weg.'
        print('Je ziet dat er nu nog twee deuren zijn: 10 en 12')
    if bos_key == 1:
        speler = input('Welke deur ga je binnen? 10 of 12? ')
        if speler in ['10', '12']:
            kamers[int(speler)] += 1
            print('')
            time.sleep(1)
            log_boek += f'Je hebt gekozen om kamer {speler} binnen te gaan.\n'
    else:
        print('Je hebt geen zwarte sleutel en geen bom, dus je kan maar alleen deur 12 openen.')
        kamers[12] += 1
        log_boek += 'Je hebt geen bos sleutel, dus je gaat automatisch naar kamer 12.\n'
        print('')
        time.sleep(1)

# == [kamer 12] == #
if kamers[12] == 1:
    print('Zodra dat je de deur opent voel je gelijk dat je in de lucht hangt')
    print('En hierbij val je tot je dood')
    print(""""""""""""" Game Over """"""""""""")
    log_boek += 'Zodra dat je de deur opent voel je gelijk dat je in de lucht hangt.\n'
    log_boek += 'En hierbij val je tot je dood.\n'
    log_boek += '"""""""""" Game Over """"""""""""\n'
    print(log_boek)
    exit()
    print('')
    time.sleep(1)

# == [kamer 10] == #
if kamers[10] == 1:
    demon_attack = 3
    demon_defense = 1
    demon_health = 5
    print('Dapper loop je de kamer binnen.')
    print('Je loopt tegen een arch demon aan.')
    log_boek += 'Dapper loop je de kamer binnen.\n'
    log_boek += 'Je loopt tegen een arch demon aan.\n'
    demon_hit_damage = max(0, demon_attack - player_defense)

    if demon_hit_damage <= 0:
        print('Jij hebt een te goede verdediging voor de Arch demon, hij kan je geen schade doen.')
        log_boek += 'Jij hebt een te goede verdediging voor de zombie, hij kan je geen schade doen.\n'
    else:
        zombie_bos_attack_amount = math.ceil(player_health /  demon_hit_damage)
        player_hit_damage = max(0, player_attack - demon_defense)
        if player_hit_damage > 0:
            player_attack_amount = math.ceil(demon_health /  player_hit_damage)

        if player_attack_amount < zombie_bos_attack_amount:
            health_damage = player_attack_amount * demon_hit_damage
            player_health -= health_damage
            print(f'In {player_attack_amount} rondes versla je de zombie.')
            log_boek += f'In {player_attack_amount} rondes versla je de zombie.\n'
            kamers [5] += 1
            print('')
            time.sleep(1)
        else:
            print('Helaas is de zombie te sterk voor je.')
            print('Game over.')
            log_boek += 'Helaas is de zombie te sterk voor je.\nGame over.\n'
            print(log_boek)
            exit()

# === [kamer 5] === #
if kamers[5] == 1:
    print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
    print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
    print('Je loopt er naartoe.')

    log_boek += 'Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.\n'
    log_boek += 'Tot je verbazing zie je een schatkist in het midden van de kamer staan.\n'
    log_boek += 'Je loopt er naartoe.\n'

    if sleutel == 1:
        print('Met de sleutel open je de kist en versla je de Dungeon.')
        log_boek += 'Met de sleutel open je de kist en versla je de Dungeon.\n'
    elif bom == 1:
        print('Je gooit de bom naar de kist.')
        print('De kist kraakt open!!')
        print('Je overleeft de Dungeon.')
        log_boek += 'Je gooit de bom naar de kist.\n'
        log_boek += 'De kist kraakt open!!\n'
        log_boek += 'Je overleeft de Dungeon.\n'
        print(log_boek)
    else:
        print('Je kon de Dungeon niet verslaan.\n""""""""""GAME OVER""""""""""')
        log_boek += 'Je kon de Dungeon niet verslaan.\n""""""""""GAME OVER""""""""""\n'
        print(log_boek)
        exit()

