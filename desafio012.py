# Faça um algoritimo que leia um preço de um produto e mostre seu novo preço, com 5% de desconto.  

preco = float(input("Digite o preço do produto: R$ "))
desconto = preco * 0.05
preco_com_desconto = preco - desconto
print("O preço com 5% de desconto é: R$ {:.2f}".format(preco_com_desconto))
