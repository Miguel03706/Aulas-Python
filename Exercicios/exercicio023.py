# Faça um programa que leia um numero de 0 a 9999 e mostre cada um dos digitos

n = str(input('digite um número: '))

if (int(n) > 9999):
    print('Número maior do que o permitido')
else:
    print('Unidade: {}'.format(n[3]))
    print('Dezena: {}'.format(n[2]))
    print('Centena: {}'.format(n[1]))
    print('Milhar: {}'.format(n[0]))
