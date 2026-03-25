qT=int(input(f'Qual a qunatidade de turmas: '))
i=0
qA=[]
while i<qT:
    i+=1
    q=int(input(f'Qual a quantidades de alunos na {i}° turma: '))
    qA.append(q)
    if q>40 or q<0:
        print(f'Digite uma quantidade válida de alunos')
        i=0
media=sum(qA)/qT
print(f'A média de alunos é: {media}')