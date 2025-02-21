#EXE 003 - Peça ao usuário para inserir um número e, em seguida, insira outro número. Some esses dois números e pergunte se ele quer adicionar outro número. Se ele digitar “ s &quot;, diga para inserir outro número e continuar adicionando números e somando até que ele não respondam “ s &quot;. Depois que o loop for interrompido, exiba o total.


total = 0
i = 0 

while i < 5 :
    numero = int(input("Digite o numero que deseja fazer a soma: "))
    pergu = input ("deseja incluir ele no total?")
    i += 1
    if pergu == "s":
        total += numero
    else:
        break
        
print('o total dos numeros adicionado deu: {}'.format(total))


print('Gabriel bartholdy')