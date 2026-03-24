salario=float(input(f'Digite seu salario: ').replace(',','.'))
te=int(input(f'Quantos anos de empresa você tem: '))


if salario <3000 & te>=2:
    print('Você tem direito a um bônus')
else:
    print('Você não tem direito ao bônus')