#EXE 005 - Crie uma variável chamada “adivinha” e defina o valor como 50. Peça ao usuário para inserir um número. Embora o palpite não seja o mesmo que o valor do “adivinha”, diga a ele se o palpite é muito baixo ou muito alto e peça que ele dê outro palpite. Se ele inserir o mesmo valor que “adivinha”, exiba a mensagem &quot;Parabéns! Você acertou o número em {} tentativas!&quot;.
adivinha = 50
teta = 0



while teta != 50 :
    num = int(input("tente acertar acertar um numero abaixo de 50: "))

    if num <= 49 :
        print("esta baixo")
        teta += 1
        
    elif num >= 51 :
        print('esta alto')
        teta += 1
    elif num ==50:
        teta += 1
        print('parabens voce acertou!!!')
        print('tentavias {}'.format(teta))
        break