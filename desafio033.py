num1 = float(input("Informe o primeiro numero: "))
num2 = float(input("Informe o segundo numero: "))
num3 = float(input("Informe o terceiro numero: "))
if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

if num1 <= num2 and num1 <= num3:
    menor = num2
elif num2 <= num1 and num2 <= num1:
    menor = num2
else:
    menor = num3

print(f"O menor número é {menor} e o maior é {maior}")