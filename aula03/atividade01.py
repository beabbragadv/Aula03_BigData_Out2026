salario_atual = float(input('Salário atual do funcionário: R$ '))
reajuste = salario_atual * 0.15

novo_salario = salario_atual + reajuste

print(f'\nSalario anterior: R$ {salario_atual:.2f}')
print(f'Valor do reajuste(15%): R$ {reajuste:.2f}')
print(f'Novo salario: R$ {novo_salario:.2f}')