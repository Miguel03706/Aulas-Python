# Usuario digit o nome, programa verifica se tem "silva"

n = str(input('Digite seu nome: '))

if (n.lower().find('silva') != -1):
    print('O nome {} POSSUI "Silva"'.format(n.title()))

else:
    print(n.lower().find('silva'))
    print('O nome {} NÃO Possui "Silva"'.format(n.title()))
