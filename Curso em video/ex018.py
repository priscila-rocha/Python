from math import sin, cos, tan, radians
a = float(input('Digite o ângulo que você deseja: '))

sen = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print('O ângulo de {} tem o Seno de {:.2f} '
      '\nO ângulo de {} tem o Cosseno de {:.2f} '
      '\nO ângulo de {} tem a Tangente de {:.2f}'.format(a, sen, a, cos, a, tan))
