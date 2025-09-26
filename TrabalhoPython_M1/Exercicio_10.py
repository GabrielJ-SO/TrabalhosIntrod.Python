
senha_invalida = True
senha_forte = False
especiais =  ['!', '@', '#', '$', '%']
tem_especial = False
tem_numero = False
tem_lower = False
tem_upper = False

while(senha_invalida):
    senha = input("Digite a senha: ")
    if(len(senha) < 8):
        print("A senha deve conter no minimo 8 caracteres.")
    else:
        senha_invalida = False

for char in senha:

    if char.isdigit():
        tem_numero = True
    if char.islower():
        tem_lower = True
    if char.isupper():
        tem_upper = True

for especial in especiais:
    if(especial in senha):
        tem_especial = True
        break

if(tem_numero and tem_lower and tem_upper and tem_especial):
    senha_forte = True

if(senha_forte):
    print("Sua senha é forte o suficiente!")
else:
    print("Sua senha é fraca demais!")