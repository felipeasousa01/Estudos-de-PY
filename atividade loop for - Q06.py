####### ATIVIDADE LOOP WHILE ######
    # 06. Crie um programa que percorra uma string digitada pelo usuário e conte quantas vogais ela possui.
print("#### Contador de vogais ####")
string = input("Digite uma string: ")   
vogais = "aeiouAEIOU"
contador = 0  
palavra=""  
for palavra in string:
    if palavra in vogais:
        contador += 1   
print("A string digitada possui", contador, "vogais.")