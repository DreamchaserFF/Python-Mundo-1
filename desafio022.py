nome = str(input("Digite seu nome completo: ")).strip()
print("Seu nome em letras minúsculas é {}".format(nome.lower()))
print("Seu nome em letras maiúsculas é {}".format(nome.upper()))
result = len(nome.replace(" ", "")) #tira todos os espaços do nome prieiro
#
print("Seu nome possui {} letras".format(result))
primeiroNome = nome[:nome.index(" ")] #começa no index 0 e termina no primeiro index de espaço
print("Seu primeiro nome é {} e ele tem {} letras" .format(primeiroNome, len(primeiroNome)))