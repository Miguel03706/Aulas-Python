amigos = int(input())  
palpites = list(map(int, input().split()))  
erros = list(map(int, input().split())) 

possiveis_valores = set()  

for i in range(amigos):
    palpite_menor = max(1, palpites[i] - erros[i])  # Palpite mínimo considerando o erro
    palpite_maior = min(10**9, palpites[i] + erros[i])  # Palpite máximo considerando o erro

    for num_pedras in range(1, amigos+1):
        possiveis_valores.add(num_pedras)

for valor in sorted(possiveis_valores):
    print(valor)