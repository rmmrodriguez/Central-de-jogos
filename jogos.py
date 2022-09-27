import adivinhacao_definitiva
import forca

continuar=True
while(continuar==True):
    print('(1) Forca (2) Adivinhação')
    jogo=int(input('Qual jogo? '))

    if jogo==1:
        print('Iniciando Forca')
        forca.jogar()
        print('Deseja jogar de novo? ')
        again = int(input('Sim (1) ou Não (2)? '))
        if again == 1:
            continue
        elif again == 2:
            continuar = False
            break

    elif jogo==2:
        print('Iniciando Adivinhação')
        adivinhacao_definitiva.jogar()
        print('Deseja jogar de novo? ')
        again = int(input('Sim (1) ou Não (2)? '))
        if again == 1:
            continue
        elif again == 2:
            continuar = False
            break

print('Fim do jogo!')