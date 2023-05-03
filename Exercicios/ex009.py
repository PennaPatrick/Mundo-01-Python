x = int(input('Digite um número para obter sua tabuada: '))

print('-'*10)
print('Aqui está!')
print(f'{x} * 1 = {x*1}')
print(f'{x} * 2 = {x*2}')
print(f'{x} * 3 = {x*3}')
print(f'{x} * 4 = {x*4}')
print(f'{x} * 5 = {x*5}')
print(f'{x} * 6 = {x*6}')
print(f'{x} * 7 = {x*7}')
print(f'{x} * 8 = {x*8}')
print(f'{x} * 9 = {x*9}')
print(f'{x} * 10 = {x*10}')
print('-'*10)

for i in range(1,11):
    print(f'{x} * {i} = {x*i}')
