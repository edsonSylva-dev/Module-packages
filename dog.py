from random import randint

nomes = ['Zeus', 'Duke', 'Bella', 'Max', 'Rex', 'Toby', 'Marley', 'Rocky', 'Nina', 'Cookie']
cores = ['Caramelo', 'Preta', 'Branca', 'Malhada', 'Laranja']
racas = ['Golden', 'Vira-lata', 'Husky', 'Pitbull', 'Salsicha']
def gerarCachorro():
    nome = nomes[randint(0, 9)]
    idade = randint(0, 13)
    numraca = randint(0,4)
    if numraca == 0:
        cor = cores[4]
    elif numraca == 2:
        cor = cores[randint(1,3)]
    else:
        cor = cores[randint(0,4)]
    print(f'O(A) cachorro(a), {nome} de {idade} anos de cor {cor} e da raca {racas[numraca]}, esta pronto(a) para ser pego(a)!')

gerarCachorro()