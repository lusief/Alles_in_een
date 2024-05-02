massa = float(input("gewicht?"))
lengte =float(input("lengte?"))

bmi =massa /(lengte*lengte)


print(round(bmi, 1))

if bmi <18:
    print("ondergewicht")
elif bmi >=25: # bmi >=18 and bmi<= 25
    print("gezond")
else:
    print("overgewicht")