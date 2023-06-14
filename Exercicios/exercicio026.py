# Digite uma frase, leia a QTD de "A", em qual posição aparece a primeira vez
# e em qual posição aparece pela ultima vez

f = str(input('Digite uma frase: '))

print('A letra "A" aparece: {} vezes'.format(f.upper().count('A')))
print('A primeira vez que "A" aparece é na posição {} da frase'.format(
    f.upper().find('A')))
print('A ultima vez que "A" aparece é na posição {} da frase'.format(
    f.upper().rfind('A')))
