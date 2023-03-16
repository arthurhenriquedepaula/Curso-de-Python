import math

angle = float(input('Digite um ângulo: '))


sen = math.sin(math.radians(angle))

cos = math.cos(math.radians(angle))

tan = math.tan(math.radians(angle))

print('O valor de seno é: {:.2f} o valor de cosseno é: {:.2f} e o valor da tangente é: {:.2f}' .format(sen, cos, tan))

