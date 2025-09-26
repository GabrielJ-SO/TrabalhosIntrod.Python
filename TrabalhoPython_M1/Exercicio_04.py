media = 0

for i in range(3):
    nota = float(input(f"Digite a  {i+1}° nota: "))
    if(nota == 0):
        break
    media +=  nota
media = media / 3

if(media >= 7):
    print("Aluno aprovado!")
elif(media >= 5 and media < 7):
    print("Aluno em recuperação!")
elif(media < 5):
    print("Aluno reprovado!")