# Programa que leia o nome de uma cidade e diga
# se o nome da cidade começa com "santo"

c = str(input('Digite o nome de uma cidade: '))

if (c.split()[0].find('santo') != -1):
    print('A cidade começa com "Santo"')
else:
    print('A cidade não começa com "Santo"')
