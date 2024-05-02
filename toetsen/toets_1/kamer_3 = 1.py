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
# if player_health <= 0:
#     print('Je bent dood gegaan je health is',player_health)
#     print('""""""""""""Game over""""""""""""')
#     exit()

log_boek = ''

kamers = [0] * 16
kamers [6] += 1
lange_trap = 0



if kamers [6] == 1:
    zombie_attack = 1
    zombie_defense = 0
    zombie_health = 2
    print('Dapper loop je de kamer binnen.')
    print('Je loopt tegen een zombie aan.')
    zombie_hit_damage = (zombie_attack - player_defense)
    if zombie_hit_damage <= 0:
        print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
        print('Na dat je de zombie verslaat krijg je een drop item')
        print('"""""""""""""Sleutel""""""""""""""')
        log_boek += 'Je hebt goed verdedigd tegen de zombie\n'
    else:
        zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
        
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