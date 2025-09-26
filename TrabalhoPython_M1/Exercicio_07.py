
idade =  int(input("Digite sua idade: "))
renda = float(input("Digite sua renda mensal: "))
dividas = float(input("Digite o valor total de suas dívidas: "))

if(renda >= 5000 and dividas < (renda * 0.3)):
    print("Risco Baixo")
elif(renda <= 5000 and dividas <= (renda * 0.5)):
    print("Risco Médio")
elif(renda < 2000  and dividas > (renda * 0.5)):
    print("Risco Alto")
else:
    print("Risco Médio-baixo")