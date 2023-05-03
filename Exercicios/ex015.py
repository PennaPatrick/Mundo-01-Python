dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))

preço = (60 * dias) + (0.15 * km)

print(f'O custo total dessa locação ficou no total de R${preço}')
