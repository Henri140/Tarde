status=input(f'Digite seu estado civil (ex: Casado/a=C): ')
status=status.upper()
if status=='C':
    print(f'{status}-Casado/a')
elif status=='S':
    print(f'{status}-Solteiro/a')
elif status=='D':
    print(f'{status}-Divorciado/a')
elif status=='V':
    print(f'{status}-Viúvo/a')
elif status=='O':
    print(f'{status}-Outro')
else:
    print(f'Digite um status válido')
    exit()