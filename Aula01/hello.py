#Iniciação
'''print(f'Hello Word')'''

#Dados do Usúario
'''nome=input(f'Qual o seu nome? ')
idade=input(f'Qual a sua idade? ')
print('Seu nome é: '+nome+' e sua idade é: '+idade)'''


# raiz=25**0.5
# print(raiz)

'''Versão padrão'''
'''
nota1=int(input('Digite a 1° nota:'))
nota2=int(input('Digite a 2° nota:'))
nota3=int(input('Digite a 3° nota:'))
nota4=int(input('Digite a 4° nota:'))
media= (nota1+nota2+nota3+nota4)/4
print(f'Essa é sua media: {media}')
if media>=7:
    print(f'Você foi aprovado')
elif ((media>=5) & (media<7)):
    print(f'Você está de recuperação')
else:
    print(f'Você está reprovado')
'''

'''Minha versão'''

nota=[]
for i in range(1,5):
    n=float(input(f'Qual sua {i}° nota?'))
    nota.append(n)
media=sum(nota)/4
print(f'Sua media é: {media}')
if media>=7:
    print(f'Você foi aprovado')
elif ((media>=5) & (media<7)):
    print(f'Você está de recuperação')
else:
    print(f'Você está reprovado')


