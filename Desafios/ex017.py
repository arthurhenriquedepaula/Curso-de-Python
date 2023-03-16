from math import sqrt

op  = float(input('Digite o valor do cateto oposto: ')) 
adj = float(input('Digite o valor do cateto adjacente: '))

op = op ** 2
adj = adj ** 2

soma = op + adj

print('O comprimento da hipotenusa é: {:.2f}'.format(sqrt(soma)))
