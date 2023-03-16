teste = input('Digite algo meu caro gafanhoto: ')

if teste.isnumeric():
    print('então é númerico')
else:
    print('então não é númerico')

if teste.isalpha():
    print('então é alfabético')
else:
    print('então não é alfabético')

if teste.isupper():
    print('então é maiúsculo')
else:
    print('então não é maisúsculo')

if teste.isalnum():
    print('então é númerico ou alfabético')
else:
    print('então é não é númerico ou alfabético')