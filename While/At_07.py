qP = int(input('Qual a quantidade de pessoas: '))
i = 0

ba = []  
ec = []  
es = []  

while i < qP:
    i += 1
    
    d = int(input(f'Qual a idade da {i}° pessoa: '))
    c = int(input('Possui convite (1=sim / 0=não): '))

    if c != 0 and c != 1:
        print('Digite um número válido (0 ou 1)')
        i -= 1
        continue

    if d < 16:
        ba.append(d)
    else:
        if c == 1:
            ec.append(d)
        else:
            es.append(d)

print(f'Número de barrados: {len(ba)}')
print(f'Número de entradas: {len(es) + len(ec)}')
print(f'Número de entradas (sem convite): {len(es)}')