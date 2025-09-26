
preco = int(input("Qual o preço do produto? R$ "))
vip = input("O cliente é VIP? (S/N) ").upper()

if(preco >= 100):
    if(vip == 'S'):
        desconto = preco * 0.25
    else:
        deconto = preco * 0.20
elif(preco >= 50):
    if(vip == 'S'):
        desconto = preco * 0.15
    else:
        desconto = preco * 0.10
elif(preco < 50):
    if(vip == 'S'):
        desconto = preco * 0.05
    else:
        desconto = 0

print(f"O valor do desconto é R$ {desconto:.2f}")