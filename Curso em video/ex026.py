frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra "A" apareceu tantas vezes: {}'.format(frase.count('a')))
print('A primeira vez que a letra "A" apareceu foi na posição: {}'.format(frase.find('a')+1))
print('A ultima vez que a letra "A" apareceu foi na posição: {}'.format(frase.rfind('a')+1))