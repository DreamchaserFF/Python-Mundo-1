nome = str(input("Digite seu nome completo: ")).strip()
lista = nome.split()
print("O seu primeiro nome é {}".format(lista[0]))
print("O seu ultimo nome é {}".format(lista[len(lista)-1]))