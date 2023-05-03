nome = str(input('Digite aqui o seu nome para uma breve análise: '))

print(nome.upper())
print(nome.lower())

letras = nome.split()
letras = (''.join(letras))

print(f'Seu nome tem ao todo: {len(letras)} letras')

letras1nome = nome.split()
print(f'Seu primeiro nome tem: {len(letras1nome[0])} letras')