largura = float(input('Digite a largura da parede: '))
altura  = float(input('Digite a altura da parede: '))

area = largura * altura

litros = area / 2

print('A área é: {:.2f} m2 e a quantidade de tinta é: {:.2f}' .format(area, litros))