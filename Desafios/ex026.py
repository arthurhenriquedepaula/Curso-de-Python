phrase = input('Digite uma frase: ')

occurrences = phrase.count('A')
one_position = phrase.find('A')
two_position = phrase.rfind('A')

print('A string "A" apareceu {} vezes, e sua primeira ocorrencia foi {}, já sua última ocorrência foi {}'.format(occurrences, one_position, two_position));


