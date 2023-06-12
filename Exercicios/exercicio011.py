# Pedir largura e altura da parede
# Calcular área
# A cada 2m² de parede, é necessário 1L de tinta
# Imprima a quantidade de tinta necessária para pintar a parede em questão

a = float(input('Digite a altura da parede(m): '))
l = float(input('Digite a largura da parede(m): '))

area = a * l

tinta = area/2

print('A sua parede tem dimensões de {}x{} e a sua área é de {}m²'.format(a, l, area))

print('A tinta necessária para pintar sua parede é de {}L'.format(tinta))
