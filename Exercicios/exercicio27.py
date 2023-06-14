# Pergunte o nome completo da pessoa e exiba o primeiro e ultimo nome


nome = str(input('Digite seu nome completo: '))

print('{} {}'.format(nome.split()[0], nome.split()[len(nome.split()) - 1]))
