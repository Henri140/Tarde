num=[]

for i in range(10):
 i+=1
 n=int(input(f'Digite o {i}° número: '))
 num.append(n)
num.reverse()
print(num)