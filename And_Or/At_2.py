nota = float(input('Digite sua nota: ').replace(',', '.'))
frequencia = int(input('Digite sua frequência (em %): '))

if nota < 0 or nota > 10 or frequencia < 0 or frequencia > 100:
    print('Sua nota ou frequência está incorreta')
else:
    if nota >= 7 or frequencia >= 75:
        print('Você foi aprovado.')
    else:
        print('Você foi reprovado.')