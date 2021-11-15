lar = float(input('Digite a largura da parece: '))
alt = float(input('Digite a altura da parede: '))
area = lar * alt
print('Sua parede tem a dimensão de {} x {}. A quantidade de tinta que você precisa para pintar a parede é: {} litros'.format(lar, alt, area/2))
