import math
prestiges = int(input("Prestiges:  "))
if prestiges >= 0 and prestiges <= 99:
    increase = float(math.floor(prestiges/20))/10
elif prestiges >= 100 and prestiges <= 179:
    increase = float(math.floor((99)/20))/10
    print(increase)
    increase = float(math.floor((99)/20))/10 + float(math.floor((prestiges-99)/20))/10 * 4
    print(increase)
cost = (prestiges * 2500000)  + ((prestiges * increase) * 2500000) + 2500000
print(cost)