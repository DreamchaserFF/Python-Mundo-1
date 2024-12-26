frase = str(input("Digite uma frase: ")).strip().lower()
print("A frase informada possui {} letras A's.".format(frase.count("a")))
print("A primeira letra A aparece na posição {}".format(frase.find("a")+1))
print("A ultima letra A aparece na posição {}".format(frase.rfind("a")+1))