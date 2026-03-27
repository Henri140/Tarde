i=0
for i in range(0,3,1):
    nome=input(f'Digite seu nome: ')
    senha=input(f'Digite sua senha:')
    if nome==senha:
        print(f'Seu nome e sua senha não podem ser identicos, digite novamente!!')
    else:
        print(f'Cadastrado')
        break


    