h=input(f'Como você está hoje? (Ex:Cansado): ').lower()

if h=='cansado':
    print(f'Descansa um pouco')
elif h=='feliz' or h=='animado':
    print(f'Faça alguma coisa social ou produtiva')
elif h=='estressado':
    print(f'Faça algo relaxante')
else:
    print(f'Faz uma pausa ai vei')