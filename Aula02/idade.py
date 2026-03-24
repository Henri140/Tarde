idade=int(input(f'Digite sua idade: '))
if idade>=18:
    print(f'Adulto')
elif ((idade<18) & (idade>=12)):
    print(f'Adolescente')
else:
    print(f'Criança')
