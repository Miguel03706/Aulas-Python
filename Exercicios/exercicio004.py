# Mostre os tipos de dados contidos no caractere que o usuário enviar

texto = input('Digite algo: ')
primitivo = type(texto)
espaco = texto.isspace()
numérico = texto.isnumeric()
alfabético = texto.isalpha()
alfanumérico = texto.isalnum()
maiúsculas = texto.isupper()
minúsculas = texto.islower()
captalizada = texto.istitle()


print('O tipo primitivo desse valor é: {}'.format(primitivo))
print('Só tem espaços? {}'.format(espaco))
print('É numérico? {}'.format(numérico))
print('É alfabético? {}'.format(alfabético))
print('É alfanumérico? {}'.format(alfanumérico))
print('Só tem maiúsculas? {}'.format(maiúsculas))
print('Só tem minúsculas? {}'.format(minúsculas))
print('Está captalizada? {}'.format(captalizada))
