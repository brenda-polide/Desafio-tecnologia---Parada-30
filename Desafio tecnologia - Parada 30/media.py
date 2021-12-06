import os

n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
n3 = float(input('Terceira nota:'))

media = (n1+n2+n3) / 3

print('media:',media)
    
if media<60:
        print('Reprovado')
elif media>60:
        print('Aprovado')

os.system("pause")