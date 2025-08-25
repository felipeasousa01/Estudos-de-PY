####### ATIVIDADE LOOP WHILE ######
    # 05. Escreva um programa que leia 5 números e mostre o maior deles.
print("#### Maior número ####")
maior = ""
for i in range(5):
    numero = int(input("Digite um número:  "))
    if maior == "" or numero > maior:
        maior = numero  
print("O maior número digitado foi:", maior)