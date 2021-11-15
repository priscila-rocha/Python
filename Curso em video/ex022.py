nome = str(input('Digite seu nome completo: ')).strip()
separado=nome.split()
print('Seu nome em letra maiuscula é: {} '
      '\nSeu nome em letra minuscula é: {}'.format(nome.upper(), nome.lower()))
print('A quantidade de caracteres que tem seu nome é: {}'.format((len(nome)-nome.count(' '))))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print('A quantidade de caracteres que o seu primeiro nome é {} e tem é de: {}'.format(separado[0], len(separado[0])))