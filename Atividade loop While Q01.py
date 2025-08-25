####### ATIVIDADE LOOP WHILE ######
    # 01. Faça um programa que peça números ao usuário até que ele digite 0. Ao final, mostre a soma de todos os números digitados.

print("#### Sistema de Somas ####")

soma = 0
numero = ""
while numero != 0:
    numero = int(input("Digite um número "))
    soma += numero
print("A soma dos números digitados é:", soma)

