x = input('Digite algo: ')
print(type(x))
print(f'Isso é numérico? {x.isnumeric()}')
print(f'Isso só tem espaços? {x.isspace()}')
print(f'Isso é alfabético? {x.isalpha()}')
print(f'Isso é alfanumérico? {x.isalnum()}')
print(f'Isso é caixa alta? {x.isupper()}')
print(f'Isso é minusculo? {x.islower()}')
print(f'Isso é capitalizado? {x.istitle()}')
