valores_pares = 0
for i in range(5):
    aux = int(input())
    valores_pares += 1 if aux % 2 == 0 else 0

print(f'{valores_pares} valores pares')
