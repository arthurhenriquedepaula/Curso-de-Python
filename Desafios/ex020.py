import random

student1 = str(input('Digite filme 1 de lalin:'))
student2 = str(input('Digite filme 2 de lalin:'))
student3 = str(input('Digite filme 1 de tuco:'))
student4 = str(input('Digite filme 2 de tuco:'))


list_names = [student1, student2, student3, student4]

random.shuffle(list_names)

print('A sequencia de sorteados é: {}'.format(list_names))

