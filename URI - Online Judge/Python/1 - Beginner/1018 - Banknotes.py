valor = int(input())

valores = [100, 50, 20, 10, 5, 2, 1]
qtd_notas = []

print(valor)
for i in range(7):
    qtd_notas.append(valor // valores[i])
    valor -= valores[i] * qtd_notas[i]
    print(f'{qtd_notas[i]} nota(s) de R$ {valores[i]},00')
