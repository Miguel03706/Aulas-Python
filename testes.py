n, m = map(int, input().split())
dna = input()
proteina = input()
q = int(input())

results = []  

for _ in range(q):
    a, b = map(int, input().split())
    substring_proteina = proteina[a-1:b]
    count = 0
    
    for i in range(n):
        substring_dna = dna[i:i+b-a+1]
        if substring_proteina == substring_dna:
            count += 1
            results.append(count)
   # count = dna.count(substring_proteina) # n conta 3 caracteres iguais seguidos
    

# Imprimir os resultados das consultas
for result in results:
    print(result)