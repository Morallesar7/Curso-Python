# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Doláres ela pode comprar.  

reais = float(input("Quanto dinheiro você tem na carteira (em reais)? "))
taxa_cambio = 5.64
dolares = reais / taxa_cambio
print("Com R$ {:.2f}, você pode comprar US$ {:.2f}.".format(reais, dolares))
