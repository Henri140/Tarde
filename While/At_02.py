qtN=float(input(f'Quantas notas serão computadas: '))
i=0
nota=[]
while i<qtN:
    i+=1
    n=float(input(f'Qual sua {i}° nota: '))
    nota.append(n)
media=sum(nota)/qtN
print(f'Sua media: {media}')