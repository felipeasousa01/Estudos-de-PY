####### ATIVIDADE LOOP WHILE ######
    # 02. Crie um programa que peça uma senha ao usuário e só termine quando a senha correta "python123" for digitada.

print("#### Sistema de Login ####")
# Programa para verificar senha

senha_correta = "python123"
senha = ""

while senha != senha_correta:
    senha = input("Digite a senha: ")

print("Senha correta! Acesso liberado.")

