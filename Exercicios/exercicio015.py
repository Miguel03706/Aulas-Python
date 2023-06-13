# Pergunte quantos dias uma pessoa alugou carro
# quantos km ele rodou
# imprimir valor pago

d = int(input('Digite a quantidade de dias o carro foi utilizado: '))
km = float(input('Digite a quantidade de km que o carro percorreu nesse tempo: '))

preço = (60*d) + km*0.15

print('O valor a ser pago pelo carro após ter passado {} dia(s) e percorrido {}Km é de: R$ {}'.format(d, km, preço))
