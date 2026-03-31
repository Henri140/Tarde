notas=[]
for i in range(4):
    i+=1
    n=float(input(f'Digite a {i}° nota: '))
    notas.append(n)
print(notas)
print(sum(notas)/4)