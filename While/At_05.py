s = input('Digite a senha: ').strip()
i=0
i+=1
while i!=0:
    rS = input('Repita a senha: ').strip()
    if s == rS:
        print('Senha salva com sucesso')
        i=0
    else:
        print('Senha incorreta')
       