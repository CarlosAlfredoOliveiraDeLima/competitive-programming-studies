valor = float(input())
cedulas_moedas = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.10, 0.05, 0.01]
qtd_cedulas_moedas = []

for i in range(11):
    qtd_cedulas_moedas.append(valor // cedulas_moedas[i])
    valor = float('%.2f' % (valor - qtd_cedulas_moedas[i] * cedulas_moedas[i]))

qtd_cedulas_moedas.append(valor / cedulas_moedas[11])

print('NOTAS:')
for i in range(6):
    print(f'{int(qtd_cedulas_moedas[i])} nota(s) de R$ {cedulas_moedas[i]:.2f}')
print('MOEDAS:')
for i in range(6, 12):
    print(f'{int(qtd_cedulas_moedas[i])} moeda(s) de R$ {cedulas_moedas[i]:.2f}')
