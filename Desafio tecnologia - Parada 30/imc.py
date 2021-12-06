import os

a = float(input('Digite a sua altura:'))
p = float(input('Digite o seu peso: '))

IMC = p / (a * a)

print('O seu Índice de massa corporal é de {:.2f}.'. format(IMC))

if IMC < 18.5:
   print('Magreza')
elif IMC >= 18.5 and IMC <=24.9:
   print('Normal')
elif IMC >= 25.0 and  IMC <=29.9:
    print('Sobrepeso')
elif IMC >= 30.0 and  IMC <=39.9:
    print('Obesidade')
elif IMC > 40.0:
    print('Obesidade grave')

os.system("pause")