from random import randint

nomes = ['Luna', 'Simba', 'Tigrao', 'Miau', 'Felix', 'Mia', 'Whisky', 'Nino', 'Oreo', 'Cleo']
cores = ['Laranja', 'Preta', 'Branca', 'Malhada']
def gerarGato():
    nome = nomes[randint(0, 9)]
    idade = randint(0, 23)
    cor = cores[randint(0,3)]
    print(f'O(A) gato(a), {nome} de {idade} anos da cor {cor}, esta pronto(a) para ser pego(a)!')

gerarGato()