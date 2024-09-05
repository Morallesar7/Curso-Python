# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m quadrado.  

largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))
area = largura * altura
cobertura_tinta = 2.0
quantidade_tinta = area / cobertura_tinta
print("A área da parede é {:.2f} metros quadrados.".format(area))
print("Você vai precisar de {:.2f} litros de tinta para pintar a parede.".format(quantidade_tinta))
