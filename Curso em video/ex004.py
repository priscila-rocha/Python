x = input('Digite alguma coisa:')
print('O tipo dessa variavel {} é:'.format(x), type(x))
print('{} É só espaço?'.format(x), x.isspace())
print('{} Está em letra maiuscula?'.format(x), x.isupper())
print('{} É só numero?'.format(x), x.isnumeric())
print('{} Está capitalizada?'.format(x), x.istitle())