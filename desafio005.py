# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antencessor.  

numero = int(input('Digite um número inteiro : '))
sucessor = numero + 1
antencessor = numero - 1
print('O sucessor de {} é {} e o antencessor é {}.'.format(numero, sucessor, antencessor))