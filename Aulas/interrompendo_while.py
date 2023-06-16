# aula 15

n = s = 1
while True:
    print(n, '-> ', end='')
    
    if(n == 10):
        break
    n+=1
    s += n
    
print(f'Acabou {s:-<4}')