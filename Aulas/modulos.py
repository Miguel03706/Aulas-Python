# aula 08

# import teste => importa tudo aqui dentro
# from teste import {comando} => importa algo especifico

# importar bibliotecas externas funciona tbm
# -> basta entrar em python.org e ver os pacotes disponiveis
import math

n = int(input('Digite um número: '))

raiz = math.sqrt(n)

print('A raiz de {} é igual a {:.2f}'.format(n, raiz))
