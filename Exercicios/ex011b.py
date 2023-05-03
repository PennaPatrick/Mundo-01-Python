def resultado(altura, largura):
    area = altura*largura
    tinta = area/2
    return tinta


largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))

# area = altura*largura
# tinta = area/2

# print(f'A área correspondente é: {area}m²')
print(f'Portanto precisará de {resultado(altura, largura)}l')
