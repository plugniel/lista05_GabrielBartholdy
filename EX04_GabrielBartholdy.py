#EXE 004 - Faça um programa que peça o nome do convidado que o usuario deseja convidar para uma festa. Depois disso, exiba a mensagem &quot;[nome] foi adicionado(a) com sucesso no convite!&quot; e adicione 1 à contagem. Em seguida, pergunte se ele quer convidar outra pessoa. Continue repetindo isso até que ele não queira mais convidar ninguém para a festa e, em seguida, mostre quantas pessoas foram convidas para a festa.
lista = []
total = 0
i = 0 

while i < 5 :
    numero = input("Digite o nome que deseja chamr a festa: ")
    pergu = input ("deseja incluir ele na lista?")
    
    if pergu == "s":
        lista.append(numero)
    else:
        break
        
print('o total dos pessoas adicionadas deu: {}'.format(lista))


print('Gabriel bartholdy')