import random

random_number = str(random.randint(0, 9999))

if (len(random_number) == 2):
    print('Referente ao número {} Unidade: {} Dezena {}' .format(random_number, random_number[1], random_number[0]))

if(len(random_number) == 3):
    print('Referente ao número {} Unidade: {} Dezena: {} Centena: {}' .format(random_number, random_number[2], random_number[1], random_number[0]))

if(len(random_number) == 4):
    print('Referente ao número {} Unidade: {} Dezena: {} Centena: {} Milhar: {}' . format(random_number, random_number[3], random_number[2], random_number[1], random_number[0]))