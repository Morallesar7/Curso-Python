# Faça um algoritimo que leia o salário de um funcioário e mostre seu novo salário, com 15 % de aumento.  

salário = float(input("Qual é o salário do funcionário: R$ "))
novo = salário + (salário * 0.15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))