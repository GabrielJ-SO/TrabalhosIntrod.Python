salario = float(input("Digite o seu salário:"))
tempo = int(input("Digite o tempo de empresa:"))

if salario < 2000 and tempo >= 5:
    bonus = salario * 0.2

elif salario < 2000 and tempo < 5:
    bonus = salario * 0.1

elif salario >= 2000 and tempo >= 5:
    bonus = salario * 0.05

elif salario >= 2000 and tempo < 5:
    bonus = salario * 0
    
else:
    salario = salario * 0

salario += bonus

print("O seu salário é:", salario)