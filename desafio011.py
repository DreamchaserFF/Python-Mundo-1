largura = float(input("Favor informar a largura da parede em metros: "))
altura = float(input("Favor infromar a altura da parede em metros: "))
area = largura * altura
tinta = area / 2
print("Para pintar uma parede de {}m², serão necessários {} litros de tinta".format(area, tinta))
