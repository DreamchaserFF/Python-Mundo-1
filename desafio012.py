preco = float(input("Favor informar o preço do produto: "))
desconto = preco * 0.05
precoFin = preco - desconto
print("O preço do produto com desconto é de R${:.2f}".format(precoFin))