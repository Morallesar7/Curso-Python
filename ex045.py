# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
print('-=' * 11)

jogador = int(input('Qual é sua jogada? '))

if jogador not in [0, 1, 2]:
    print('Jogada inválida! Por favor, escolha um número entre 0 e 2.')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-=' * 11)

    if computador == 0:  # computador jogou PEDRA
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('JOGADOR VENCE')
        elif jogador == 2:
            print('COMPUTADOR VENCE!')
    elif computador == 1:  # computador jogou PAPEL
        if jogador == 0:
            print('COMPUTADOR VENCE')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('JOGADOR VENCE')
    elif computador == 2:  # computador jogou TESOURA
        if jogador == 0:
            print('JOGADOR VENCE')
        elif jogador == 1:
            print('COMPUTADOR VENCE!')
        elif jogador == 2:
            print('EMPATE')
