import random
numero = random.randint(1,5)
chute = int(input("Escolha um numero de 1 a 5: "))
if chute <= 5 and chute >= 1:
    if chute == numero:
        print("Parabéns, o numero era mesmo {}".format(numero))
    else:
        print("Você errou. O numero correto era {}".format(numero))
else:
    print("Você precisa escolher um numero de 1 a 5")