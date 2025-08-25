####### ATIVIDADE LOOP WHILE ######
    # 03. Escreva um programa que mostre a tabuada de um número escolhido pelo usuário, de 1 até 10, usando while.
numero=int(input("Digite um número para ver a tabuada: "))
contador=1
print("#### Taboada do", numero, "####")
while contador <= 10:
    print(numero, "x", contador, "=", numero*contador)
    contador+=1 