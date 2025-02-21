#EXE 006 - Peça ao usuário para inserir um número entre 15 e 20. Se ele inserir um valor abaixo de 15, exiba a mensagem &quot;Muito baixo&quot; e peça que tentem novamente. Se ele inserir um valor acima de 20, exiba a mensagem &quot;Muito alto&quot; e peça que tentem novamente. Continue repetindo isso até que ele insira um valor entre 15 e 20 e, em seguida, exibam a mensagem &quot;Obrigado&quot;.
teta = 0
while teta <1 :
    num = int(input("tente acertar acertar um numero abaixo de 50: "))

    if num <= 14 :
        print("esta baixo")

        
    elif num >= 21 :
        print('esta alto')

    elif num >= 15 and num <= 20:

        print('parabens voce acertou!!!')
        break