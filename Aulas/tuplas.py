lanche = ('Hamburguer', 'Suco', 'Pudim') # TUPLA É IMUTÁVEL
# aceita valores com tipos diferentes

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
    
    
for comida in lanche:
    print(f'Eu vou comer {comida}')
        
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')


print('Comi muito')

a = (1, 2, 3)
b = (4, 5, 6)
c = a+b

print(c)

# sorted() -> organiza
# c.count(5) -> mostra quantas vezes aparece
# c.index(8) -> mostra onde está o 8
# c.index(8, 4) -> mostra onde está o 8 a partir da posição 4
# del(nome_tupla) -> apaga a tupla
# #
