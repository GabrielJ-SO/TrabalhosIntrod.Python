
idade = int(input("Digite sua idade: "))
nacionalidade = input("Você é brasileiro(a)? (s/n) ").lower()

if(idade >= 18):
    if(nacionalidade == 's'):
        print("Você deve votar!")
    else:
        print("Voto opcional.")
        
elif(idade < 18 and idade >= 16):
    print("Voto opcional.")
else:
    print("Não pode votar!")