import random

student1 = str(input('Digite o 1 filme de laura peidorreira: '))
student2 = str(input('Digite o 2 filme de laura pindola: '))
student3 = str(input('Digite o 1 filme de arthur: '))
student4 = str(input('Digite o 2 filme de arthur: '))

names = [student1, student2, student3, student4]

print('O aluno sorteado é: {}' .format(random.sample(names, 1)))

