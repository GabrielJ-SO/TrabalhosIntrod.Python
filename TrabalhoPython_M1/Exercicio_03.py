

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))


imc = peso / (altura ** 2)

if(imc < 18.5):
    print("Abaixo do peso")
elif(imc >= 18.5 and imc < 25):
    print("Peso normal")
elif(imc >= 25 and imc < 30):
    print("Sobrepeso")
elif(imc >= 30 and imc < 35):
    print("Obesidade grau I")
elif(imc >= 35 and imc < 40):
    print("Obesidade grau II")
else:
    print("Obesidade grau III")