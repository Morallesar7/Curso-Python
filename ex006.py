# Crie um algoritimo que leia um número e mostre o seu dobro, o triplo e a raiz quadrada.

n = int(input('Digite um número : '))
d = n * 2
t = n * 3
rq = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}'.format(n, (n*3), n, pow(n, (1/2))))
