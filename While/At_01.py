v=False
while v==False:
    nota=int(input(f'Digite uma nota de 0 a 10: '))
    if nota>10 or nota<0:
        v=False
        print(f'Digite um valor válido')
    else:
        v=True