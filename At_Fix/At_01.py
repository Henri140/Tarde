idade=int(input(f'Digite sua idade: '))

if idade<0:
    print(f'Digite uma idade válida')
    exit()
else:
    if idade>=0 and idade<=12:
        print(f'Você tem {idade} anos, você é criança')
    elif idade>12 and idade<=17:
        print(f'Você tem {idade} anos, você é um adolescente')
    elif idade>17 and idade<=25:
        print(f'Você tem {idade} anos, você é um adulto jr')
    elif idade>25 and idade<=35:
        print(f'Você tem {idade} anos, você é um adulto')
    elif idade>35 and idade<=60:
        print(f'Você tem {idade} anos, você é um adulto sr')
    else:
        print(f'Você tem {idade} anos, você é um idoso')
