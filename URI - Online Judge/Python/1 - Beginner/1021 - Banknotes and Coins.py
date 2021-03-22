valor = float(input())
cedulas_moedas = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
qtd_cedulas_moedas = []

for i in range(12):
    qtd_cedulas_moedas.append(int(valor // cedulas_moedas[i]))
    valor -= qtd_cedulas_moedas[i] * cedulas_moedas[i]

print('NOTAS:')
for i in range(7):
    print(f'{qtd_cedulas_moedas[i]} nota(s) de R$ {cedulas_moedas[i]:.2f}')
print('MOEDAS:')
for i in range(6,13):
    print(f'{qtd_cedulas_moedas[i]} moeda(s) de R$ {cedulas_moedas[i]:.2f}')