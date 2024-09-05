# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antencessor. 

n = int(input('Digite um número inteiro : '))
s = n + 1
a = n - 1
print('O sucessor de {} é {} e o antencessor é {}.'.format(n, s, a))