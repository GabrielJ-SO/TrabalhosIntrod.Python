cartasGab = ['B', 'C', 'D','A']
pontuacao = 0

cartas = input("Digite a sequência de 4 cartas:")
cartas = cartas.upper()
cartas = list(cartas)
i = 0

for carta in cartas:
   if carta == cartasGab[i]:
      pontuacao += 10
   if carta == 'A':
      pontuacao += 5 
   if carta == 'C' and cartas[i + 1] == 'D':
      pontuacao += 5
   i += 1

print("A sequência de cartas era",cartasGab, "\n")
print("Pontuação final:", pontuacao, "\n")