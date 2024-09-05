# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Doláres ela pode comprar.  

real = float(input("Quanto dinheiro você tem na carteira (em reais)? "))
dolar = 5.64
dolar = real / dolar
print("Com R$ {:.2f}, você pode comprar US$ {:.2f}".format(real, dolar))
