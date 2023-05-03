frase = str(input('Digite aqui uma frase: ')).lower().strip()

print('A frase contem {} letras A'.format(frase.count('a')))
print('A primeira letra A aparece na posição: {}'.format(frase.find('a')+1))
print('A ultima letra A aparece na posição: {}'.format(frase.rfind('a')+1))
