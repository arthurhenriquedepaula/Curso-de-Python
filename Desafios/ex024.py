city = input('Digite o nome da sua cidade: ')

position = city.find("SANTO")

if(position == 0):
    print('O nome da sua cidade é: {} e ela começa com SANTO' .format(city))
else:
    print('Sua cidade não começa com SANTO')
