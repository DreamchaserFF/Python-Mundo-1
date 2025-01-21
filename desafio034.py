salario = float(input("Favor informar o seu salário: "))
if salario >= 1250:
    aumento = (salario / 100) * 10
    novo = salario + aumento
    print(f"O seu salário receberá um aumento de R${aumento}. Seu novo salário será R${novo}")
else:
    aumento = (salario / 100) * 15
    novo = salario + aumento
    print(f"O seu salário receberá um aumento de R${aumento}. Seu novo salário, será de R${novo}")