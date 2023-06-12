# Digite o valor de um produto e imprima o valor dele com 5% de desconto

v = float(input('Digite o valor do produto: R$ '))

print('O produto que custava R${:.2f}, com desconto de 5% passa a custar: R${:.2f}'.format(
    v, float(v - (v*0.05))))
