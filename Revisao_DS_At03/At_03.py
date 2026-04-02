no=[]
for i in range(4):
    i+=1
    n=float(input(f'Digite sua {i}° nota: '))
    no.append(n)

print(no)
print(sum(no)/4)