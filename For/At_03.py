num=[]

for i in range(0,5,1):
    i+=1
    n=float(input(f'Digite o {i}° número: '))
    num.append(n)
soma=sum(num)
print(sum(num))
print(sum(num)/5)