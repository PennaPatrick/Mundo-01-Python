nome = str.lower(input('Digite seu nome: '))

lista = nome.split()
print(f'Seu primeiro nome é: {lista[0].capitalize()}')
print(f'Seu ultimo nome é: {lista[-1].capitalize()}')
