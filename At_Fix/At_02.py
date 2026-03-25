dia=int(input(f'Digite o seu dia de nascimento: '))
mes=int(input(f'Digite o seu mês de nascimento: '))

if dia<0 or dia>31:
    print(f'Seu dia ou mês de nascimento são inválidos')


if mes==1:
    if dia<=20:
        print(f'Você é de Capricórnio')
    else:
        print(f'Você é de Aquário')

if mes==2:
    if dia<=19:
        print(f'Você é de Aquário')
    else:
        print(f'Você é de Peixes')

if mes==3:
    if dia<=20:
        print(f'Você é de Peixes')
    else:
        print(f'Você é de Áries')

if mes==4:
    if dia<=20:
        print(f'Você é de Áries')
    else:
        print(f'Você é de Touro')

if mes==5:
    if dia<=20:
        print(f'Você é de Touro')
    else:
        print(f'Você é de Gêmeos')

if mes==6:
    if dia<=20:
        print(f'Você é de Gêmeos')
    else:
        print(f'Você é de Câncer')

if mes==7:
    if dia<=21:
        print(f'Você é de Câncer')
    else:
        print(f'Você é de Leão')

if mes==8:
    if dia<=22:
        print(f'Você é de Leão')
    else:
        print(f'Você é de Virgem')

if mes==9:
    if dia<=22:
        print(f'Você é de Virgme')
    else:
        print(f'Você é de Libra')

if mes==10:
    if dia<=22:
        print(f'Você é de Libra')
    else:
        print(f'Você é de Escorpião')

if mes==11:
    if dia<=21:
        print(f'Você é de Escorpião')
    else:
        print(f'Você é de Sagitário')

if mes==12:    
    if dia<=21:
        print(f'Você é de Sagitário')
    else:
        print(f'Você é de Capricórnio')