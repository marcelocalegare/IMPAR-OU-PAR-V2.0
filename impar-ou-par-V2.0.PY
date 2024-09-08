from random import randint



par_impar = """DIGITE UMA OPÇÃO:
[P] - PAR
[I] - IMPAR"""

cont = 0

print('='*30)
print(f'{VAMOS JOGAR IMPAR OU PAR:=^30}')
print('='*30)

while True:
    computador = randint(0,10)
    n = int(input('DIGITE UM NUMERO DE 0 A 10: '))
    while n > 10:
        print(f'|VALOR NÃO ACEITO!|')
        n = int(input('DIGITE UM NUMERO DE 0 A 10: '))
    print(f'|VALOR ACEITO, MUITO BEM!|\n')
    
    print(par_impar)
    opc = str(input('\nQUAL OPÇÃO VOCÊ ESCOLHE?')).strip().upper() 
    while opc not in 'PI':
       print('\n|OPÇÃO INVALIDA!|\n')
       print(par_impar)
       opc = str(input('QUAL OPÇÃO VOCÊ ESCOLHE? ')).strip().upper()
    
    print('='*30)
    print(f'O JOGADOR ESCOLHEU [{n}]')
    print(f'O COMPUTADOR ESCOLHEU [{computador}]')
    if(n+computador) % 2 == 0:
        print(f'O valor {n+computador} é PAR!\n')
    else:
        print(f'O valor {n+computador} é IMPAR!\n')

    if opc == 'P':
        if(n+computador) % 2 == 0:
            print(f'O jogador VENCEU! Vamos jogar novamente...')
            print('='*30)
            cont += 1
        else:
            print(f'GAME OVER!! Você venceu {cont} vezes!')
            print('FIM DO PROGRAMA')
            print('='*30)
            break
    if opc == 'I':
        if(n+computador) % 2 == 1:
            print('O jogador VENCEU! Vamos jogar novamente...')
            print('='*30)
            cont +=1
        else:
            print(f'GAME OVER!! Você venceu {cont} vezes!')
            print('FIM DO PROGRAMA')
            print('='*30)
            break
