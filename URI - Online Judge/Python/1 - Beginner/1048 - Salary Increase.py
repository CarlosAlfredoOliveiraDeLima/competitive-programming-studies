salario = float(input())
if 0 < salario <= 400:
    novo_salario = salario + salario * 0.15
elif 400 < salario <= 800:
    novo_salario = salario + salario * 0.12
elif 800 < salario <= 1200:
    novo_salario = salario + salario * 0.10
elif 1200 < salario <= 2000:
    novo_salario = salario + salario * 0.07
else:
    novo_salario = salario + salario * 0.04

print(f'Novo salario: {(novo_salario):.2f}')
print(f'Reajuste ganho: {(novo_salario - salario):.2f}')
print(f'Em percentual: {(((novo_salario / salario) - 1 ) * 100):.0f} %')
