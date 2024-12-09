frase = "Exemplo" # Obter tamanho de um objeto
print(len(frase))  # Saída: 7

lista = [10, 20, 30] # Acessar elementos por índice
print(lista[1])  # Saída: 20

frase = "Python" # Fatiamento de sequências
print(frase[1:4])  # Saída: "yth"
print(frase[::-1])  # Saída: "nohtyP" (reverso)

frase = "Olá, mundo!" # Encontrar a posição de um valor
print(frase.find("mundo"))  # Saída: 5

lista = [1, 2, 3, 4]
print(lista.index(3))  # Saída: 2

frase = "banana" # Contar ocorrências
print(frase.count("a"))  # Saída: 3

frase = "Python" # Verificar valores com base no índice
print("P" in frase)  # Saída: True

frase = "teste" # Iterar com índices
for indice, letra in enumerate(frase):
    print(indice, letra)

# Remover elementos por índice
lista = [1, 2, 3]
del lista[1]
print(lista)  # Saída: [1, 3]

# Obter maior ou menor índice com valores
lista = [10, 20, 30]
print(max(lista))  # Saída: 30
print(lista.index(max(lista)))  # Saída: 2

# Inserir ou substituir valores por índice
lista = [1, 2, 3]
lista.insert(1, 99)
print(lista)  # Saída: [1, 99, 2, 3]

lista[2] = 42
print(lista)  # Saída: [1, 99, 42, 3]

frase = "hello world" # Substituir um termo por outro
print(frase.replace("hello", "goodbye"))

frase = "   hello world   " # Remove os espaços extras no inicio e fim
print(frase.strip())
print(frase.lstrip()) #remove os espaços da esquerda
print(frase.rstrip()) #remove os espaços da direita

frase = "My precious power ring, gone for ever!" # Divide a frase pelos espaços em diversas arrays
print(frase.split())

print("-".join(frase))