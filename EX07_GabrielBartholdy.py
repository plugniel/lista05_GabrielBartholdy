#EXE 007 . Escreva um programa que permaneça em laço lendo números inteiros. O laço termina quando for digitado 0 (zero). Cada valor diferente de zero digitado deve ser colocado em uma lista, desde que ele ainda não esteja lá, ou seja, valores repetidos não são aceitos. Se um valor repetido for digitado, o programa deve exibir uma mensagem na tela. Ao final exiba a lista e a quantidade de elementos que ela contém.

lista = []
i = 0

while i < 1:
    nome = input('insira o nome que deseja adicionar: ')
    if nome in lista :
        lista.index(nome)
        print('ja cadastrado')
    if nome == 'sair':
        print(lista)
        break
      
    else:
        lista.append(nome)
