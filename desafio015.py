km = float(input("Quantos quilômetros foram rodados? "))
dias = int(input("Por quantos dias foi alugado? "))
valorKm = float(km * 0.15)
valorDia = float(dias * 60)
total = valorKm + valorDia
print("O total a ser pago é de R${:.2f}" .format(total))