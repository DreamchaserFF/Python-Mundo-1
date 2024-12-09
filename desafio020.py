import random
aluno1 = input("Informe o nome do 1° aluno: ")
aluno2 = input("Informe o nome do 2° aluno: ")
aluno3 = input("Informe o nome do 3° aluno: ")
aluno4 = input("Informe o nome do 4° aluno: ")
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print("A ordem de apresentação é: {}".format(lista))