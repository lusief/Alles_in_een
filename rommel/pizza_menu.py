pizza_menu = [
    {"naam": "Margherita", "diameter": 30, "ingrediënten": ["Tomatensaus", "Mozzarella kaas", "Verse basilicum", "Olijfolie"]},
    {"naam": "Pepperoni", "diameter": 35, "ingrediënten": ["Tomatensaus", "Mozzarella kaas", "Pepperoni plakjes"]},
    {"naam": "Quattro Stagioni", "diameter": 60, "ingrediënten": ["Tomatensaus", "Mozzarella kaas", "Champignons", "Artisjokken", "Ham", "Olijven"]},
    {"naam": "Prosciutto e Funghi", "diameter": 30, "ingrediënten": ["Tomatensaus", "Mozzarella kaas", "Ham", "Champignons"]},
    {"naam": "BBQ Chicken", "diameter": 35, "ingrediënten": ["Barbecuesaus", "Mozzarella kaas", "Gegrilde kip", "Rode ui", "Koriander"]},
    {"naam": "Diavola", "diameter": 40, "ingrediënten": ["Tomatensaus", "Mozzarella kaas", "Pikante salami", "Rode pepers"]},
    {"naam": "Quattro Formaggi", "diameter": 30, "ingrediënten": ["Tomatensaus", "Mozzarella kaas", "Gorgonzola", "Parmezaanse kaas", "Ricotta"]},
    {"naam": "Capricciosa", "diameter": 35, "ingrediënten": ["Tomatensaus", "Mozzarella kaas", "Ham", "Champignons", "Artisjokken", "Olijven", "Ansjovis"]},
    {"naam": "Vegetariana", "diameter": 40, "ingrediënten": ["Tomatensaus", "Mozzarella kaas", "Paprika", "Ui", "Courgette", "Olijven", "Artisjokken"]},
    {"naam": "Frutti di Mare", "diameter": 30, "ingrediënten": ["Tomatensaus", "Mozzarella kaas", "Garnalen", "Mosselen", "Inktvis", "Ansjovis", "Knoflook"]}
]
def get_diameter(pizza_menu):
    return pizza_menu['diameter']

grooteste_pizza = max(pizza_menu, key=get_diameter)
print(grooteste_pizza)
print()
gesorteerde_lijst = sorted(pizza_menu, key=get_diameter)
print(gesorteerde_lijst)
print()
for a in gesorteerde_lijst:
    print(f"{a['naam']}: {a['diameter']} ")
print()

for namen in pizza_menu:
    # namen.append(pi)
    print(f"{namen['naam']}: {namen['diameter']} ")
# pizza_menu_sorted = sorted(pizza_menu, key=lambda x: x['diameter'], reverse=True)