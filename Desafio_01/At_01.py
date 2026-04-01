li=int(input(f'Digite quantos litros foram solicitados: '))
tC=input(f'De qual tipo de combustivel?(Ex:A-alcool ou G-gasolina): ').upper()

if tC!='A' and tC!='G':
    print(f'Só temos Gasolina e Alcool neste posto')
    exit()

if tC=='A' and li<=20:
    tP=3.89*li
    dP=(tP/100)*3
    pF=tP-dP
    print(f'Você deve {pF} reais, pague o frentista')

elif tC=='A' and li>20:
    tP=3.89*li
    dP=(tP/100)*5
    pF=tP-dP
    print(f'Você deve {pF} reais, pague o frentista')

if tC=='G' and li<=20:
    tP=5.50*li
    dP=(tP/100)*4
    pF=tP-dP
    print(f'Você deve {pF} reais, pague o frentista')

if tC=='G' and li>20:
    tP=5.50*li
    dP=(tP/100)*6
    pF=tP-dP
    print(f'Você deve {pF} reais, pague o frentista')