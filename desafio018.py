import math
angulo = float(input("Favor, informe o ângulo: "))
rad = math.radians(angulo)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)
print("O seno do ângulo de {}° é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}".format(angulo, seno, cosseno, tangente))