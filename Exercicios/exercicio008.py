# faça a conversão de uma medida em metros para outras medidas

m = float(input('Digite uma medida em metros: '))

print('A medida de {}m corresponde a:'.format(m))
print('{}km'.format(m/1000))
print('{}hm'.format(m/100))
print('{}dam'.format(m/10))
print('{}dm'.format(m*10))
print('{}cm'.format(m*100))
print('{}mm'.format(m*1000))
