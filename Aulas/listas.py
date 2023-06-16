# Aula 17

lanche = ['Hamburguer', 'Bebida', 'Pizza']

lanche.append('Kookie') # Add elemento
lanche.insert(0, 'Hot Dog') # Add na posição zero
del lanche[3] # Deleta posição 3
lanche.pop(3) # Deleta posição 3 (sem parametro deleta a ultima)
lanche.remove('Pizza') # remove pizza (se não existir, da erro)

numeros = list(range(1,11)) # Cria lista que vai do 1 ao 10

numeros2 = [2, 6, 1, 2, 3]

numeros2.sort() # Organiza lista
numeros2.sort(reverse=True) # Organiza lista ao contrario

a = [1,2,3]
b = a # Cria "Ligação" entre as listas

print(f'Lista A: {a}')
print(f'Lista B: {b}')


a = [1,2,3]
b = a[:] # Cria Cópia da lista A na B

print(f'Lista A: {a}')
print(f'Lista B: {b}')


galera = [['João', 19],['Maria', 13],['Miguel', 20]]

print(galera[0][1])