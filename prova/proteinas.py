n, m = map(int, input().split())
dna = input()
proteina = input()
q = int(input())

results = []  

for _ in range(q):
    a, b = map(int, input().split())
    # pega a posição certa (linguagem humana // ex: 1 = posição 2)
    substring_proteina = proteina[a-1:b] 
    
    count = 0
    # vai do inicio ao fim no dna
    print('Proteina:',substring_proteina)
    for i in range(n): # OU  (n - b + 1)
        substring_dna = dna[i:i+b-a+1] # isso q deixa lento?
        print(substring_dna)
        
        if substring_proteina == substring_dna:
            count += 1
    results.append(count)

# Imprimir os resultados das consultas
# for result in results:
#     print(result)