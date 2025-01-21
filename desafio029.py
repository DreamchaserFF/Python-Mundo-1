vel = float(input("Informe a velocidade do carro em Km/h: "))
multa = (vel - 80) * 7
if vel > 80:
    print("Você estava acima da velocidade permitida. Sua multa é de: R${:.2f}".format(multa))
else:
    print("Tudo certo. Prossiga.")