num = []

while True:
    try:
        n = int(input('Digite um número (para sair pressione 0): '))
    except:
        print('Digite apenas números!')
        continue
    
    if n == 0:
        print(sum(num))
        break
    
    num.append(n)