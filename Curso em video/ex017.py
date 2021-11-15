import math
#from math import hypot
x = float(input('Digite o comprimento do cateto oposto do triangulo: '))
y = float(input('Digite o comprimento do cateto adjacente do triangulo: '))
hyp = math.hypot(x,y)
#hyp = (x ** 2 + y ** 2) ** (1/2)
print('O comprimento da hypotenusa  {:.2f}'. format(hyp))