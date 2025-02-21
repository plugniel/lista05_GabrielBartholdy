#EXE 001 . - Faça um programa que leia os números digitados pelo usuario, a cada número digitado ele deve ser somado ao anterior digitado e a cada soma exibida na tela, quando a soma for superior a 50 deve exibir a mensagem “ O total é... [total] ” e parar o programa.

total = 0
while True:
    num = int(input("Insira um numero: "))
    total += num
    if total > 50:
        print('o resultado deu {}'.format(total))
        break
