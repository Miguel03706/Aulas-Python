# Pergunte o salaria de um funcionario e aplique um aumento de 15%

n = float(input('Digite o salário do funcionário: R$ '))

print('Um funcionário que ganhava R$ {}, com 15% de aumento, passa a receber R$ {}'.format(
    n, float(n+(n*(15/100)))))
