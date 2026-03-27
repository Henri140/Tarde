qP=int(input(f'Quantas pessoas estarão: '))
i=0
qm=0
for i in range(0,qP,1):
    i+=1
    g=input(f'Qual o gênero da {i}° pessoa(m-masculino / f-feminino): ')
    if g=='m' or g=='M':
        qm+=1

print(f'Tiveram {qm} homens')