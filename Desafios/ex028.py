import random

number_random = random.randint(0,5)

number_question = int(input('Tenta acertar o número sorteado: '))

if(number_random == number_question):
    print('Você acertou!!! o número realmente é: {}'.format(number_question))




