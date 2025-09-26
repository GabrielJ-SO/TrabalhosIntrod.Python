
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if(ano < 0):
    print("Data inválida!")

elif(mes < 1 or mes > 12):
    print("Data inválida!")

elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
    if(dia < 1 or dia > 30):
        print("Data inválida!")
    else:
        print("Data válida!")

elif(mes == 2):
    if(ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
        if(dia < 1 or dia > 29):
            print("Data inválida!")
        else:
            print("Data válida!")
    else:
        if(dia < 1 or dia > 28):
            print("Data inválida!")
        else:
            print("Data válida!")

else:
    if(dia < 1 or dia > 31):
        print("Data inválida!")
    else:
        print("Data válida!")