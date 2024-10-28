import math
catOp = float(input("Informe o comprimento do cateto oposto: "))
catAd = float(input("Informe o comprimento do cateto adjacente: "))
hip = math.hypot(catOp, catAd)
print("A hipotenusa vale {}".format(hip))