# Peça para o usuario digitar um angulo e mostre SENO, COSSENO e TANGENTE

from math import sin, cos, tan, radians

a = float(input('Digite o ângulo que você deseja: '))

print('O ângulo de 30° tem o SENO de {:.2f}'.format(sin(radians(a))))
print('O ângulo de 30° tem o COSSENO de {:.2f}'.format(cos(radians(a))))
print('O ângulo de 30° tem o TANGENTE de {:.2f}'.format(tan(radians(a))))
