N = int(input())
total = 0
total_C = 0
total_R = 0
total_S = 0

for i in range(N):
    qtd, animal = input().split(' ')
    qtd = int(qtd)
    total += qtd
    total_C += qtd if animal == 'C' else 0
    total_R += qtd if animal == 'R' else 0
    total_S += qtd if animal == 'S' else 0

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {total_C}')
print(f'Total de ratos: {total_R}')
print(f'Total de sapos: {total_S}')
print(f'Percentual de coelhos: {(100 * total_C / total):.2f} %')
print(f'Percentual de ratos: {(100 * total_R / total):.2f} %')
print(f'Percentual de sapos: {(100 * total_S / total):.2f} %')