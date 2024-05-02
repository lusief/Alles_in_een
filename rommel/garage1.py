from garage import autos
print(f"ik heb {len(autos)}auto's in mijn garage")
aantal_ferrari =0
for auto in autos:
    if auto ['merk'] =='ferrari':
        aantal_ferrari +=1
print(f"ik heb {aantal_ferrari} ferrari's in mijn garage")

def get_Moter_size(a):
    return a['motor_inhoud']
def get_Max_letter(b):
    return len(b["model"])

# print(len(autos["model"]))
langste_naam= max  (autos, key= get_Max_letter)
print(langste_naam)
langste_naam2= max  (autos, key=lambda b:len(b['model']))
print(langste_naam2)                
                     
langste_naam3= min  (autos, key=lambda s:len(s['merk']))
print(langste_naam3) 


kleinste_moter =min (autos, key= get_Moter_size)
kleinste_moter2 = min (autos, key=lambda a: a['motor_inhoud'])
print (kleinste_moter2)
print (kleinste_moter)

