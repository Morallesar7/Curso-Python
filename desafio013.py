# Faça um algoritimo que leia o salário de um funcioário e mostre seu novo salário, com 15 % de aumento.  

salario = float(input("Digite o salário do funcionário: R$ "))
aumento = salario * 0.15
novo_salario = salario + aumento
print("O novo salário com 15% de aumento é: R$ {:.2f}".format(novo_salario))
