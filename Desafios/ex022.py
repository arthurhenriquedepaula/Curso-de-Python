name = input('Digite o seu nome completo: ')

name_split = name.split() 

print("""Seu nome em maiúsculo é: {}
         Seu nome em minúsculo é: {}
         A quantidade de letras que seu nome contém é: {}
         A quantiade de letras que seu primeiro nome possui é: {}""". format(name.upper(), name.lower(), len(name),len(name_split[0]) ))
