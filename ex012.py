# Faça um algoritimo que leia um preço de um produto e mostre seu novo preço, com 5% de desconto.  

preço = float(input("Digite o preço do produto: R$ "))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))

