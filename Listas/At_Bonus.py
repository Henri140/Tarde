alt=[]
id=[]
aluno=0
for i in range(30):
    aluno+=1
    d=int(input(f'Digite a idade do {aluno}° aluno: '))
    a=float(input(f'Digite a altura desse {aluno}° aluno: '))
    id.append(d)
    alt.append(a)
       


mediaAlt=sum(alt)/len(alt)
for i in range (30):
    if id[i]>13 and alt[i]<mediaAlt:
            print(f'A altura do {i+1}° aluno é menor que a média')



