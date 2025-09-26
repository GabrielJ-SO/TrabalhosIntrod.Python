lado1 = float(input("Lado 1:"))
lado2 = float(input("Lado 2:"))
lado3 = float(input("Lado 3:"))

if (lado1 + lado2 < lado3) or (lado2 + lado3 < lado1) or (lado1 + lado3 < lado2):
    print("As medidas fornecidas não forma um triângulo.")
    
elif lado1 == lado2 and lado3 == lado1:
    print("O triângulo é equilátero.")

elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
    print("O triângulo é escaleno.")

else:
    print("O triângulo é isósceles.")