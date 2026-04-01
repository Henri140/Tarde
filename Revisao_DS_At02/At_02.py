num=['0','1','2','3','4','5','6','7','8','9']

se=input(f'Digite sua senha: ')

if all(c in num for c in se):
    print('Só número não dá né meu chapa')

if len(se)<6:
    print(f'Sua senha é fraca, coloque mais caracteres')
elif len(se)>=6 and len(se)<8:
    print(f'Sua senha é média, acrescenta mais uns negocio é vai ficar show')
else:
    print(f'Sua senha é forte, tá joia meu querido(a)')

