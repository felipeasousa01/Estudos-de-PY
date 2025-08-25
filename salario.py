# Exercício – Cálculo de Salário com Descontos

# Solicita os dados ao usuário
valor_hora = float(input("Digite o valor recebido por hora trabalhada: R$ "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

# Cálculos
salario_bruto = valor_hora * horas_trabalhadas
desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (desconto_ir + desconto_inss + desconto_sindicato)

# Saída formatada
print(f" + Salário Bruto    : R$ {salario_bruto:.2f}")
print(f"- IR (11%)           : R$ {desconto_ir:.2f}")
print(f"- INSS (8%)          : R$ {desconto_inss:.2f}")
print(f"- Sindicato (5%)     : R$ {desconto_sindicato:.2f}")
print(f"= Salário Líquido  : R$ {salario_liquido:.2f}")
