preco = float(input('Digite o preço do produto: '))
print('O valor com desconto é {:.2f}'.format(preco*0.95))

#outra forma
novo = preco - (preco * 5 / 100)
print('Novo preço {}'.format(novo))