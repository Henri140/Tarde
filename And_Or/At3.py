usuario=input(f'Digite seu nome de usuário: ')
senha=input(f'Digite sua senha: ')

if usuario == 'admin' and senha == '1234':
    print('Acesso concedido.')
else:
    print('Acesso negado.')