# aula 09

f = 'Curso em Video Python'

teste = 'frase' in f

print('{}'.format(f[9]))  # pega o 9° caractere
print('{}'.format(f[9:14]))  # pega do 9° caractere até o 13°
print('{}'.format(f[9:14:2]))  # Do 9° até o 13°, pulando de 2 em dois
print('{}'.format(f[:9]))  # do inicio até o 9°
print('{}'.format(f[9:]))  # do 9° até o final
print('{}'.format(len(f)))  # tamanho
print('{}'.format(f.count('o')))  # qtd de 'o'
print('{}'.format(f.count('o', 0, 13)))  # qtd de 'o' do 0 ate 13°
print('{}'.format(f.find('deo')))  # encontra

# Modificar texto

f.replace('Python', 'Android')  # Alterar valor
f.upper()  # Maiusculo
f.lower()  # Minusculo
f.capitalize()  # Primeira Maiuscula
f.title()  # Primeiras letras maiusculas
f.strip()  # Remove espaços excedentes
f.rstrip()  # Remove espaços finais
f.lstrip()  # Remove espaços iniciais
f.split()  # Divide onde tiver espaços
'-'.join(f)  # Coloca o '-' na frase

# Exibe textos grandes
print("""aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa""")
