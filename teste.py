class Candidato:
    def __init__(self, nome, experiencia, habilidades, realizacoes):
        self.nome = nome
        self.experiencia = experiencia
        self.habilidades = habilidades
        self.realizacoes = realizacoes

    def calcular_pontuacao_total(self):
        return self.experiencia + self.habilidades + self.realizacoes


N = int(input())

candidatos = []

# Dados dos participantes
for _ in range(N):
    nome, experiencia, habilidades, realizacoes = input().split()
    experiencia = int(experiencia)
    habilidades = int(habilidades)
    realizacoes = int(realizacoes)
    candidato = Candidato(nome, experiencia, habilidades, realizacoes)
    candidatos.append(candidato)

# Ordena Candidats
candidatos = sorted(
    candidatos, key=lambda c: (-c.calcular_pontuacao_total(), c.nome))

# Resultados
for candidato in candidatos:
    print(candidato.nome)
