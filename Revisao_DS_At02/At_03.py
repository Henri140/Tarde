en=int(input(f'Digite seu valor de energia(0 a 100): '))

if en<0 or en>100:
    print(f'Um número válido por favor')
    exit()

iE=input(f'Possui algum item especial(s/n): ').lower()

if iE!='s' or 'n':
 print(f'Uma informação válida por favor')
 exit()

if en<30:
    print(f'Infelizmente você não pode entrar, nível de energia muito baixa')
elif (en>30 and en<70) and (iE=='s'):
    print(f'Pode entrar, Você tem energia suficiente e um item especial')
elif (en>30 and en<70) and (iE=='n'):
    print(f'Você não pode entrar, te falta um item especial')
else:
    print(f'Pode entrar')