valores_pares = 0
valores_impares = 0
valores_positivos = 0
valores_negativos = 0
for i in range(5):
    aux = int(input())
    valores_pares += 1 if aux % 2 == 0 else 0
    valores_impares += 1 if aux % 2 != 0 else 0
    valores_positivos += 1 if aux > 0 else 0
    valores_negativos += 1 if aux < 0 else 0


print(f'{valores_pares} valor(es) par(es)')
print(f'{valores_impares} valor(es) impar(es)')
print(f'{valores_positivos} valor(es) positivo(s)')
print(f'{valores_negativos} valor(es) negativo(s)')
