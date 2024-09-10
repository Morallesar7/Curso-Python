# Crie um programa que leia um nome de uma cidade diga se ela começa ou não com o nome santo "SANTO".  

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')