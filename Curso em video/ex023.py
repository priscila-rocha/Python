num = int(input('Digite um numero entre 0 e 9999:'))
if num<0 or num>9999:
    print('O numero digitado {} é invalido'.format(num))
else:
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10
    print('Analisando o número: {}'.format(num))
    print('Unidade {}'.format(u))
    print('Dezena {}'.format(d))
    print('Centena {}'.format(c))
    print('Milhar {}'.format(m))

'''outra forma de fazer é 
converter a num pra string
n = str(num)
print('unidade {}'.format(n[3]))
print('unidade {}'.format(n[2]))
print('unidade {}'.format(n[1]))
print('unidade {}'.format(n[0]))
porem precisaria utilizar condição'''