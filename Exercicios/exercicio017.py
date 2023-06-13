# Peça os catetos e calcule a hipotenusa

from math import hypot

c1 = float(input('Digite o cateto oposto: '))
c2 = float(input('Digite o cateto adjacente: '))

print('Com os catetos: {} e {}, sua hipotenusa é: {:.2f}'.format(
    c1, c2, hypot(c1, c2)))
