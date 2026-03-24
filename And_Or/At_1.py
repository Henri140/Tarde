idade=int(input(f'Digite sua idade: '))
autorizacao=input(f'Você tem autorização para participar? (s/n): ').upper()

if autorizacao == 'S' or autorizacao == 'N':
   if idade >= 18 or autorizacao == 'S':
     print('Você pode participar.')
   else:
     print('Você não pode participar.') 
else:
    print('Digite uma resposta válida')
    exit()