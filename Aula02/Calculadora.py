'''Receber dois valores numéricos do usuário
 e apresentar o resultado das operações matemáticas 
 básicas entre eles: soma, subtração, multiplicação, 
 divisão, resto da divisão e exponenciação



numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print(f"{numero1} + {numero2} = {numero1+numero2}")
print(f"{numero1} - {numero2} = {numero1-numero2}")
print(f"{numero1} / {numero2} = {numero1/numero2}")
print(f"{numero1} x {numero2} = {numero1*numero2}")
print(f"{numero1} % {numero2} = {numero1%numero2}")
print(f"{numero1} ** {numero2} = {numero1**numero2}")
'''



#Versão padrão
'''v1=float(input(f'Digite o primeiro valor: '))
v2=float(input(f'Digite o segundo valor: '))
resultado=0
valores=[]
quant=int(input(f'Quantos valores gostaria de usar: '))
operacao=input('Que operação deseja realizar: ')
for i in range(quant):
    valores[input(f'Digite o {i}° valor: ')]
    valores.append()
if (operacao=='+'):
    resultado=v1+v2
    print(resultado)
elif (operacao=='-'):
    resultado=v1-v2
    print(resultado)
elif(operacao=='*'):
    resultado=v1*v2
    print(resultado)
elif(operacao=='/'):
    resultado=v1/v2
    print(resultado)
elif(operacao=='**'):
    resultado=v1**v2
    print(resultado)
else:
    resultado=v1%v2
    print(resultado)

    valores = []
'''


#Minha versão

quant = int(input('Quantos valores gostaria de usar: '))
valores=[]
for i in range(quant):
    valor = float(input(f'Digite o {i+1}° valor: '))
    valores.append(valor)

operacao = input('Que operação deseja realizar (+, -, *, /, **, %): ')

resultado = valores[0]

if operacao == '+':
    for i in range(1, len(valores)):
        resultado += valores[i]
elif operacao == '-':
    for i in range(1, len(valores)):
        resultado -= valores[i]
elif operacao == '*':
    for i in range(1, len(valores)):
        resultado *= valores[i]
elif operacao == '/':
    for i in range(1, len(valores)):
        if valores[i] != 0:
            resultado /= valores[i]
        else:
            print('Erro: Divisão por zero!')
            exit()
elif operacao == '**':
    for i in range(1, len(valores)):
        resultado **= valores[i]
elif operacao == '%':
    for i in range(1, len(valores)):
        if valores[i] != 0:
            resultado %= valores[i]
        else:
            print('Erro: Módulo por zero!')
            exit()
else:
    print('Operação inválida!')
    exit()
    
print(f'\nResultado: {resultado}')
print(f'Expressão: ', end='')
for i in range(len(valores)):
    print(valores[i], end='')
    if i < len(valores)-1:
        print(f' {operacao} ', end='')
print(f' = {resultado}')