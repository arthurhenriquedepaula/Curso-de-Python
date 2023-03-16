name = input('Digite seu nome: ')

verify_position = name.find('SILVA')

if(verify_position != -1):
    print('{} possui SILVA no nome ' .format(name))
else:
    print('Você não possui SILVA no nome')