# Escreva um programa que leia um valor em metros e o exiba convertido em centímentros e milímetros.  

metros = float(input('Digite um valor em metros: ')) 
centimetros = metros * 100
milimetros = metros * 1000
print('{} Metros equivalem a {} centímetros e {} milímetros.'.format(metros, centimetros, milimetros))