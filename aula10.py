'''if carro.esquerda():
    bloco True
else:
    bloco False'''

'''tempo = int(input("Quantos anos tem o seu carro? "))
if tempo <= 3:
    print("Carro novo")
else:
    print("Carro velho")
print("--FIM--")'''

'''tempo = int(input("Quantos anos tem o seu carro? "))
print("Carro novo" if tempo <=3 else "Carro velho")
print("--FIM--")'''

'''nome = str(input("Qual é o seu nome? "))
if nome == "Eduardo":
    print("Que nome lindo você tem!")
else:
    print("Nome padrãozinho.")
print("Bom dia, {}!".format(nome))''' #Tem que sintaxar com os espaços corretamente

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print("Sua média foi {:.1f}".format(media))
if media >= 6:
    print("Parabéns, está acima da média.")
else:
    print("Estude mais.")