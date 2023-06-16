# Aula 19

dados = dict()

dados = {'nome': 'Pedro', 'idade': 19}

dados['sexo'] = 'M'

del dados['sexo']

print(dados.values()) # pega apenas valores
print(dados.keys()) # pega nome dos valores
print(dados.items()) # pega valores e nome de valores

for k, v in dados.items():
    print(f'O {k} é: {v}')

