import time, math, random



# kamer_2 = 0
# kamer_3 = 0
# kamer_4 = 1
# kamer_5 = 0
# kamer_6 = 0
# kamer_7 = 0
# kamer_8 = 0
# kamer_9 = 0
# kamer_10 = 0
# kamer_11 = 0
# kamer_12 = 0
# kamer_13 = 0
# kamer_14 = 0
# kamer_15 = 0





# # === [kamer 4] === #
# if kamer_4 ==1:
#     zombie_bos_attack = 2
#     zombie_bos_defense = 0
#     zombie_bos_health = 3
#     print('Dapper loop je de kamer binnen.')
#     print('Je loopt tegen een zombie bos aan.')

#     zombie_bos_hit_damage = (zombie_bos_attack - player_defense)
#     if zombie_bos_hit_damage <= 0:
#         print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
#         print ("Je ziet drie deuren elke met zijn nummer der boven op 10/12/13")
#         spaler = input('Je denkt welke kant nou? ').lower()
#         if spaler == '12' :
#             kamer_12 += 1
#         elif spaler == '13' and bom == 1 :
#             print('Je makt de hek open met een bom naar toe te gooien')
#             print('Je vindt binne een zwaard je pakt hem houdt hem bij je')
#             player_attack += 2
#             if bos_key == 1:
#                 print('Na dat je de zwaard hebt gepakt loop je de kleine kamer der uit')
#                 print('je ziet nu twee deuren een met nummer 10 en andere met nummer 12')
#                 spaler = input('welke deur ga je?')
#                 if spaler == '10':
#                     print('Na dat je de zwaard hebt gepakt je loopt naar de deur naast je met nummer 10 ')
#                     kamer_10 += 1
#                 elif spaler == '12':
#                     kamer_12 += 1
#             elif bos_key == 0 :
#                 print('Je loopt naar deur rechts van je met nummer 10 ')
#                 print('Je probeert de deur open te maken maar krijg je hem toch niet open')
#                 print('Dus je loopt naar de ander deur met nummer 12')
#                 print('Je dwut de deur open')
#                 kamer_12 +=1
#         elif spaler == '10':
#             if bos_key == 1:
#                 print('Je dewt de deur open')
#                 kamer_10 += 1
#             elif bos_key == 0 and bom == 1 :
#                 print('Je probeert de deur open te maken maar het lukt je niet')
#                 print('Je loopt paar stapen naar acht en gooit met de bom naar de deur!')
#                 print('......Boooom!!!!')
#                 print('De deur gaat open en je loopt naar binne')
#                 kamer_10 += 1
#     else:
#         zombie_bos_attack_amount = math.ceil(player_health / zombie_bos_hit_damage)
        
#         player_hit_damage = (player_attack - zombie_bos_defense)
#         player_attack_amount = math.ceil(zombie_bos_health / player_hit_damage)

#         if player_attack_amount < zombie_bos_attack_amount:
#             health_damig = player_attack_amount * zombie_bos_hit_damage
#             player_health -= health_damig
#             print(f'In {player_attack_amount} rondes versla je de zombie.')
#             print ("Je ziet drie deuren elke met zijn nummer der boven op 10/12/13")
#             spaler = input('Je denkt welke kant nou? ').lower()    
#             if spaler == '12' :
#                 kamer_12 += 1
#             elif spaler == '13' and bom == 1 :
#                 print('Je makt de hek open met een bom naar toe te gooien')
#                 player_attack += 2
#                 if bos_key == 1:
#                     print('je ziet nu twee deuren een met nummer 10 en andere met nummer 12')
#                     spaler = input('welke deur ga je?')
#                     if spaler == '10':
#                         print('Na dat je de zwaard hebt gepakt je loopt naar de deur naast je met nummer 10 ')
#                         kamer_10 += 1
#                     elif spaler == '12':
#                         kamer_12 += 1
#                 elif bos_key == 0 :
#                     print('Je loopt naar deur rechts van je met nummer 10 ')
#                     print('Je probeert de deur open te maken maar krijg je hem toch niet open')
#                     print('Dus je loopt naar de ander deur met nummer 12')
#                     print('Je dwut de deur open')
#                     kamer_12 +=1
#             elif spaler == '10':
#                 if bos_key == 1:
#                     print('Je dewt de deur open')
#                     kamer_10 += 1
#                 elif bos_key == 0 and bom == 1 :
#                     print('Je probeert de deur open te maken maar het lukt je niet')
#                     print('Je loopt paar stapen naar acht en gooit met de bom naar de deur!')
#                     print('......Boooom!!!!')
#                     print('De deur gaat open en je loopt naar binne')
#                     kamer_10 += 1    
#         else:
#             print('Helaas is de zombie te sterk voor je.')
#             print('Game over.')
#             exit()
#     print('')
#     time.sleep(1)
player_attack = 2
player_defense = 1
player_health = 3
sleutel = 0
aantal_rupee = 3
schild = 0
bom = 0
dolk = 0
bos_key = 0
log_boek = ''
kamers = [0] * 16
kamers [1] += 1
lange_trap = 0

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

kamers[3] += 1

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
            
print(bom)
print(schild,player_defense)
print(dolk,player_attack)
print(aantal_rupee)
if speler == '4':
    print('A')

if speler == '11':
    print('B')