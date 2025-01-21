linha1 = float(input("Informe o cumprimento da primeira linha: "))
linha2 = float(input("Informe o cumprimento da segunda linha: "))
linha3 = float(input("Informe o cumprimento da terceira linha: "))
if (linha2 + linha3) > linha1 and (linha1 + linha3) > linha2 and (linha1 + linha2) > linha3:
    print("As três linhas formam um triangulo.")
else:
    print("As três linhas não formam um triangulo.")