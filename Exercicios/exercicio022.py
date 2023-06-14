# Crie um programa que leia o nome completo de uma pessoa
# Mostre ele com maiúsculas/minúsculas/sem considerar espaços e quantas letras tem o nome

n = str(input('Digite o seu nome completo: '))

print('Maiúsculo: {}'.format(n.upper()))
print('Minúsculo: {}'.format(n.lower()))
print('Número de letras: {}'.format(len(n.replace(' ', ''))))
print('Letras no primeiro nome: {}'.format(len(n.split()[0])))
