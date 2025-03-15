import dog
import cat

print('Ola, Seja bem vindo(a)!')
while True:
    option = input('O seu animalzinho e um gato ou cachorro? ').capitalize().strip()
    if option == 'Gato':
        cat.gerarGato()
        break
    elif option == 'Cachorro':
        dog.gerarCachorro()
        break
    else:
        print('Tente novamente!')