print("#### Calculadora Simples ####")

# Lê o primeiro número
num1 = float(input("Digite o primeiro número: "))

# Lê a primeira operação
operacao1 = input("Digite a primeira operação (+, -, *, /): ")

# Lê o segundo número
num2 = float(input("Digite o segundo número: "))

# Calcula o primeiro resultado
if operacao1 == '+':
    resultado = num1 + num2
elif operacao1 == '-':
    resultado = num1 - num2
elif operacao1 == '*':
    resultado = num1 * num2
elif operacao1 == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: divisão por zero.")
        exit()
else:
    print("Operação inválida.")
    exit()

# Lê a segunda operação
operacao2 = input("Digite a segunda operação (+, -, *, /): ")

# Lê o terceiro número
num3 = float(input("Digite o terceiro número: "))

# Calcula o resultado final
if operacao2 == '+':
    resultado = resultado + num3
elif operacao2 == '-':
    resultado = resultado - num3
elif operacao2 == '*':
    resultado = resultado * num3
elif operacao2 == '/':
    if num3 != 0:
        resultado = resultado / num3
    else:
        print("Erro: divisão por zero.")
        exit()
else:
    print("Operação inválida.")
    exit()

# Exibe o resultado final
print("O resultado final é: %.2f" % resultado)