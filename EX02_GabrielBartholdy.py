#EXE 002 - Peça ao usuário para inserir um número. Continue perguntando até que ele insira CINCO números, em seguida, exibam a mensagem “ O último número que você digitou foi um [número] &quot; e pare o programa.

i = 0

while i <5:
    numero = int(input('Digite um numero: '))
    i += 1
print("seu ultimo numero : {}".format(numero))